你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# Guming Holdings Ltd. (1364.HK)

# 1H26 preview: factoring in slower store additions, yet resilient margins; Buy (on CL)

1364.HK 12m Price Target: HK\$31.00 Price: HK\$22.14 Upside: 40.0%

Guming is expected to release its 1H26 results in late Aug. We forecast a $30\% / 43\%$ yoy sales/adj. core NP growth, to Rmb7,372mn/1,630mn in 1H26. Compared to our prior forecast, we lower 2026-28E adj. core NP by $6\% - 13\%$ , reflecting a slower (yet still decent at $18\%$ 2025-28E CAGR) topline growth with lowered store addition forecast (from 3,600 to 2,000 in 2026E), faster-than-expected delivery subsidy normalization, and higher expenses including financing costs from a convertible bond, and a slightly higher effective tax rate going forward.

That said, with share price pulled back by 19% since 2Q26 and the stock currently trading at 13X 2026E P/E vs. 17% adj. core NP yoy growth we expect for 2026E, we view the slower store opening outlook and near-term negative SSSG have been reflected by the market, and we note that: 1) while near-term store opening has been impacted by franchisees' willingness (last year the company opened many stores, and SSSG declined as subsidies faded) and company's priority on store quality, we view that Guming continues to see meaningful room for store expansion, with store network remaining much smaller than Mixue/Luckin; 2) Category expansion, differentiated new products, and the company's focus on store quality would support a resilient SSSG despite last year's high base (we expect -2% per store GMV yoy in 2026E); 3) earnings growth in 2026E will be supported by last year's fast store network expansion, and margin remains solid with continuous operating leverage/efficiency gain. With new TP of HK\$31 (based on 20X 2026E P/E, lowered from 23X prior given the weak sentiment in consumer sectors, SSSG turning to decline with base effects, and lowered earnings outlook) implying 40% upside, we remain Buy rated on Guming (on CL).

Into results, we expect investors to focus on: 1) Recent SSSG performance and 2H26 outlook; 2) progress of category expansion, including coffee sales mix and breakfast, as well as other initiatives

Michelle Cheng
+852-2978-6631 | michelle.cheng@gs.com
GS (Asia) L.L.C.

Xinyu Ruan
+852-2978-7347 | xinyu.ruan@gs.com
GS (Asia) L.L.C.

Molly Dai
+852-3966-4000 | molly.dai@gs.com
GS (Asia) L.L.C.

## Key Data

Market cap: HK\$52.7bn / \$6.7bn
Enterprise value: HK\$43.8bn / \$5.6bn
3m ADTV: HK\$113.6mn / \$14.5mn
China
Greater China Retail
M&A Rank: 3
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn) New</td><td>12,913.8</td><td>15,252.0</td><td>18,050.9</td><td>21,006.8</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>12,913.8</td><td>16,608.8</td><td>19,944.1</td><td>23,260.8</td></tr><tr><td>EBITDA (Rmb mn)</td><td>3,440.6</td><td>4,117.4</td><td>4,863.6</td><td>5,560.5</td></tr><tr><td>EPS (Rmb) New</td><td>1.21</td><td>1.37</td><td>1.58</td><td>1.81</td></tr><tr><td>EPS (Rmb) Old</td><td>1.21</td><td>1.45</td><td>1.76</td><td>2.07</td></tr><tr><td>P/E (X)</td><td>16.7</td><td>13.9</td><td>12.1</td><td>10.6</td></tr><tr><td>P/B (X)</td><td>8.2</td><td>5.8</td><td>4.5</td><td>3.6</td></tr><tr><td>Dividend yield (%)</td><td>10.3</td><td>3.1</td><td>3.7</td><td>5.1</td></tr><tr><td>CROCI (%)</td><td>NM</td><td>224.0</td><td>121.9</td><td>118.4</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.49</td><td>0.72</td><td>0.69</td><td>0.69</td></tr></table>

GS Factor Profile

![](images/84eaf6dd4c6bb4b583e18f7ef6d1114f6906413366794895df141fb6ce0124d4.jpg)  
Source: Company data, GS estimates. See disclosures for details.

![](images/57ce875fe7a129fcb3645b1e76ca806f42bb8c9f268c25d2ad875c8b157a490c.jpg)

## Guming Holdings Ltd. (1364.HK)

