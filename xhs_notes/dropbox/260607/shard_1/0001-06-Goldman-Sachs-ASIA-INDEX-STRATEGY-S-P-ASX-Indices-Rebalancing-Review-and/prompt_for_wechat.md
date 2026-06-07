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
ASIA INDEX STRATEGY

# S&P/ASX Indices Rebalancing Review and Flow Implications (June 2026)

What happened? S&P Dow Jones Indices (S&P DJI) announced its quarterly review results for the S&P/ASX Index Series after market close on June 5 (Friday). All changes will take effect after market close on June 19 (Friday).

Constituent Changes: There are 1, 1, and 5 stock changes for the S&P/ASX 50, 100, and 200 indices, respectively. For the ASX 200 index, ELV, EOS, FFM, KCN, and MI6 will replace GYG, IEL, SDR, TPW, and WEB. Overall, around $0.3\%$ of ASX 200 index weights will be adjusted. (Exhibit 3)

Index Implications: The proforma index cap is estimated at US\$1,873 billion for ASX 200. Following the rebalancing, forward 12-month P/E is expected to shift from 16.6x to 16.7x, trailing dividend yield will remain unchanged at 3.5%, and EPS growth (2026-27 CAGR) will change from 13.7% to 13.9% for ASX200. (Exhibit 1)

Sector Implications: Metals & Mining (+US\$80mn) and Capital Goods (+US\$50mn) are poised to see the largest passive inflows, while Consumer Retail (-US\$80mn) may face the biggest outflows. Overall, we estimate that the S&P/ASX rebalancing could generate over US\$900mn of gross two-way passive trading flows. (Exhibit 4)

Historical vs. Current Patterns: ASX 200 additions vs. deletions have traded along a highly volatile path ahead of the announcement; historically, post-announcement performance remains volatile with a modest negative bias, before rebounding around the effective date. (Exhibit 2)

We highlight the index and sector changes, as well as the passive flow implications for stock additions and deletions.

Alvin So, CFA

+852-2978-1585 | alvin.so@gs.com

GS (Asia) L.L.C.

Timothy Moe, CFA

+65-6889-1199 | timothy.moe@gs.com

GS (Singapore) Pte

Matthew Ross

+61(3)9679-1616

matthew.ross@gs.com

GS Australia Pty Ltd

Tony Wu

+61(3)9679-1402 | tony.wu@gs.com

GS Australia Pty Ltd

Exhibit 1: S&P DJI has announced its quarterly review results for the S&P/ASX Index Series, effective after market close on June 19 (Friday)

<table><tr><td rowspan="2"></td><td rowspan="2">S&amp;P/ASX Indices</td><td colspan="3">Jun 2026 Review Summary</td></tr><tr><td>ASX 50</td><td>ASX Mid-Cap 50</td><td>ASX 200</td></tr><tr><td rowspan="3">Stock Changes</td><td>Current # Constituents</td><td>50</td><td>50</td><td>200</td></tr><tr><td># Stocks Added / Deleted</td><td>1 / 1</td><td>2 / 2</td><td>5 / 5</td></tr><tr><td>% Weight Rebalanced</td><td>0.6%</td><td>4.9%</td><td>0.3%</td></tr><tr><td rowspan="4">Liquidity</td><td>Current Index Cap (US$bn)</td><td>1,489</td><td>231</td><td>1,872</td></tr><tr><td>Proforma % Change</td><td>+0.1%</td><td>-0.6%</td><td>+0.0%</td></tr><tr><td>Current 3M ADVT (US$bn)</td><td>3.7</td><td>1.0</td><td>5.5</td></tr><tr><td>Proforma % Change</td><td>-0.1%</td><td>+1.8%</td><td>+0.6%</td></tr><tr><td rowspan="3">Valuations / Growth</td><td>NTM P/E (x)(Current / Proforma)</td><td>17.2x /17.1x</td><td>15.3x /15.6x</td><td>16.6x /16.7x</td></tr><tr><td>LTM Dividend Yield (%) (Current / Proforma)</td><td>3.6% /3.6%</td><td>3.0% /3.0%</td><td>3.5% /3.5%</td></tr><tr><td>2026-27 EPS Growth (%) (Current / Proforma)</td><td>10.3% /10.3%</td><td>19.9% /20.8%</td><td>13.7% /13.9%</td></tr><tr><td>Passive Flows</td><td>Potential Gross Passive Buying + Selling (Two-way) (US$mn)</td><td>9</td><td>57</td><td>490</td></tr><tr><td rowspan="2">Trading Pattern Prior to Announce.</td><td>Return Since 10D Prior to Ann.(Additions / Deletions)</td><td>-1.5% /+29.5%</td><td>+14.6% /-0.9%</td><td>-12.2% /-5.5%</td></tr><tr><td>Share Turnover % Chg (Median 20D vs.Prior 3M) (Add / Del)</td><td>+8% /-21%</td><td>-8% /+6%</td><td>+0% /+53%</td></tr></table>

