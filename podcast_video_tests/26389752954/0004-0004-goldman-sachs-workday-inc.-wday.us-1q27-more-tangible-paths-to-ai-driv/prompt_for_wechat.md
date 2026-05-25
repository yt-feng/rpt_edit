你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 1800 字，允许上下浮动 15%。
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
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来社群继续拆完整报告。
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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Workday Inc. (WDAY)

1Q27: More tangible paths to AI-driven value

WDAY

12m Price Target: \$151.00

Price: \$121.85

Upside: $23.9\%$

WDAY is indicated +11% post 1QFY27 results. Workday was able to start FY27 on better footing, following a disappointing 4Q and against bearish expectations from most investors we talked to ahead of earnings. Subscription revenue was 80bps ahead of the Street, EBIT margin was \~130bps ahead of Street/guidance, and EPS was 6% above (FactSet). cRPO growth was 15.5% y/y, which we estimate normalizes to \~13.5% when adjusting for M&A, and is an uptick from 4Q. FY27 subscription guidance of 12-13% is unchanged, and F2Q27 was guided in line with GS/the Street (+13% y/y). The company noted the best 1Q for NNACV growth in five years, and agentic ARR at \$500mn or >30% NNARR on our estimates. Adjusting for AI revenue, we believe Workday's "core" subscription revenue growth is stable at around \~12% for the fifth quarter in a row. Post his first quarter back as CEO, cofounder Aneel Bhusri emphasized the company is reinventing itself in the current period of AI disruption, by going back to its founding principles and placing leaders from the companies they've acquired in key leadership roles. For example, Joel Hellermark (founder of Sana) was named Chief AI Officer today.

Workday expanded on the vision for “lights out” finance and HR they outlined last quarter, which intergrates a vision of “headless” enterprise software that lets Workday monetize through three paths: 1) selling their own agents and owning the TCO/success; 2) growing Extend Pro which allows customers to build AI apps on top of Workday; and 3) providing the rails/APIs for an ecosystem of third-party builders. In addition to that, Workday’s entry into ITSM (announced today) is aimed at broadening the TAM and leveraging Workday’s domain experience in the employee lifecycle. Ultimately, these avenues of monetization will be key to offsetting slowing growth (and potentially pricing pressure) in the seat-count based SaaS business. While 1Q exceeded low buyside expectations, a sustained re-rating for the stock will likely depend on the successful rollout of organically built AI agents

# NEUTRAL

# Gabriela Borges, CFA

+1(212)902-7839 | gabriela.borges@gs.com

Goldman Sachs & Co. LLC

# Noah Naparst

+1(917)343-6395 | noah.x.naparst@gs.com

Goldman Sachs & Co. LLC

# Praachi Arora

+1(332)245-7970 | praachi.arora@gs.com

Goldman Sachs India SPL

Key Data

Market cap: \$31.8bn

Enterprise value: \$34.1bn

3m ADTV: \$710.5mn

United States

Americas Software

M&A Rank: 3

GS Forecast 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>Revenue ($ mn) New</td><td>9,552.0</td><td>10,662.1</td><td>11,752.1</td><td>12,855.7</td></tr><tr><td>Revenue ($ mn) Old</td><td>9,552.0</td><td>10,644.4</td><td>11,722.5</td><td>12,810.8</td></tr><tr><td>EBITDA ($ mn)</td><td>3,066.0</td><td>3,429.9</td><td>3,827.6</td><td>4,239.9</td></tr><tr><td>EBIT ($ mn)</td><td>2,823.0</td><td>3,253.4</td><td>3,644.6</td><td>4,034.8</td></tr><tr><td>EPS ($) New</td><td>9.21</td><td>10.96</td><td>13.45</td><td>16.68</td></tr><tr><td>EPS ($) Old</td><td>9.23</td><td>10.50</td><td>12.19</td><td>14.05</td></tr><tr><td>P/E (X)</td><td>25.4</td><td>11.1</td><td>9.1</td><td>7.3</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.5</td><td>0.7</td><td>0.3</td><td>(0.1)</td></tr><tr><td></td><td>4/26</td><td>7/26E</td><td>10/26E</td><td>1/27E</td></tr><tr><td>EPS ($)</td><td>2.66</td><td>2.65</td><td>2.69</td><td>2.97</td></tr></table>