Rating since Mar 23, 2025

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>16.7</td><td>13.9</td><td>12.1</td><td>10.6</td></tr><tr><td>P/B (X)</td><td>8.2</td><td>5.8</td><td>4.5</td><td>3.6</td></tr><tr><td>FCF yield (%)</td><td>4.5</td><td>6.1</td><td>7.2</td><td>9.2</td></tr><tr><td>EV/EBITDAR (X)</td><td>11.6</td><td>10.0</td><td>8.4</td><td>6.8</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>11.8</td><td>10.1</td><td>8.5</td><td>6.8</td></tr><tr><td>CROCI (%)</td><td>NM</td><td>224.0</td><td>121.9</td><td>118.4</td></tr><tr><td>ROE (%)</td><td>78.8</td><td>45.7</td><td>41.1</td><td>37.5</td></tr><tr><td>Net debt/equity (%)</td><td>(103.4)</td><td>(97.5)</td><td>(71.2)</td><td>(76.4)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(104.4)</td><td>(98.2)</td><td>(71.8)</td><td>(76.9)</td></tr><tr><td>Interest cover (X)</td><td>44.2</td><td>30.9</td><td>46.4</td><td>1,428.7</td></tr><tr><td>Days inventory outst, sales</td><td>32.3</td><td>32.2</td><td>32.2</td><td>32.2</td></tr><tr><td>Receivable days</td><td>12.4</td><td>13.3</td><td>13.4</td><td>14.7</td></tr><tr><td>Days payable outstanding</td><td>35.6</td><td>36.6</td><td>37.6</td><td>38.6</td></tr><tr><td>DuPont ROE (%)</td><td>53.2</td><td>39.8</td><td>36.5</td><td>33.7</td></tr><tr><td>Turnover (X)</td><td>0.8</td><td>1.0</td><td>1.1</td><td>1.3</td></tr><tr><td>Leverage (X)</td><td>2.8</td><td>2.0</td><td>1.6</td><td>1.3</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>123.2</td><td>2,935.9</td><td>3,669.1</td><td>3,985.5</td></tr><tr><td>Average capital employed (Rmb)</td><td>(873.7)</td><td>(59.3)</td><td>1,478.6</td><td>2,850.1</td></tr><tr><td>BVPS (Rmb)</td><td>2.46</td><td>3.28</td><td>4.21</td><td>5.25</td></tr></table>

Growth & Margins (%)

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>12,913.8</td><td>15,252.0</td><td>18,050.9</td><td>21,006.8</td></tr><tr><td>Cost of goods sold</td><td>(8,651.6)</td><td>(10,185.6)</td><td>(12,059.7)</td><td>(14,043.1)</td></tr><tr><td>SG&amp;A</td><td>(1,067.8)</td><td>(1,238.3)</td><td>(1,435.8)</td><td>(1,643.6)</td></tr><tr><td>R&amp;D</td><td>(223.4)</td><td>(274.5)</td><td>(315.9)</td><td>(357.1)</td></tr><tr><td>Other operating inc./(exp.)</td><td>304.9</td><td>375.3</td><td>413.9</td><td>366.8</td></tr><tr><td>EBITDA</td><td>3,440.6</td><td>4,117.4</td><td>4,863.6</td><td>5,560.5</td></tr><tr><td>Depreciation &amp; amortization</td><td>(164.7)</td><td>(188.6)</td><td>(210.1)</td><td>(230.8)</td></tr><tr><td>EBIT</td><td>3,275.9</td><td>3,928.9</td><td>4,653.5</td><td>5,329.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>(74.1)</td><td>(127.1)</td><td>(100.3)</td><td>(3.7)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>3,758.6</td><td>3,801.8</td><td>4,553.1</td><td>5,326.0</td></tr><tr><td>Provision for taxes</td><td>(643.1)</td><td>(688.3)</td><td>(896.8)</td><td>(1,111.9)</td></tr><tr><td>Minority interest</td><td>(6.4)</td><td>(7.6)</td><td>(9.1)</td><td>(10.4)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>3,109.1</td><td>3,105.8</td><td>3,647.3</td><td>4,203.7</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>3,109.1</td><td>3,105.8</td><td>3,647.3</td><td>4,203.7</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>1.34</td><td>1.31</td><td>1.53</td><td>1.77</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>1.32</td><td>1.31</td><td>1.53</td><td>1.77</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>1.34</td><td>1.31</td><td>1.53</td><td>1.77</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>1.32</td><td>1.31</td><td>1.53</td><td>1.77</td></tr><tr><td>DPS (Rmb)</td><td>2.09</td><td>0.59</td><td>0.70</td><td>0.97</td></tr><tr><td>Div. payout ratio (%)</td><td>155.7</td><td>45.2</td><td>45.7</td><td>54.8</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>46.9</td><td>18.1</td><td>18.4</td><td>16.4</td></tr><tr><td>EBITDA growth</td><td>74.3</td><td>19.7</td><td>18.1</td><td>14.3</td></tr><tr><td>EPS growth</td><td>61.5</td><td>13.7</td><td>14.7</td><td>14.8</td></tr><tr><td>DPS growth</td><td>NM</td><td>(71.7)</td><td>18.7</td><td>38.0</td></tr><tr><td>EBIT margin</td><td>25.4</td><td>25.8</td><td>25.8</td><td>25.4</td></tr><tr><td>EBITDA margin</td><td>26.6</td><td>27.0</td><td>26.9</td><td>26.5</td></tr><tr><td>Net income margin</td><td>24.1</td><td>20.4</td><td>20.2</td><td>20.0</td></tr></table>