Note: Pricing is as of Jun 5, 2026  
Source: S&P/ASX, Bloomberg, FactSet, Refinitiv, EPFR, GS Global Investment Research

Exhibit 2: ASX 200: Additions vs. deletions have traded along a highly volatile path ahead of the announcement; historically, post-announcement performance remains volatile with a modest negative bias, before rebounding around the effective date

![](images/c2979a8128919d44f9e2a4642dc87b9015f3026f8e7fbb74bb614baae3684d40.jpg)

<details>
<summary>line chart</summary>

| # workdays before/after index review announcement date | Past Add/Del Median | Current (5-Jun-26) |
| ----------------------------------------------------- | ------------------- | ------------------ |
| -20                                                   | 103                 | 88                 |
| -15                                                   | 101                 | 104                |
| -10                                                   | 101                 | 107                |
| -5                                                    | 101                 | 108                |
| 0                                                     | 100                 | 100                |
| 5                                                     | 100                 | 100                |
| 10                                                    | 99                  | 100                |
| 15                                                    | 101                 | 100                |
| 20                                                    | 101                 | 100                |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 3: Stocks that may experience net passive buying or selling flows following the S&P/ASX indices rebalancing (only additions and deletions are shown)

<table><tr><td rowspan="2">BBG Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">Sector</td><td rowspan="2">Listed Mkt Cap (US$mn)</td><td rowspan="2"># Free Float Cap (US$mn)</td><td rowspan="2">3M ADVT (US$mn)</td><td colspan="3">Potential Passive Flows (US$mn)</td><td rowspan="2">Net Passive Flows (US$mn)</td><td rowspan="2">Net Flows /3M ADVT (days)</td><td rowspan="2">S3&#x27;s Short Interest 20D Chg (pp)</td><td rowspan="2">Days to Cover (1M ADVT)</td><td rowspan="2">S3&#x27;s HF Long Interest 20D Chg (pp)</td><td rowspan="2">Return since 20D prior to ann.</td><td rowspan="2">Return since 10D prior to ann.</td><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M)</td><td colspan="2">Corporate Event Dates</td></tr><tr><td>ASX 50</td><td>ASX Mid. Cap 50</td><td>ASX 200</td><td>Expected Next Report</td><td>Ex-Dividend</td></tr><tr><td colspan="6">Stocks with net passive buying following S&amp;P/ASX indices rebalancing (Additions)</td><td colspan="3">(Additions Only)</td><td colspan="2">(ranked)</td><td colspan="8"></td></tr><tr><td>ELV AT</td><td>Elevra Lithium</td><td>Metals &amp; Mining</td><td>1,592</td><td>1,353</td><td>15</td><td>-</td><td>-</td><td>53</td><td>54</td><td>3.5</td><td>(3.2%)</td><td>2.0</td><td>0.0%</td><td>(18%)</td><td>(20%)</td><td>63%</td><td>Aug 31</td><td></td></tr><tr><td>EOS AT</td><td>Electro Optic Systems</td><td>Capital Goods</td><td>1,633</td><td>1,345</td><td>23</td><td>-</td><td>-</td><td>53</td><td>54</td><td>2.3</td><td>-</td><td>-</td><td>0.0%</td><td>23%</td><td>24%</td><td>5%</td><td>Aug 20</td><td></td></tr><tr><td>MI6 AT</td><td>Minerals 260</td><td>Metals &amp; Mining</td><td>1,385</td><td>1,095</td><td>6</td><td>-</td><td>-</td><td>43</td><td>43</td><td>7.7</td><td>0.2%</td><td>4.1</td><td>-</td><td>(3%)</td><td>(8%)</td><td>0%</td><td>Sep 29</td><td></td></tr><tr><td>FFM AT</td><td>FireFly Metals Ltd</td><td>Metals &amp; Mining</td><td>1,142</td><td>1,087</td><td>7</td><td>-</td><td>-</td><td>43</td><td>43</td><td>6.1</td><td>0.8%</td><td>8.3</td><td>(0.2%)</td><td>3%</td><td>0%</td><td>(19%)</td><td>Sep 8</td><td></td></tr><tr><td>KCN AT</td><td>Kingsgate Consolidated</td><td>Metals &amp; Mining</td><td>1,007</td><td>956</td><td>7</td><td>-</td><td>-</td><td>37</td><td>38</td><td>5.3</td><td>0.0%</td><td>1.2</td><td>0.0%</td><td>(28%)</td><td>(16%)</td><td>(17%)</td><td>Mar 4</td><td></td></tr><tr><td>PME AT</td><td>Pro Medicus</td><td>Health Care</td><td>11,878</td><td>6,549</td><td>32</td><td>(3)</td><td>17</td><td>-</td><td>14</td><td>0.4</td><td>1.0%</td><td>13.6</td><td>0.1%</td><td>28%</td><td>29%</td><td>(21%)</td><td>Aug 14</td><td></td></tr><tr><td>PDN AT</td><td>Paladin Energy</td><td>Energy</td><td>3,491</td><td>3,491</td><td>23</td><td>-</td><td>9</td><td>-</td><td>5</td><td>0.2</td><td>1.5%</td><td>17.8</td><td>0.2%</td><td>(12%)</td><td>(0%)</td><td>6%</td><td>Aug 28</td><td></td></tr><tr><td colspan="6">Stocks with net passive selling following S&amp;P/ASX indices rebalancing (Deletions)</td><td colspan="3">(Deletions Only)</td><td colspan="2">(ranked)</td><td colspan="8"></td></tr><tr><td>GYG AT</td><td>Guzman y Gomez</td><td>Consumer Retail &amp; Services</td><td>1,359</td><td>747</td><td>6</td><td>-</td><td>-</td><td>(29)</td><td>(29)</td><td>(5.1)</td><td>(1.0%)</td><td>27.9</td><td>0.0%</td><td>1%</td><td>(6%)</td><td>55%</td><td>Aug 24</td><td></td></tr><tr><td>SDR AT</td><td>SiteMinder</td><td>Software &amp; Services</td><td>776</td><td>713</td><td>4</td><td>-</td><td>-</td><td>(28)</td><td>(28)</td><td>(7.1)</td><td>(1.0%)</td><td>9.8</td><td>0.0%</td><td>23%</td><td>38%</td><td>(10%)</td><td>Aug 27</td><td></td></tr><tr><td>WEB AT</td><td>WEB Travel</td><td>Consumer Retail &amp; Services</td><td>623</td><td>614</td><td>6</td><td>-</td><td>-</td><td>(24)</td><td>(24)</td><td>(4.2)</td><td>0.8%</td><td>5.9</td><td>0.0%</td><td>(13%)</td><td>3%</td><td>56%</td><td>Nov 18</td><td></td></tr><tr><td>ALQ AT</td><td>ALS</td><td>Capital Goods</td><td>8,596</td><td>8,585</td><td>26</td><td>5</td><td>(22)</td><td>-</td><td>(17)</td><td>(0.6)</td><td>0.3%</td><td>3.2</td><td>0.0%</td><td>6%</td><td>(1%)</td><td>8%</td><td>Nov 23</td><td>Jun 12</td></tr><tr><td>IEL AT</td><td>IDP Education</td><td>Consumer Retail &amp; Services</td><td>409</td><td>396</td><td>6</td><td>-</td><td>-</td><td>(16)</td><td>(16)</td><td>(2.5)</td><td>0.3%</td><td>2.7</td><td>0.0%</td><td>(30%)</td><td>(25%)</td><td>53%</td><td>Aug 20</td><td></td></tr><tr><td>TPW AT</td><td>Temple &amp; Webster</td><td>Consumer Retail &amp; Services</td><td>408</td><td>327</td><td>6</td><td>-</td><td>-</td><td>(13)</td><td>(13)</td><td>(2.3)</td><td>1.5%</td><td>5.7</td><td>(0.0%)</td><td>(21%)</td><td>(8%)</td><td>48%</td><td>Aug 18</td><td></td></tr><tr><td>MTS AT</td><td>Metcash</td><td>Consumer Staples</td><td>2,379</td><td>2,379</td><td>11</td><td>-</td><td>(6)</td><td>-</td><td>(6)</td><td>(0.5)</td><td>0.3%</td><td>7.5</td><td>0.0%</td><td>11%</td><td>(0%)</td><td>4%</td><td>Jun 22</td><td></td></tr><tr><td rowspan="2"></td><td colspan="2">ASX 200 Median</td><td>3,733</td><td>2,770</td><td>14</td><td rowspan="2" colspan="8"></td><td>(1%)</td><td>(0%)</td><td>(6%)</td><td rowspan="2" colspan="2"></td></tr><tr><td colspan="2">ASX 300 Median</td><td>1,808</td><td>1,324</td><td>6</td><td>(2%)</td><td>0%</td><td>(4%)</td></tr></table>

