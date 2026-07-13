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
# Porsche AG (P911\_p.DE)

# Expect a strong 2Q26 as cost momentum accelerates and 911 mix offsets lower FY27 volumes; Reiterate Buy

P911\_p.DE

12m Price Target: €57.00

Price: €45.13

Upside: $26.3\%$

Expect strong 2Q26 with story in-line with our recent Buy thesis: We expect the company to report an EBIT of €785mn (vs €586mn VA cons), implying an 8.5% margin (VA cons 6.6%). We estimate a €50mn net positive effect from the net effect of a provision reversal and additional restructuring costs, lifting the margin above the 5.5-7.5% FY corridor. On an underlying basis we expect the quarter to benefit from an improving 911 mix in-line with our Buy thesis.

Cost momentum building post our upgrade: Since our 11 June upgrade, company messaging and press reports point to accelerating cost momentum, with a second personnel package close to finalisation likely equal to or larger than the first (c.3.9k of 41.8k employees) with the resulting restructuring costs likely fully offset by the provision unwind. Market discussion of a relocation of Cayenne production from Bratislava to Porsche-owned Leipzig or Zuffenhausen suggests a further signal of streamlining ahead of the 7 October CMD.

911 ASP likely even higher, offsetting further volume declines: We cut FY27 volumes yoy to -11% (vs -2% previously), with FY26 unchanged at -10%, as we see China weakness and the ICE Macan production stop hitting volumes, yet we see 911 strength as a continuously underappreciated offset. We now factor a pricing lift alongside mix for FY27, raising FY27 911 ASP growth to +8% (vs c.5% previously), plus c.1k units of the widely discussed 911 GT2 RS at a GSe ASP of €475k.

Revise near-term volume expectations down albeit largely offset by mix: We revise our EPS estimates for Porsche AG by +2.4%/-2.2%/-2.9% for FY26/27/28, factoring our latest views on volumes, cost initiatives and higher 911 ASP mix helped by the GT2. We use our FY27/28 blended EPS estimate of €2.87 on a P/E multiple of 20x to derive our 12-month price target of €57 (prev. €59). We reiterate Buy.

Christian Frenes  
+44(20)7051-8641 | christian.frenes@gs.com  
GS International

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com  
GS International

Monika Mengting Liu, CFA +44(20)7051-7601 | monika.liu@gs.com GS International

## Key Data

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (€ mn) New</td><td>36,272.0</td><td>36,038.7</td><td>35,677.8</td><td>37,601.6</td></tr><tr><td>Revenue (€ mn) Old</td><td>36,272.0</td><td>36,038.7</td><td>37,115.6</td><td>38,862.1</td></tr><tr><td>EBIT (€ mn)</td><td>413.0</td><td>2,284.4</td><td>3,034.9</td><td>4,036.0</td></tr><tr><td>EPS (€) New</td><td>0.47</td><td>1.84</td><td>2.46</td><td>3.27</td></tr><tr><td>EPS (€) Old</td><td>0.47</td><td>1.79</td><td>2.52</td><td>3.37</td></tr><tr><td>P/E (X)</td><td>100.2</td><td>24.5</td><td>18.3</td><td>13.8</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>2.7</td><td>2.9</td><td>3.3</td></tr><tr><td>CROCI (%)</td><td>10.3</td><td>8.7</td><td>9.9</td><td>10.4</td></tr><tr><td>Net debt/EBITDA (X)</td><td>1.1</td><td>0.9</td><td>0.7</td><td>0.4</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (€)</td><td>0.44</td><td>0.64</td><td>0.28</td><td>0.96</td></tr></table>

GS Factor Profile