Price Performance  
![](images/0fa230ab8eccb77dbba3ba46bb1ec0c44f382dc861ba8fef06b77b23d3d6646f.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(12.1)%</td><td>(22.0)%</td><td>(4.6)%</td></tr><tr><td>Rel. to the Hang Seng Index</td><td>(10.9)%</td><td>(14.3)%</td><td>(3.6)%</td></tr></table>

Source: FactSet. Price as of 28 Jul 2026 close.

Balance Sheet (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>12,561.6</td><td>10,970.9</td><td>10,483.2</td><td>9,736.1</td></tr><tr><td>Accounts receivable</td><td>588.0</td><td>522.2</td><td>799.3</td><td>897.5</td></tr><tr><td>Inventory</td><td>1,300.0</td><td>1,389.3</td><td>1,794.8</td><td>1,913.0</td></tr><tr><td>Other current assets</td><td>524.3</td><td>525.4</td><td>712.9</td><td>734.8</td></tr><tr><td>Total current assets</td><td>14,973.9</td><td>13,407.8</td><td>13,790.2</td><td>13,281.4</td></tr><tr><td>Net PP&amp;E</td><td>1,172.4</td><td>1,648.6</td><td>1,820.6</td><td>2,000.8</td></tr><tr><td>Net intangibles</td><td>0.6</td><td>0.3</td><td>0.1</td><td>0.0</td></tr><tr><td>Total investments</td><td>240.8</td><td>240.8</td><td>240.8</td><td>240.8</td></tr><tr><td>Other long-term assets</td><td>262.7</td><td>328.5</td><td>228.5</td><td>228.5</td></tr><tr><td>Total assets</td><td>16,650.3</td><td>15,625.9</td><td>16,080.2</td><td>15,751.5</td></tr><tr><td>Accounts payable</td><td>992.1</td><td>1,053.4</td><td>1,434.5</td><td>1,539.5</td></tr><tr><td>Short-term debt</td><td>6,322.4</td><td>3,161.2</td><td>3,161.2</td><td>0.0</td></tr><tr><td>Short-term lease liabilities</td><td>28.7</td><td>28.7</td><td>28.7</td><td>28.7</td></tr><tr><td>Other current liabilities</td><td>3,168.8</td><td>983.5</td><td>1,121.0</td><td>1,348.7</td></tr><tr><td>Total current liabilities</td><td>10,512.0</td><td>7,503.2</td><td>5,745.4</td><td>2,916.8</td></tr><tr><td>Long-term debt</td><td>139.3</td><td>139.3</td><td>139.3</td><td>139.3</td></tr><tr><td>Long-term lease liabilities</td><td>29.0</td><td>29.0</td><td>29.0</td><td>29.0</td></tr><tr><td>Other long-term liabilities</td><td>127.8</td><td>145.0</td><td>165.7</td><td>187.5</td></tr><tr><td>Total long-term liabilities</td><td>296.1</td><td>313.4</td><td>334.0</td><td>355.8</td></tr><tr><td>Total liabilities</td><td>10,808.1</td><td>7,816.6</td><td>6,079.4</td><td>3,272.7</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>5,823.8</td><td>7,783.3</td><td>9,965.7</td><td>12,433.4</td></tr><tr><td>Minority interest</td><td>18.4</td><td>26.1</td><td>35.1</td><td>45.5</td></tr><tr><td>Total liabilities &amp; equity</td><td>16,650.3</td><td>15,625.9</td><td>16,080.2</td><td>15,751.5</td></tr><tr><td>Net debt, adjusted</td><td>(6,099.8)</td><td>(7,670.3)</td><td>(7,182.7)</td><td>(9,596.8)</td></tr></table>

Cash Flow (Rmb mn)

<table><tr><td colspan="5">Cash flow (Kmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>3,109.1</td><td>3,105.8</td><td>3,647.3</td><td>4,203.7</td></tr><tr><td>D&amp;A add-back</td><td>164.7</td><td>188.6</td><td>210.1</td><td>230.8</td></tr><tr><td>Minority interest add-back</td><td>6.4</td><td>7.6</td><td>9.1</td><td>10.4</td></tr><tr><td>Net (inc)/dec working capital</td><td>(392.3)</td><td>72.2</td><td>(310.0)</td><td>34.1</td></tr><tr><td>Other operating cash flow</td><td>(640.7)</td><td>20.6</td><td>79.2</td><td>82.1</td></tr><tr><td>Cash flow from operations</td><td>2,408.6</td><td>3,394.8</td><td>3,635.7</td><td>4,561.0</td></tr><tr><td>Capital expenditures</td><td>(248.3)</td><td>(591.6)</td><td>(295.8)</td><td>(310.6)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(106.7)</td><td>(72.8)</td><td>(86.2)</td><td>(100.3)</td></tr><tr><td>Cash flow from investing</td><td>(355.1)</td><td>(664.4)</td><td>(382.0)</td><td>(410.9)</td></tr><tr><td>Repayment of lease liabilities</td><td>(58.1)</td><td>(53.2)</td><td>(57.5)</td><td>(65.3)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(1,493.2)</td><td>(3,380.8)</td><td>(1,405.0)</td><td>(1,668.3)</td></tr><tr><td>Inc/(dec) in debt</td><td>6,312.9</td><td>(884.7)</td><td>(2,276.5)</td><td>(3,161.2)</td></tr><tr><td>Other financing cash flows</td><td>8,463.8</td><td>(3,203.5)</td><td>(2.3)</td><td>(3,163.5)</td></tr><tr><td>Cash flow from financing</td><td>6,785.0</td><td>(4,321.1)</td><td>(3,741.4)</td><td>(4,897.2)</td></tr><tr><td>Total cash flow</td><td>8,838.6</td><td>(1,590.7)</td><td>(487.7)</td><td>(747.1)</td></tr><tr><td>Free cash flow</td><td>2,102.2</td><td>2,750.0</td><td>3,282.4</td><td>4,185.1</td></tr></table>

Source: Company data, GS estimates.

that can support SSSG; 3) thoughts on store network expansion pace and strategy; 4) competitive landscape update and thoughts on pricing/promotion; 5) plan on shareholder returns and further buyback plans.