Note (1): Free Float Cap is calculated based on ASX-registered share assumptions prior to the current index review, and the average free float % estimates from Bloomberg, FactSet, and Refinitiv. Pricing is as of Jun 5, 2026
Note (2): Passive fund AUM is derived from EPFR and FactSet ownership data, along with our estimation of identifiable index-tracking portions from non-public funds.  
Source: S&P/ASX, FactSet, Refinitiv, Bloomberg, EPFR, GS Global Investment Research

Exhibit 4: Metals & Mining and Capital Goods are poised to see the largest passive inflows, while Consumer Retail may face the biggest outflows  
Current vs. Proforma Sector Weights and Changes in Major S&P/ASX Indices, and Aggregate Potential Passive Flows

<table><tr><td rowspan="2" colspan="2">GICS Sector/Industry</td><td colspan="4">ASX 50</td><td colspan="4">ASX Mid-Cap 50</td><td colspan="3">ASX 200</td><td colspan="3">Passive Flows (US$mn)</td><td></td></tr><tr><td>Current %</td><td>Proforma %</td><td colspan="2">Change (bps)</td><td>Current %</td><td>Proforma %</td><td colspan="2">Change (bps)</td><td>Current %</td><td>Proforma %</td><td>Change (bps)</td><td>Gross Buying</td><td>Gross Selling</td><td>Net Flows</td><td></td></tr><tr><td rowspan="2">Financials</td><td>Banks</td><td>28.9%</td><td>28.9%</td><td></td><td>-2</td><td>3.0%</td><td>3.0%</td><td></td><td>+2</td><td>23.4%</td><td>23.4%</td><td></td><td>-1</td><td>32</td><td>-5</td><td>27</td></tr><tr><td>Insurance &amp; Other Financials</td><td>9.2%</td><td>9.2%</td><td></td><td>-1</td><td>7.4%</td><td>7.4%</td><td></td><td>-6</td><td>9.2%</td><td>9.1%</td><td></td><td>-2</td><td>12</td><td>-36</td><td>-24</td></tr><tr><td></td><td>Real Estate</td><td>4.8%</td><td>4.8%</td><td></td><td>-0</td><td>9.8%</td><td>9.9%</td><td></td><td>+5</td><td>5.9%</td><td>5.9%</td><td></td><td>-0</td><td>10</td><td>-5</td><td>5</td></tr><tr><td rowspan="7">Domestic / Global Cyclicals</td><td>Capital Goods</td><td>2.0%</td><td>2.6%</td><td></td><td>+57</td><td>11.5%</td><td>7.8%</td><td></td><td>368</td><td>4.0%</td><td>4.1%</td><td></td><td>+7</td><td>69</td><td>-24</td><td>45</td></tr><tr><td>Transportation</td><td>2.9%</td><td>2.9%</td><td></td><td>-0</td><td>6.6%</td><td>6.6%</td><td></td><td>+3</td><td>3.3%</td><td>3.3%</td><td></td><td>-1</td><td>4</td><td>-10</td><td>-6</td></tr><tr><td>Autos &amp; Components</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.1%</td><td>0.1%</td><td></td><td>-0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Consumer Retail &amp; Services</td><td>6.8%</td><td>6.8%</td><td></td><td>-1</td><td>3.7%</td><td>3.7%</td><td></td><td>+1</td><td>6.6%</td><td>6.5%</td><td></td><td>-12</td><td>7</td><td>-88</td><td>-80</td></tr><tr><td>Tech Hardware &amp; Semis</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.2%</td><td>0.2%</td><td></td><td>-0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Software &amp; Services</td><td>1.1%</td><td>1.0%</td><td></td><td>-0</td><td>7.9%</td><td>8.0%</td><td></td><td>+4</td><td>2.1%</td><td>2.0%</td><td></td><td>-4</td><td>3</td><td>-29</td><td>-26</td></tr><tr><td>Internet/Media &amp; Entertainment</td><td>0.5%</td><td>0.5%</td><td></td><td>-0</td><td>3.9%</td><td>3.9%</td><td></td><td>-3</td><td>1.0%</td><td>1.0%</td><td></td><td>-1</td><td>0</td><td>-14</td><td>-14</td></tr><tr><td rowspan="3">Commodities</td><td>Energy</td><td>4.0%</td><td>4.0%</td><td></td><td>-0</td><td>5.1%</td><td>6.6%</td><td></td><td>156</td><td>4.6%</td><td>4.6%</td><td></td><td>-1</td><td>15</td><td>-19</td><td>-4</td></tr><tr><td>Metals &amp; Mining</td><td>26.3%</td><td>26.3%</td><td></td><td>-7</td><td>20.9%</td><td>21.1%</td><td></td><td>+12</td><td>25.7%</td><td>25.9%</td><td></td><td>+15</td><td>215</td><td>-143</td><td>72</td></tr><tr><td>Chemicals &amp; Other Materials</td><td>0.5%</td><td>0.5%</td><td></td><td>-0</td><td>7.4%</td><td>7.5%</td><td></td><td>+13</td><td>1.4%</td><td>1.4%</td><td></td><td>+1</td><td>20</td><td>-1</td><td>19</td></tr><tr><td></td><td>Consumer Staples</td><td>3.5%</td><td>3.5%</td><td></td><td>-0</td><td>4.8%</td><td>3.7%</td><td></td><td>103</td><td>3.5%</td><td>3.5%</td><td></td><td>-0</td><td>5</td><td>-10</td><td>-6</td></tr><tr><td rowspan="3">Defensives</td><td>Health Care</td><td>5.1%</td><td>4.6%</td><td></td><td>-46</td><td>6.5%</td><td>9.3%</td><td></td><td>283</td><td>5.0%</td><td>5.0%</td><td></td><td>-2</td><td>23</td><td>-47</td><td>-24</td></tr><tr><td>Utilities</td><td>1.6%</td><td>1.6%</td><td></td><td>-0</td><td>1.6%</td><td>1.6%</td><td></td><td>+1</td><td>1.4%</td><td>1.4%</td><td></td><td>-0</td><td>2</td><td>0</td><td>2</td></tr><tr><td>Telecommunication Services</td><td>2.7%</td><td>2.7%</td><td></td><td>-0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>2.5%</td><td>2.5%</td><td></td><td>+1</td><td>16</td><td>-2</td><td>14</td></tr></table>

Note: Proforma changes reflect additions and deletions. Pricing is as of Jun 5, 2026  
Source: S&P/ASX, FactSet, Refinitiv, EPFR, GS Global Investment Research

## Disclosure Appendix

## Reg AC

I, Matthew Ross, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

We, Alvin So, CFA, Timothy Moe, CFA and Tony Wu, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alvin So, CFA GS (Asia) L.L.C., Timothy Moe, CFA GS (Singapore) Pte, Matthew Ross GS Australia Pty Ltd, Tony Wu GS Australia Pty Ltd.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subj

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
