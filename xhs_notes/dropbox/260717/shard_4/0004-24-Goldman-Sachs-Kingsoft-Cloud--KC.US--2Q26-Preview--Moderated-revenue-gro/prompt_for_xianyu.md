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
# Kingsoft Cloud (KC)

# 2Q26 Preview: Moderated revenue growth against a more normalized base; Capex visibility key to 2H26 growth acceleration; Buy

Upside: 69.5%

Kingsoft Cloud (KC) is scheduled to report 2Q26 results in mid-to-late Aug. Share price has fallen -23% since its 1Q26 results reported in late May, as investors are concerned about disconnect between management's optimistic capex outlook and revenue guidance which appeared to be unchanged. We believe such correction may be overdone as management's 30%+ revenue yoy growth outlook in 2026 should be the base case based on the 1Q26 capex run rate, while outlook for Rmb15-20bn capex implies a more bullish case and could support c.35% revenue yoy growth in 2026E based on our estimate.

Into the 2Q26 print, we believe investor focus will be primarily on: 1) AI cloud revenue growth (GSe +62% yoy in 2Q26E vs. +90% yoy in 1Q26) and path to growth re-acceleration into 2H26E (GSe +71% yoy); 2) capex spending visibility considering tighter supply and rising prices of advanced chips/servers; 3) GPM vs. OPM trajectory (GSe 2Q26E non-GAAP GPM 14.3% with narrower yoy decline, yet potentially still dragged by favorable pricing with KAs, and non-GAAP OPM back to positive thanks to OPEX control); 4) progress of MaaS services which provide higher profitability vs. GPUaaS. For 2Q26E, we model revenue +27% yoy to Rmb3.0bn (2% below Visible Alpha Consensus Data) led by +37% yoy public cloud revenue growth (moderating from +47% yoy in 1Q26 against a more normalized base as 1Q25 public cloud revenue only grew +14% yoy), Rmb909mn adj. EBITDA (largely in line with consensus) and Rmb13mn adj. operating profit.

We keep our 2026E-28E revenue and adj. EBITDA forecasts largely unchanged, yet revise up 2026E-28E adj. operating profit by 85%/6%/4% to account for better OPEX efficiency. That said, we modify our DCF-based 12m TP to US\$17 (vs. US\$19.5 prior) based on a 10.3% WACC and 3% terminal growth (unchanged), as we factor in higher capex needed in the longer term to support the revenue growth given the rising chip/server prices.

## BUY

Timothy Zhao
+852-2978-2673 | timothy.zhao@gs.com
GS (Asia) L.L.C.

Ronald Keung, CFA
+852-2978-0856 | ronald.keung@gs.com
GS (Asia) L.L.C.

Eunice Liu
+852-2978-7472 | eunice.liu@gs.com
GS (Asia) L.L.C.

## Key Data

<table><tr><td>Market cap: $3.0bn</td></tr><tr><td>Enterprise value: $3.9bn</td></tr><tr><td>3m ADTV: $19.3mn</td></tr><tr><td>China</td></tr><tr><td>China Internet Verticals</td></tr><tr><td>M&amp;A Rank: 3</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td></tr></table>

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn) New</td><td>9,558.6</td><td>12,506.6</td><td>15,702.2</td><td>19,040.0</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>9,558.6</td><td>12,506.7</td><td>15,707.7</td><td>19,050.9</td></tr><tr><td>EBITDA (Rmb mn)</td><td>2,328.1</td><td>3,982.8</td><td>5,685.4</td><td>7,478.0</td></tr><tr><td>EPS (Rmb) New</td><td>(2.67)</td><td>(2.03)</td><td>(1.24)</td><td>(0.52)</td></tr><tr><td>EPS (Rmb) Old</td><td>(2.67)</td><td>(2.14)</td><td>(1.30)</td><td>(0.60)</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>P/B (X)</td><td>2.9</td><td>2.4</td><td>2.5</td><td>2.6</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CROCI (%)</td><td>14.0</td><td>14.6</td><td>16.3</td><td>16.9</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>(0.78)</td><td>(0.52)</td><td>(0.47)</td><td>(0.26)</td></tr></table>

GS Factor Profile