Relevant reports:

Guming Holdings Ltd. (1364.HK): NDR takeaways: Store quality a priority; store network upgrade/category expansion/marketing to support SSSG; Buy (on CL)

Guming Holdings Ltd. (1364.HK): Announced offering of HK\$ 1.96bn CB with concurrent share repurchase; Buy (on CL)

## 1H26 preview

Sales: We look for 31% topline growth in 1H26, 1) we look for 3.4% per store GMV growth, and we expect per store goods sales growth at a similar level, with higher delivery mix yoy being offset by an improving GMV/actual sales rate in the delivery channel; 2) we expect to see yoy decline in sales of equipment given last year's high base when coffee machines were being rolled out, and slower new store additions this year; 3) average store count increase is at 32% yoy in 1H26, driven by the strong store openings last year, while we expect to see 780 net store additions in 1H26.

Margin: We look for 33% GPM in 1H26, at a similar level to 2025's full-year level, and implying 1.6pp yoy expansion. With operating leverage at the company level, we also expect to see yoy SG&A cost ratio decline; that said, this will be partially offset by higher FX loss yoy. Net-net, we expect OPM yoy expansion of 1.9pp in 1H26 (or 3pp yoy expansion if using GPM-SG&A ratio).

Net profit: Reflecting the sales and margin assumptions above and factoring in withholding tax of Rmb80mn/an FX loss of Rmb80mn, we expect 1H26 reported NP at Rmb1,470mn. We expect adj. core net profit (excl. withholding tax and FX loss impact) at Rmb1,630mn, implying 43% yoy growth.

Exhibit 1: Guming 1H26 preview

<table><tr><td>1H26E</td><td>GSe</td><td>Growth yoy</td><td>Margin</td><td>Margin yoy</td></tr><tr><td>Sales</td><td>7,372</td><td>30.2%</td><td></td><td></td></tr><tr><td>Per store GMV</td><td>1.42</td><td>3.4%</td><td></td><td></td></tr><tr><td>Average store #</td><td>13,944</td><td>32.2%</td><td></td><td></td></tr><tr><td>Period end store #</td><td>14,334</td><td

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