GS Factor Profile   
![](images/793506e847a869ce2b6ab80f7dff27ecc963a3b5c2d8822cf726e733f81ef8aa.jpg)

<details>
<summary>bar</summary>

| Category | WDAY relative to Americas Coverage (Percentile) | WDAY relative to Americas Software (Percentile) |
| :--- | :--- | :--- |
| Growth | 68 | 31 |
| Financial Returns | 85 | 75 |
| Multiple | 35 | 12 |
| Integrated | 72 | 65 |
</details>

Source: Company data, Goldman Sachs Research estimates.   
See disclosures for details.

# NEUTRAL

# Workday Inc. (WDAY)

Rating since Jan 11, 2026

Ratios & Valuation 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>P/E (X)</td><td>25.4</td><td>11.1</td><td>9.1</td><td>7.3</td></tr><tr><td>EV/EBITDA (X)</td><td>20.7</td><td>9.4</td><td>7.5</td><td>5.6</td></tr><tr><td>EV/sales (X)</td><td>6.7</td><td>3.0</td><td>2.4</td><td>1.9</td></tr><tr><td>FCF yield (%)</td><td>4.5</td><td>10.4</td><td>15.6</td><td>19.3</td></tr><tr><td>EV/DACF (X)</td><td>21.2</td><td>11.0</td><td>8.8</td><td>6.7</td></tr><tr><td>CROCI (%)</td><td>21.6</td><td>20.9</td><td>23.5</td><td>27.6</td></tr><tr><td>ROE (%)</td><td>29.3</td><td>37.0</td><td>44.9</td><td>50.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.5</td><td>0.7</td><td>0.3</td><td>(0.1)</td></tr><tr><td>Net debt/equity (%)</td><td>19.0</td><td>35.0</td><td>19.9</td><td>(6.1)</td></tr><tr><td>Interest cover (X)</td><td>25.6</td><td>29.5</td><td>48.4</td><td>53.6</td></tr><tr><td>Inventory days</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Receivable days</td><td>81.8</td><td>85.4</td><td>81.6</td><td>77.2</td></tr><tr><td>Days payable outstanding</td><td>23.1</td><td>24.4</td><td>24.6</td><td>24.8</td></tr></table>

Growth & Margins (%) 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>Total revenue growth</td><td>13.1</td><td>11.6</td><td>10.2</td><td>9.4</td></tr><tr><td>EBITDA growth</td><td>26.0</td><td>11.9</td><td>11.6</td><td>10.8</td></tr><tr><td>EPS growth</td><td>25.8</td><td>18.9</td><td>22.8</td><td>24.0</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Gross margin</td><td>79.3</td><td>78.6</td><td>78.3</td><td>78.2</td></tr><tr><td>EBIT margin</td><td>29.6</td><td>30.5</td><td>31.0</td><td>31.4</td></tr></table>

Price Performance   
![](images/bda781538bc9eecd49590a8eb13c4af2dd3972e7d681307a5531f0d4126e9df0.jpg)

<details>
<summary>line</summary>

|        | 3m     | 6m     | 12m    |
| ------ | ------ | ------ | ------ |
| Absolute | (11.6)% | (45.9)% | (54.6)% |
| Rel. to the S&P 500 | (17.9)% | (52.0)% | (64.4)% |
</details>

Source: FactSet. Price as of 21 May 2026 close.