![](images/463415c32165b050cae09cfcbae77b2403d652d18e94f306ec51a9c2e00157e6.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Kingsoft Cloud (KC)

Rating since Feb 11, 2026

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>P/B (X)</td><td>2.9</td><td>2.4</td><td>2.5</td><td>2.6</td></tr><tr><td>FCF yield (%)</td><td>(3.5)</td><td>(6.3)</td><td>(10.1)</td><td>(5.4)</td></tr><tr><td>EV/EBITDAR (X)</td><td>13.7</td><td>6.9</td><td>5.5</td><td>4.5</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>13.7</td><td>6.9</td><td>5.5</td><td>4.5</td></tr><tr><td>CROCI (%)</td><td>14.0</td><td>14.6</td><td>16.3</td><td>16.9</td></tr><tr><td>ROE (%)</td><td>(10.1)</td><td>(6.9)</td><td>(4.5)</td><td>(2.0)</td></tr><tr><td>Net debt/equity (%)</td><td>30.1</td><td>64.3</td><td>111.0</td><td>145.9</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>29.1</td><td>63.3</td><td>109.9</td><td>144.8</td></tr><tr><td>Interest cover (X)</td><td>(0.3)</td><td>0.1</td><td>0.6</td><td>1.0</td></tr><tr><td>Days inventory outst, sales</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Receivable days</td><td>61.3</td><td>55.3</td><td>51.3</td><td>50.3</td></tr><tr><td>Days payable outstanding</td><td>88.6</td><td>85.2</td><td>85.2</td><td>81.1</td></tr><tr><td>DuPont ROE (%)</td><td>(7.9)</td><td>(7.2)</td><td>(4.6)</td><td>(2.0)</td></tr><tr><td>Turnover (X)</td><td>0.4</td><td>0.4</td><td>0.5</td><td>0.5</td></tr><tr><td>Leverage (X)</td><td>2.9</td><td>3.5</td><td>4.1</td><td>4.8</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>22,049.1</td><td>29,450.3</td><td>38,384.9</td><td>48,027.1</td></tr><tr><td>Average capital employed (Rmb)</td><td>8,114.6</td><td>9,887.8</td><td>11,072.9</td><td>12,433.4</td></tr><tr><td>BVPS (Rmb)</td><td>34.05</td><td>28.28</td><td>26.76</td><td>25.98</td></tr></table>

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>9,558.6</td><td>12,506.6</td><td>15,702.2</td><td>19,040.0</td></tr><tr><td>Cost of goods sold</td><td>(8,016.9)</td><td>(10,695.8)</td><td>(13,428.7)</td><td>(16,238.7)</td></tr><tr><td>SG&amp;A</td><td>(1,114.8)</td><td>(1,135.3)</td><td>(1,221.9)</td><td>(1,320.8)</td></tr><tr><td>R&amp;D</td><td>(752.9)</td><td>(774.5)</td><td>(843.1)</td><td>(933.6)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>2,162.0</td><td>3,802.1</td><td>5,511.6</td><td>7,304.3</td></tr><tr><td>Depreciation &amp; amortization</td><td>(2,480.4)</td><td>(3,908.1)</td><td>(5,303.2)</td><td>(6,757.4)</td></tr><tr><td>EBIT</td><td>(152.2)</td><td>74.7</td><td>382.2</td><td>720.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>(417.2)</td><td>(509.2)</td><td>(590.9)</td><td>(709.3)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>(735.6)</td><td>(615.2)</td><td>(382.5)</td><td>(162.4)</td></tr><tr><td>Provision for taxes</td><td>4.2</td><td>(5.1)</td><td>0.0</td><td>0.0</td></tr><tr><td>Minority interest</td><td>-</td><td>(0.1)</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>(731.4)</td><td>(620.3)</td><td>(382.5)</td><td>(162.4)</td></tr><tr><td>Post-tax exceptionals</td><td>(204.9)</td><td>(296.8)</td><td>(306.3)</td><td>(363.3)</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>(936.3)</td><td>(917.1)</td><td>(688.8)</td><td>(525.6)</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>(2.67)</td><td>(2.03)</td><td>(1.24)</td><td>(0.52)</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>(2.67)</td><td>(2.03)</td><td>(1.24)</td><td>(0.52)</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>(3.42)</td><td>(3.00)</td><td>(2.23)</td><td>(1.68)</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>(3.42)</td><td>(3.00)</td><td>(2.23)</td><td>(1.68)</td></tr><tr><td>DPS (Rmb)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>22.8</td><td>30.8</td><td>25.6</td><td>21.3</td></tr><tr><td>EBITDA growth</td><td>179.9</td><td>71.1</td><td>42.7</td><td>31.5</td></tr><tr><td>EPS growth</td><td>21.0</td><td>24.1</td><td>38.9</td><td>58.0</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EBIT margin</td><td>(1.6)</td><td>0.6</td><td>2.4</td><td>3.8</td></tr><tr><td>EBITDA margin</td><td>24.4</td><td>31.8</td><td>36.2</td><td>39.3</td></tr><tr><td>Net income margin</td><td>(7.7)</td><td>(5.0)</td><td>(2.4)</td><td>(0.9)</td></tr></table>

Price Performance  
![](images/95ea77108c41342c250039d8e0026b1c05a77c0e75fbd738cea646885b76bdfb.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(40.6)%</td><td>(18.9)%</td><td>(33.5)%</td></tr><tr><td>Rel. to the NASDAQ Composite</td><td>(45.7)%</td><td>(27.3)%</td><td>(47.7)%</td></tr></table>

Source: FactSet. Price as of 15 Jul 2026 close.

<table><tr><td colspan="5">Balance Sheet (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>6,117.2</td><td>4,812.5</td><td>4,200.2</td><td>5,046.8</td></tr><tr><td>Accounts receivable</td><td>1,740.5</td><td>2,047.2</td><td>2,364.1</td><td>2,880.6</td></tr><tr><td>Inventory</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>3,165.7</td><td>3,795.6</td><td>4,416.7</td><td>5,000.6</td></tr><tr><td>Total current assets</td><td>11,023.4</td><td>10,655.3</td><td>10,981.0</td><td>12,928.0</td></tr><tr><td>Net PP&amp;E</td><td>10,193.3</td><td>14,404.7</td><td>18,011.1</td><td>21,006.8</td></tr><tr><td>Net intangibles</td><td>5,138.5</td><td>5,018.9</td><td>4,909.3</td><td>4,836.2</td></tr><tr><td>Total investments</td><td>234.2</td><td>234.2</td><td>234.2</td><td>234.2</td></tr><tr><td>Other long-term assets</td><td>139.8</td><td>139.8</td><td>139.8</td><td>139.8</td></tr><tr><td>Total assets</td><td>26,729.2</td><td>30,453.0</td><td>34,275.4</td><td>39,145.0</td></tr><tr><td>Accounts payable</td><td>2,014.5</td><td>2,977.7</td><td>3,287.8</td><td>3,930.5</td></tr><tr><td>Short-term debt</td><td>3,348.3</td><td>3,348.3</td><td>3,348.3</td><td>3,848.3</td></tr><tr><td>Short-term lease liabilities</td><td>40.9</td><td>40.9</td><td>40.9</td><td>40.9</td></tr><tr><td>Other current liabilities</td><td>4,017.7</td><td>4,589.9</td><td>5,083.0</td><td>5,578.5</td></tr><tr><td>Total current liabilities</td><td>9,421.3</td><td>10,956.8</td><td>11,760.1</td><td>13,398.3</td></tr><tr><td>Long-term debt</td><td>3,023.5</td><td>3,023.5</td><td>4,523.5</td><td>6,023.5</td></tr><tr><td>Long-term lease liabilities</td><td>51.1</td><td>51.1</td><td>51.1</td><td>51.1</td></tr><tr><td>Other long-term liabilities</td><td>4,920.1</td><td>7,772.8</td><td>9,674.4</td><td>11,568.2</td></tr><tr><td>Total long-term liabilities</td><td>7,994.8</td><td>10,847.5</td><td>14,249.1</td><td>17,642.9</td></tr><tr><td>Total liabilities</td><td>17,416.2</td><td>21,804.3</td><td>26,009.2</td><td>31,041.2</td></tr><tr><td>Preferred shares</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>9,317.0</td><td>8,652.6</td><td>8,270.1</td><td>8,107.7</td></tr><tr><td>Minority interest</td><td>(4.0)</td><td>(3.9)</td><td>(3.9)</td><td>(3.9)</td></tr><tr><td>Total liabilities &amp; equity</td><td>26,729.2</td><td>30,453.0</td><td>34,275.4</td><td>39,145.0</td></tr><tr><td>Net debt, adjusted</td><td>2,714.6</td><td>5,472.0</td><td>9,086.0</td><td>11,733.2</td></tr></table>

Cash Flow (Rmb mn)

<table><tr><td colspan="5">Cash flow (Kmb mln)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>(943.7)</td><td>(917.0)</td><td>(688.8)</td><td>(525.6)</td></tr><tr><td>D&amp;A add-back</td><td>2,480.4</td><td>3,908.1</td><td>5,303.2</td><td>6,757.4</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>1,760.7</td><td>3,451.5</td><td>1,767.0</td><td>1,931.6</td></tr><tr><td>Other operating cash flow</td><td>503.6</td><td>252.7</td><td>306.3</td><td>363.3</td></tr><tr><td>Cash flow from operations</td><td>3,801.0</td><td>6,695.3</td><td>6,687.7</td><td>8,526.6</td></tr><tr><td>Capital expenditures</td><td>(4,742.4)</td><td>(8,000.0)</td><td>(8,800.0)</td><td>(9,680.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>212.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(4,529.7)</td><td>(8,000.0)</td><td>(8,800.0)</td><td>(9,680.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>1,357.3</td><td>0.0</td><td>1,500.0</td><td>2,000.0</td></tr><tr><td>Other financing cash flows</td><td>2,758.5</td><td>0.1</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>4,115.8</td><td>0.1</td><td>1,500.0</td><td>2,000.0</td></tr><tr><td>Total cash flow</td><td>3,387.1</td><td>(1,304.6)</td><td>(612.3)</td><td>846.6</td></tr><tr><td>Free cash flow</td><td>(941.3)</td><td>(1,304.7)</td><td>(2,112.3)</td><td>(1,153.4)</td></tr></table>

Source: Company data, GS estimates.

Maintain Buy as we see its current valuation as attractive; KC is trading at 1.5x 2026E P/S which is at 2x standard deviation below its historical average level of 2.5x since 2025. Key catalysts: Xiaomi's new model launches (e.g. MiMo, Xiaomi-Robotics embodied foundation model; also see Setting the scene for a catalyst-rich 3Q; Sharpening the scene ahead of SkyNomad launch and continued AI progress); enhanced chip availability; domestic chip breakthrough.

Exhibit 1: We model KC's revenue growth at $27\%$ yoy in 2Q26E moderating from $37\%$ yoy in 1Q26 due to chip constraints  
![](images/546dd1a33eee020c974c0a932cc21614d42b71ace1b86a9f53638234e858cf4e.jpg)

![](images/6316fb0537091d4edfb835c55de864dc00def52c137da71ec4d8aead64503468.jpg)

![](images/18d69256e9f71aceaa96c1be9dac2b95f4d913d648d674a31a7d7e3b8d38406f.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: We expect AI related revenue contribution to increase to 40%+ in 2026E vs. 31% in 2025  
![](images/7bb0d93b717af234a88555a60e64fe68039c682f73dac1b0fa38b0b439794080.jpg)

![](images/1d4b281deb27a44e1f6123ddf370d03a54b40ec9b845924aebd59b0d1a88eb69.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 3: We expect Xiaomi and Kingsoft combined to account for $40\%$ of KC's revenue by 2028E vs. $27\%$ in 2025...  
![](images/aafa70481f9977598d4f35ef1c828bec434494ce601a4947459cba98cd5d17fb.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: ... with revenue from Xiaomi/Kingsoft combined growing at a 43% CAGR in 2025-28E vs. an 18% CAGR for revenue from other customers
yoy revenue growth by customer  
![](images/b9be687955a3b798e3f1a8a80595bdcaad8900f07452f87973db5be06c6f2c2d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: Our quarterly forecasts on GPM, EBITDA margin and operating margin  
![](images/db5535205f7ffbf959c49b99248eb3b4af6a87a1c490559adeef6821fbf0a868.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 6: Our annual forecasts on GPM, EBITDA margin and operating margin  
![](images/45d0f3bb131b7edac0efed6fb98fdaea1262c626a6cc6549aceba093af2b47d2.jpg)  
Source: Company data, GS Global Inve

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