![](images/f901f06123b61b82ac3122bfc938182ad841534deb5c256879c5ea6efc2c3a4e.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Porsche AG (P911\_p.DE)

BUY

Rating since Jun 11, 2026

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>EV/sales (X)</td><td>1.4</td><td>1.3</td><td>1.3</td><td>1.2</td></tr><tr><td>EV/EBITDAR (X)</td><td>8.5</td><td>7.3</td><td>6.4</td><td>5.4</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>8.5</td><td>7.3</td><td>6.4</td><td>5.4</td></tr><tr><td>EV/EBIT (X)</td><td>120.4</td><td>20.8</td><td>15.4</td><td>11.2</td></tr><tr><td>P/E (X)</td><td>100.2</td><td>24.5</td><td>18.3</td><td>13.8</td></tr><tr><td>FCF yield (%)</td><td>0.8</td><td>1.5</td><td>4.9</td><td>6.9</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>2.7</td><td>2.9</td><td>3.3</td></tr><tr><td>EV/GCI (X)</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.7</td></tr><tr><td>CROCI (%)</td><td>10.3</td><td>8.7</td><td>9.9</td><td>10.4</td></tr><tr><td>ROIC (%)</td><td>1.0</td><td>5.3</td><td>7.1</td><td>9.6</td></tr><tr><td>ROA (%)</td><td>0.5</td><td>2.9</td><td>3.8</td><td>4.9</td></tr><tr><td>Days inventory outst, sales</td><td>61.1</td><td>60.1</td><td>59.6</td><td>57.8</td></tr><tr><td>Asset turnover (X)</td><td>2.3</td><td>2.2</td><td>2.1</td><td>2.2</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>28.6</td><td>24.2</td><td>19.6</td><td>12.4</td></tr><tr><td>Capex/D&amp;A (%)</td><td>57.5</td><td>96.5</td><td>65.7</td><td>67.2</td></tr><tr><td>FCF cover of dividends (X)</td><td>0.3</td><td>0.6</td><td>1.7</td><td>2.1</td></tr></table>

Growth & Margins (%)

Balance Sheet (€ mn)

<table><tr><td colspan="5">Balance Sheet (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>4,996.0</td><td>6,203.4</td><td>7,913.1</td><td>10,369.9</td></tr><tr><td>Accounts receivable</td><td>1,282.4</td><td>1,673.3</td><td>1,594.1</td><td>1,553.7</td></tr><tr><td>Inventory</td><td>6,006.4</td><td>5,856.6</td><td>5,785.7</td><td>6,123.6</td></tr><tr><td>Financial services assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>7,653.2</td><td>8,140.9</td><td>8,436.2</td><td>8,737.9</td></tr><tr><td>Total current assets</td><td>19,938.0</td><td>22,284.7</td><td>24,139.5</td><td>27,195.5</td></tr><tr><td>Net PP&amp;E</td><td>15,702.0</td><td>17,039.1</td><td>17,163.2</td><td>17,169.0</td></tr><tr><td>Net intangibles</td><td>8,243.0</td><td>7,046.0</td><td>5,726.3</td><td>4,602.3</td></tr><tr><td>Total investments</td><td>3,710.5</td><td>3,523.4</td><td>3,488.4</td><td>3,453.4</td></tr><tr><td>Other long-term assets</td><td>5,121.5</td><td>5,641.3</td><td>6,330.3</td><td>7,034.2</td></tr><tr><td>Total assets</td><td>52,715.0</td><td>55,534.5</td><td>56,847.7</td><td>59,454.4</td></tr><tr><td>Accounts payable</td><td>3,244.0</td><td>3,568.5</td><td>3,399.5</td><td>3,475.1</td></tr><tr><td>Short-term debt</td><td>4,908.0</td><td>5,049.0</td><td>5,049.0</td><td>5,049.0</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>5,968.6</td><td>6,204.4</td><td>5,924.4</td><td>5,924.4</td></tr><tr><td>Total current liabilities</td><td>14,120.6</td><td>14,821.9</td><td>14,372.9</td><td>14,448.5</td></tr><tr><td>Long-term debt</td><td>6,711.0</td><td>7,211.9</td><td>7,987.4</td><td>8,774.7</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>8,763.0</td><td>8,510.6</td><td>8,390.6</td><td>8,390.6</td></tr><tr><td>Total long-term liabilities</td><td>15,474.0</td><td>15,722.5</td><td>16,378.0</td><td>17,165.3</td></tr><tr><td>Total liabilities</td><td>29,594.6</td><td>30,544.4</td><td>30,750.9</td><td>31,613.8</td></tr><tr><td>Preferred shares</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total common equity</td><td>22,991.0</td><td>24,891.7</td><td>26,039.7</td><td>27,838.3</td></tr><tr><td>Minority interest</td><td>129.5</td><td>98.5</td><td>57.3</td><td>2.4</td></tr><tr><td>Total liabilities &amp; equity</td><td>52,715.1</td><td>55,534.6</td><td>56,847.8</td><td>59,454.5</td></tr><tr><td>Financial services adjustment</td><td>2,625.4</td><td>2,819.7</td><td>3,028.5</td><td>3,246.8</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(9.5)</td><td>(0.6)</td><td>(1.0)</td><td>5.4</td></tr><tr><td>EBITDA growth</td><td>(39.7)</td><td>10.6</td><td>13.2</td><td>14.0</td></tr><tr><td>EBIT growth</td><td>(92.7)</td><td>453.1</td><td>32.9</td><td>33.0</td></tr><tr><td>Net inc. growth</td><td>(88.0)</td><td>390.1</td><td>6.2</td><td>33.1</td></tr><tr><td>EPS growth</td><td>(88.0)</td><td>289.3</td><td>33.6</td><td>33.1</td></tr><tr><td>DPS growth</td><td>(56.5)</td><td>20.0</td><td>8.3</td><td>15.4</td></tr></table>

Price Performance  
![](images/c5007c9f9b5038f02b3f18464fd17189be3895fd857063315944b0a04ed34016.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>10.3%</td><td>(4.3)%</td><td>1.9%</td></tr><tr><td>Rel. to the FTSE World Europe (EUR)</td><td>5.5%</td><td>(9.3)%</td><td>(12.6)%</td></tr></table>

<table><tr><td colspan="5">Cash Flow (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>444.8</td><td>2,977.0</td><td>3,142.8</td><td>4,182.9</td></tr><tr><td>D&amp;A add-back</td><td>5,451.0</td><td>4,201.4</td><td>4,305.8</td><td>4,329.0</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(2,166.4)</td><td>(1,264.0)</td><td>(1,803.1)</td><td>(1,227.6)</td></tr><tr><td>Other operating cash flow</td><td>(115.6)</td><td>(1,344.0)</td><td>(907.8)</td><td>(1,219.9)</td></tr><tr><td>Cash flow from operations</td><td>3,613.8</td><td>4,570.4</td><td>4,737.7</td><td>6,064.5</td></tr><tr><td>Capital expenditures</td><td>(3,136.0)</td><td>(4,056.3)</td><td>(2,828.8)</td><td>(2,910.6)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>54.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(670.0)</td><td>8.0</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(3,752.0)</td><td>(4,048.3)</td><td>(2,828.8)</td><td>(2,910.6)</td></tr><tr><td>Repayment of lease liabilities</td><td>(135.0)</td><td>100.7</td><td>118.6</td><td>(300.1)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(2,095.3)</td><td>(911.0)</td><td>(1,093.2)</td><td>(1,184.3)</td></tr><tr><td>Inc/(dec) in debt</td><td>630.0</td><td>475.0</td><td>775.5</td><td>787.3</td></tr><tr><td>Other financing cash flows</td><td>392.3</td><td>1,020.6</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(1,208.0)</td><td>685.4</td><td>(199.2)</td><td>(697.1)</td></tr><tr><td>Total cash flow</td><td>(1,388.2)</td><td>1,207.4</td><td>1,709.7</td><td>2,456.8</td></tr><tr><td>Reinvestment rate (%)</td><td>54.3</td><td>69.5</td><td>43.2</td><td>39.9</td></tr></table>

Source: FactSet. Price as of 10 Jul 2026 close.  
Source: Company data, GS estimates.

Income Statement (€ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>36,272.0</td><td>36,038.7</td><td>35,677.8</td><td>37,601.6</td></tr><tr><td>Total operating expenses</td><td>(29,136.0)</td><td>(28,488.8)</td><td>(26,873.7)</td><td>(27,973.5)</td></tr><tr><td>R&amp;D</td><td>(1,329.0)</td><td>(1,233.4)</td><td>(1,300.2)</td><td>(1,426.1)</td></tr><tr><td>Other operating inc./(exp.)</td><td>57.0</td><td>169.3</td><td>(163.2)</td><td>163.1</td></tr><tr><td>EBITDA</td><td>5,864.0</td><td>6,485.8</td><td>7,340.7</td><td>8,365.0</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(5,451.0)</td><td>(4,201.4)</td><td>(4,305.8)</td><td>(4,329.0)</td></tr><tr><td>EBIT</td><td>413.0</td><td>2,284.4</td><td>3,034.9</td><td>4,036.0</td></tr><tr><td>Net interest inc./(exp.)</td><td>31.8</td><td>692.6</td><td>107.9</td><td>146.9</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>444.8</td><td>2,977.0</td><td>3,142.8</td><td>4,182.9</td></tr><tr><td>Provision for taxes</td><td>(135.0)</td><td>(904.6)</td><td>(942.8)</td><td>(1,254.9)</td></tr><tr><td>Minority interest</td><td>121.0</td><td>38.9</td><td>41.2</td><td>54.9</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>430.8</td><td>2,111.3</td><td>2,241.2</td><td>2,983.0</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>430.8</td><td>2,111.3</td><td>2,241.2</td><td>2,983.0</td></tr><tr><td>EPS (basic, pre-except) (€)</td><td>0.47</td><td>2.32</td><td>2.46</td><td>3.27</td></tr><tr><td>EPS (basic, post-except) (€)</td><td>0.47</td><td>1.84</td><td>2.46</td><td>3.27</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>911.0</td><td>911.0</td><td>911.0</td><td>911.0</td></tr><tr><td>Tax rate (%)</td><td>30.4</td><td>30.4</td><td>30.0</td><td>30.0</td></tr><tr><td>Common dividends declared</td><td>911.0</td><td>1,093.2</td><td>1,184.3</td><td>1,366.5</td></tr><tr><td>DPS (€)</td><td>1.00</td><td>1.20</td><td>1.30</td><td>1.50</td></tr></table>

## Key charts from our recent upgrade to Buy

Exhibit 1: We expect significant ASP increases in the near term, driven by the maturing of the 911 model mix... Porsche 911 variants mix per generation  
![](images/9c6cab011c2a75820ab2f2a841ac805415e05c9ca1862f51adff02f0bf346830.jpg)  
Source: EEA, GS Global Investment Research

Exhibit 2: ...which historically has been burdened by supplier force-majeure disrupting the top-end ramp 911 model implied EU ASP (€k); 25-27 GSe mix  
![](images/9e112d3af70583a0aeba1f9dc9500fcfa4bce22a104536be3a246d1eca7e73f1.jpg)  
Source: EEA, ADAC, GS Global Investment Research

Exhibit 3: Meanwhile, we see significant room for Porsche to address its SG&A cost base...
Porsche SG&A expenses (€mn) and as % of revenue (%)  
![](images/608736bad1b9f42c9eebb5a4edf5a654e24388153c28d15ec7ed58d3cf27a4fc.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: ...which sits materially above both premium and luxury peers in the sector
SG&A as % of Revenue per OEM  
![](images/5f86a9b145173ac19facf752edb2beb65dfc6eba3dff358793a87113effe8363.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: We expect a near-term offset primarily from price/mix and SG&A initiatives; in the medium term, we expect volume recovery  
26E to 30E GSe Auto EBIT bridge  
![](images/47a2863a358b4dd0c89a3dbe43c1d69eca1a487ef5a568f20540eaa352101b37.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 6: We see Porsche's multi-year EPS recovery path as justifying a premium valuation in the near term  
2Y FWD EPS (LHS, €); 2Y FWD P/E & Historical Median (RHS); Dashed forceast uses GSe EPS & TP and implied P/E  
![](images/ff56ef4443582579839cdc7edf3a10ad5d14d2902669caaf07a54258675343b5.jpg)  
Source: Bloomberg, GS Global Investment Research

## Cost-momentum accelerating with 911 likely to further offset lower FY27 volumes

We upgraded Porsche AG to Buy on 11 June, emphasizing room for positive earnings revisions despite continued structural headwinds, which we believe are now largely priced in. Our differentiated view centred on two underappreciated near-term offset mechanisms: i) 911 mix normalization driving ASP acceleration and ii) indirect cost reduction, namely on SG&A. Since 11 June, significant news flow and company messaging have signalled an acceleration of cost-momentum alongside continued 911 strength, further supporting our thesis.

## Cost-momentum accelerating and progressing in-line with our Buy-thesis

## Second personnel package close to finalisation

Several developments flagged at the time of our upgrade have since been addressed by the company or repo

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