Income Statement (\$ mn) 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>Total revenue</td><td>9,552.0</td><td>10,662.1</td><td>11,752.1</td><td>12,855.7</td></tr><tr><td>Cost of goods sold</td><td>(1,976.0)</td><td>(2,277.1)</td><td>(2,552.5)</td><td>(2,807.1)</td></tr><tr><td>SG&amp;A</td><td>(2,807.0)</td><td>(3,066.6)</td><td>(3,324.8)</td><td>(3,605.1)</td></tr><tr><td>R&amp;D</td><td>(1,946.0)</td><td>(2,065.1)</td><td>(2,230.3)</td><td>(2,408.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>3,066.0</td><td>3,429.9</td><td>3,827.6</td><td>4,239.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(349.0)</td><td>(254.4)</td><td>(235.0)</td><td>(257.1)</td></tr><tr><td>EBIT</td><td>2,823.0</td><td>3,253.4</td><td>3,644.6</td><td>4,034.8</td></tr><tr><td>Net interest inc./(exp.)</td><td>287.7</td><td>63.8</td><td>68.5</td><td>83.4</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>3,110.7</td><td>3,317.2</td><td>3,713.1</td><td>4,118.2</td></tr><tr><td>Provision for taxes</td><td>(640.2)</td><td>(629.0)</td><td>(704.0)</td><td>(781.0)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>2,470.5</td><td>2,688.2</td><td>3,009.1</td><td>3,337.2</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>693.0</td><td>1,057.5</td><td>1,398.2</td><td>1,585.3</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>9.32</td><td>10.97</td><td>13.48</td><td>16.72</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>9.21</td><td>10.96</td><td>13.45</td><td>16.68</td></tr><tr><td>EPS (ex-ESO exp., dil.) ($)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS ($)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>265.1</td><td>245.0</td><td>223.3</td><td>199.6</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>268.1</td><td>245.4</td><td>223.7</td><td>200.0</td></tr></table>

Balance Sheet (\$ mn) 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>1,501.0</td><td>637.5</td><td>661.8</td><td>2,395.6</td></tr><tr><td>Accounts receivable</td><td>2,332.0</td><td>2,658.0</td><td>2,595.9</td><td>2,841.4</td></tr><tr><td>Inventory</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>4,596.0</td><td>5,055.0</td><td>5,274.8</td><td>4,925.8</td></tr><tr><td>Total current assets</td><td>8,429.0</td><td>8,350.5</td><td>8,532.4</td><td>10,162.8</td></tr><tr><td>Net PP&amp;E</td><td>1,812.0</td><td>1,813.7</td><td>1,805.2</td><td>1,804.2</td></tr><tr><td>Net intangibles</td><td>5,910.0</td><td>5,873.0</td><td>5,873.0</td><td>5,873.0</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>1,923.0</td><td>1,805.3</td><td>1,754.6</td><td>1,704.9</td></tr><tr><td>Total assets</td><td>18,074.0</td><td>17,842.4</td><td>17,965.2</td><td>19,544.9</td></tr><tr><td>Accounts payable</td><td>142.0</td><td>162.4</td><td>181.8</td><td>200.3</td></tr><tr><td>Short-term debt</td><td>-</td><td>998.0</td><td>998.0</td><td>998.0</td></tr><tr><td>Current lease liabilities</td><td>130.0</td><td>131.0</td><td>131.0</td><td>131.0</td></tr><tr><td>Other current liabilities</td><td>6,106.0</td><td>6,957.4</td><td>8,087.3</td><td>9,636.9</td></tr><tr><td>Total current liabilities</td><td>6,378.0</td><td>8,248.8</td><td>9,398.1</td><td>10,966.2</td></tr><tr><td>Long-term debt</td><td>2,987.0</td><td>1,990.0</td><td>990.0</td><td>990.0</td></tr><tr><td>Non-current lease liabilities</td><td>704.0</td><td>686.0</td><td>686.0</td><td>686.0</td></tr><tr><td>Other long-term liabilities</td><td>200.0</td><td>200.6</td><td>213.0</td><td>231.0</td></tr><tr><td>Total long-term liabilities</td><td>3,891.0</td><td>2,876.6</td><td>1,889.0</td><td>1,907.0</td></tr><tr><td>Total liabilities</td><td>10,269.0</td><td>11,125.4</td><td>11,287.2</td><td>12,873.2</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>7,805.0</td><td>6,717.0</td><td>6,678.0</td><td>6,671.7</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total liabilities &amp; equity</td><td>18,074.0</td><td>17,842.4</td><td>17,965.2</td><td>19,544.9</td></tr><tr><td>BVPS ($)</td><td>29.11</td><td>27.37</td><td>29.85</td><td>33.35</td></tr></table>

Cash Flow (\$ mn) 

<table><tr><td></td><td>1/26</td><td>1/27E</td><td>1/28E</td><td>1/29E</td></tr><tr><td>Net income</td><td>693.0</td><td>1,057.5</td><td>1,398.2</td><td>1,585.3</td></tr><tr><td>D&amp;A add-back</td><td>756.0</td><td>647.4</td><td>476.5</td><td>498.6</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(331.0)</td><td>343.7</td><td>1,149.4</td><td>1,265.5</td></tr><tr><td>Others</td><td>1,821.0</td><td>1,346.3</td><td>1,533.0</td><td>1,697.6</td></tr><tr><td>Cash flow from operations</td><td>2,939.0</td><td>3,394.9</td><td>4,557.1</td><td>5,046.9</td></tr><tr><td>Capital expenditures</td><td>(162.0)</td><td>(287.1)</td><td>(316.5)</td><td>(346.2)</td></tr><tr><td>Acquisitions</td><td>(2,720.0)</td><td>(2,413.3)</td><td>(4,016.4)</td><td>(5,046.9)</td></tr><tr><td>Divestitures</td><td>5,276.0</td><td>2,127.0</td><td>4,000.0</td><td>5,600.0</td></tr><tr><td>Others</td><td>(2,061.0)</td><td>50.0</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>333.0</td><td>(523.4)</td><td>(332.8)</td><td>206.9</td></tr><tr><td>Dividends paid</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Share issuance/(repurchase)</td><td>(3,319.0)</td><td>(3,733.0)</td><td>(3,200.0)</td><td>(3,520.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>(1,000.0)</td><td>-</td></tr><tr><td>Others</td><td>5.0</td><td>(2.0)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>(3,319.0)</td><td>(3,733.0)</td><td>(4,200.0)</td><td>(3,520.0)</td></tr><tr><td>Total cash flow</td><td>(42.0)</td><td>(863.5)</td><td>24.3</td><td>1,733.8</td></tr><tr><td>Free cash flow</td><td>2,777.0</td><td>3,107.8</td><td>4,240.6</td><td>4,700.7</td></tr><tr><td>Free cash flow per share (basic) ($)</td><td>10.47</td><td>12.69</td><td>18.99</td><td>23.55</td></tr></table>

Source: Company data, Goldman Sachs Research estimates.

and product/market fit for the headless/ITSM products. We remain Neutral and see the next \~12 months as a transition year for the company.

# EPS Recap

Exhibit 1: 1QFY27 Actuals vs. Estimates 

<table><tr><td rowspan="2">$ millions, unless specified</td><td colspan="5">1Q27A</td></tr><tr><td>Actual</td><td>GSe</td><td>Street</td><td>Actual vs GSe</td><td>Actual vs Street</td></tr><tr><td>Subscription</td><td>$2,354</td><td>$2,335</td><td>$2,335</td><td>0.8%</td><td>0.8%</td></tr><tr><td>%yoy</td><td>14%</td><td>13%</td><td>13%</td><td></td><td></td></tr><tr><td>Professional Services</td><td>$188</td><td>$180</td><td>$180</td><td>4.4%</td><td>4.3%</td></tr><tr><td>%yoy</td><td>4%</td><td>-1%</td><td>0%</td><td></td><td></td></tr><tr><td>Total Revenue</td><td>$2,542</td><td>$2,515</td><td>$2,517</td><td>1.1%</td><td>1.0%</td></tr><tr><td>%yoy</td><td>13%</td><td>12%</td><td>12%</td><td></td><td></td></tr><tr><td>Gross Profit</td><td>$2,028</td><td>$1,993</td><td>$2,005</td><td>1.8%</td><td>1.1%</td></tr><tr><td>% margin</td><td>80%</td><td>79%</td><td>80%</td><td>55bps</td><td>12bps</td></tr><tr><td>% yoy</td><td>13%</td><td>11%</td><td>12%</td><td></td><td></td></tr><tr><td>Operating Income</td><td>$809</td><td>$776</td><td>$769</td><td>$33</td><td>$40</td></tr><tr><td>% margin</td><td>32%</td><td>31%</td><td>31%</td><td>98bps</td><td>129bps</td></tr><tr><td>% yoy</td><td>19%</td><td>15%</td><td>14%</td><td></td><td></td></tr><tr><td>EPS (non GAAP)</td><td>$2.66</td><td>$2.51</td><td>$2.51</td><td>$0.15</td><td>$0.14</td></tr><tr><td>% yoy</td><td>20%</td><td>12%</td><td>13%</td><td></td><td></td></tr><tr><td>Free Cash Flow</td><td>$616</td><td>$300</td><td>$484</td><td>$316</td><td>$132</td></tr><tr><td>% margin</td><td>24%</td><td>12%</td><td>19%</td><td>1231bps</td><td>501bps</td></tr><tr><td>% yoy</td><td>46%</td><td>-29%</td><td>15%</td><td></td><td></td></tr><tr><td>Billings</td><td>$1,856</td><td>$1,758</td><td>$1,819</td><td>5.6%</td><td>2.0%</td></tr><tr><td>%yoy</td><td>18%</td><td>12%</td><td>16%</td><td></td><td></td></tr><tr><td>12-Month Backlog (cRPO)</td><td>$8,806</td><td>$8,733</td><td>$8,774</td><td>0.8%</td><td>0.4%</td></tr><tr><td>%yoy</td><td>15.5%</td><td>15%</td><td>15%</td><td></td><td></td></tr></table>

Source: FactSet, Company data, Goldman Sachs Global Investment Research

# Valuation & Risks

We lower our 12-month price target to \$151 (from \$206), based on 24x our GAAP Q5-Q8 EPS (previously 17.5x non-GAAP EPS). As non-GAAP to GAAP conversion improves, we believe GAAP can now be used as an anchor for valuation (consistent with how we value other large cap peers in our coverage like ADBE/CRM). 24x is 2 turns above the median app software peer in our coverage to reflect faster GAAP EPS growth (3pp above the group) and a higher rule of 40.

We remain Neutral rated. Key risks: Pace of share gain; execution with M&A; AI impact on HCM software.

We adjust our FY2027E/FY2028E/FY2029E revenue estimates on the report to \$10,662/\$11,752mn/\$12,856mn from \$10,644/\$11,722mn/\$12,811mn.

# Disclosure Appendix

# Reg AC

We, Gabriela Borges, CFA, Noah Naparst and Praachi Arora, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in Goldman Sachs' Global Investment Research division.

Contributing Authors: Gabriela Borges, CFA Goldman Sachs & Co. LLC, Noah Naparst Goldman Sachs & Co. LLC, Praachi Arora Goldman Sachs India SPL.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in Goldman Sachs' Global Investment Research division.

# GS Factor Profile

The Goldman Sachs Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the Goldman Sachs analyst forecasts at the fiscal year-end at least three quarters in th

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or Goldman Sachs policy.

The views attributed to third party presenters at Goldman Sachs arranged conferences, including individuals from other parts of Goldman Sachs, do not necessarily reflect those of Global Investment Research and are not an official view of Goldman Sachs.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from Goldman Sachs sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by Goldman Sachs Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is Goldman Sachs responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 Goldman Sachs.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of Goldman Sachs. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of Goldman Sachs. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
