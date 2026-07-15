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
# Mercedes-Benz Group AG (MBGn.DE)

# 2Q26 preview: Trimming estimates on softer China profitability; 2Q Cars margin still within guidance

MBGn.DE

12m Price Target: €65.00

Price: €45.11

Upside: 44.1%

Following Mercedes's release of 2Q26 wholesale volume and public pre-close call on July 14, in which the company expects 2Q Cars adj. EBIT margin to be in line with the full-year range (3-5%, GSe 3.4%, Visible Alpha consensus 3.5%), we revise our price target and estimates to reflect stronger US/Europe (+10%/+4% vs. previous GSe +1%/+2%), softer China volume (-30% vs. previous GSe -14%) and lower BBAC JV profitability (4.0% at FY26, cut from 6%). We now expect the company to report 2Q Group adj. EPS of €1.43 (vs. cons €1.29) and Cars adj. EBIT at €778mn or 3.4% margin (vs. cons €816mn or 3.5%). For FY26, we forecast Cars adj. EBIT margin at 4.0% (cons 3.7%). Mercedes is scheduled to report 2Q results on July 28.

New products are gaining strong momentum, but China remains the key drag on volumes. Group unit sales reached 418k in 2Q, down 8% yoy driven by declines China, partly offset by Europe and the US. Europe delivered positive momentum on the back of the new products CLA, GLB, and GLC, while the US was supported by the GLE and GLE Coupe. Electrification continues to accelerate, with BEVs up +51% yoy globally (+87% yoy in Europe or a 26% BEV share there) and the overall xEV BEV share reaching 13%. Demand for the electric CLA, GLB, and GLC is strong with orders extending into next year, and electric C-Class orders opened in May. Top-end vehicles came in at 58k units, affected by planned product changeovers and timing of availability, leading to 2Q TEV share at c.14%.

Profitability is tracking within guidance across divisions, though reported earnings may be clouded by non-cash items. For Cars, management expects 2Q adjusted EBIT margin within the full-year guidance range of 3-5% (GSe 3.4%, cons 3.5%), Vans adj. EBIT margin towards the upper end of the 8-10% range (GSe 9.2%, cons 9.0%), while Financial Services adj.

## BUY

Christian Frenes
+44(20)7051-8641 | christian.frenes@gs.com
GS International

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

Shivam Kotecha
+1(332)245-7822 | shivam.kotecha@gs.com
GS India SPL

Key Data

Market cap: €43.4bn / \$49.5bn  
Enterprise value: €66.0bn / \$75.3bn  
3m ADTV: €137.2mn / \$159.4mn  
Germany  
Europe Autos  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td colspan="5">CS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (€ mn) New</td><td>132,214.0</td><td>129,414.6</td><td>132,545.6</td><td>135,794.7</td></tr><tr><td>Revenue (€ mn) Old</td><td>132,214.0</td><td>130,918.3</td><td>134,085.7</td><td>137,382.0</td></tr><tr><td>EBIT (€ mn)</td><td>8,235.0</td><td>7,139.0</td><td>8,416.5</td><td>9,186.0</td></tr><tr><td>EPS (€) New</td><td>5.34</td><td>5.57</td><td>6.85</td><td>7.94</td></tr><tr><td>EPS (€) Old</td><td>5.34</td><td>5.81</td><td>7.41</td><td>8.41</td></tr><tr><td>P/E (X)</td><td>10.2</td><td>8.1</td><td>6.6</td><td>5.7</td></tr><tr><td>Dividend yield (%)</td><td>6.4</td><td>7.8</td><td>8.6</td><td>9.3</td></tr><tr><td>CROCI (%)</td><td>(0.7)</td><td>16.6</td><td>15.7</td><td>16.8</td></tr><tr><td>Net debt/EBITDA (X)</td><td>2.2</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (€)</td><td>1.49</td><td>1.43</td><td>1.30</td><td>1.35</td></tr></table>

GS Factor Profile

![](images/0dcd546e005f7080ee96c23a5eabf6e01f558c3d820fbf51b9d97dcbb3f88dd0.jpg)  
Source: Company data, GS estimates. See disclosures for details.

BUY

Mercedes-Benz Group AG (MBGn.DE)
Rating since Nov 23, 2025  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>EV/sales (X)</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>EV/EBITDAR (X)</td><td>7.0</td><td>6.2</td><td>5.5</td><td>5.2</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>7.0</td><td>6.2</td><td>5.5</td><td>5.2</td></tr><tr><td>EV/EBIT (X)</td><td>17.0</td><td>11.1</td><td>9.5</td><td>8.8</td></tr><tr><td>P/E (X)</td><td>10.2</td><td>8.1</td><td>6.6</td><td>5.7</td></tr><tr><td>FCF yield (%)</td><td>(13.1)</td><td>12.4</td><td>11.8</td><td>15.0</td></tr><tr><td>Dividend yield (%)</td><td>6.4</td><td>7.8</td><td>8.6</td><td>9.3</td></tr><tr><td>EV/GCI (X)</td><td>1.0</td><td>0.8</td><td>0.8</td><td>0.8</td></tr><tr><td>CROCI (%)</td><td>(0.7)</td><td>16.6</td><td>15.7</td><td>16.8</td></tr><tr><td>ROIC (%)</td><td>11.1</td><td>7.7</td><td>8.9</td><td>9.6</td></tr><tr><td>ROA (%)</td><td>1.9</td><td>2.0</td><td>2.3</td><td>2.6</td></tr><tr><td>Days inventory outst, sales</td><td>68.4</td><td>68.0</td><td>68.3</td><td>68.5</td></tr><tr><td>Asset turnover (X)</td><td>5.0</td><td>4.7</td><td>4.8</td><td>4.9</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>26.2</td><td>23.1</td><td>24.9</td><td>26.7</td></tr><tr><td>Capex/D&amp;A (%)</td><td>137.0</td><td>122.2</td><td>109.5</td><td>106.3</td></tr><tr><td>FCF cover of dividends (X)</td><td>(2.2)</td><td>1.7</td><td>1.4</td><td>1.7</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(9.2)</td><td>(2.1)</td><td>2.4</td><td>2.5</td></tr><tr><td>EBITDA growth</td><td>(38.9)</td><td>15.8</td><td>3.7</td><td>4.6</td></tr><tr><td>EBIT growth</td><td>(63.1)</td><td>29.7</td><td>12.4</td><td>8.0</td></tr><tr><td>Net inc. growth</td><td>(49.6)</td><td>0.6</td><td>15.8</td><td>9.9</td></tr><tr><td>EPS growth</td><td>(47.6)</td><td>4.2</td><td>23.0</td><td>15.9</td></tr><tr><td>DPS growth</td><td>(18.6)</td><td>0.0</td><td>11.4</td><td>7.7</td></tr></table>

<table><tr><td>Balance Sheet (€ mn)</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>10,118.0</td><td>5,855.9</td><td>7,625.2</td><td>9,567.2</td></tr><tr><td>Accounts receivable</td><td>5,352.0</td><td>5,776.2</td><td>5,945.4</td><td>6,098.4</td></tr><tr><td>Inventory</td><td>23,787.0</td><td>24,461.0</td><td>25,149.9</td><td>25,798.1</td></tr><tr><td>Financial services assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>62,875.0</td><td>64,705.1</td><td>62,237.2</td><td>62,872.7</td></tr><tr><td>Total current assets</td><td>102,132.0</td><td>100,798.2</td><td>100,957.8</td><td>104,336.3</td></tr><tr><td>Net PP&amp;E</td><td>26,987.3</td><td>27,918.9</td><td>27,862.3</td><td>27,777.2</td></tr><tr><td>Net intangibles</td><td>20,055.8</td><td>20,806.1</td><td>21,560.2</td><td>22,110.0</td></tr><tr><td>Total investments</td><td>16,413.0</td><td>17,315.0</td><td>15,315.0</td><td>13,315.0</td></tr><tr><td>Other long-term assets</td><td>89,878.0</td><td>89,617.7</td><td>86,821.8</td><td>87,541.7</td></tr><tr><td>Total assets</td><td>255,466.0</td><td>256,455.9</td><td>252,517.0</td><td>255,080.2</td></tr><tr><td>Accounts payable</td><td>9,890.0</td><td>11,696.2</td><td>11,924.1</td><td>12,231.5</td></tr><tr><td>Short-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>63,878.0</td><td>64,239.8</td><td>62,552.3</td><td>63,179.6</td></tr><tr><td>Total current liabilities</td><td>73,768.0</td><td>75,936.0</td><td>74,476.4</td><td>75,411.1</td></tr><tr><td>Long-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>87,458.0</td><td>87,482.5</td><td>84,553.4</td><td>85,306.7</td></tr><tr><td>Total long-term liabilities</td><td>87,458.0</td><td>87,482.5</td><td>84,553.4</td><td>85,306.7</td></tr><tr><td>Total liabilities</td><td>161,226.0</td><td>163,418.5</td><td>159,029.8</td><td>160,717.9</td></tr><tr><td>Preferred shares</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total common equity</td><td>93,257.0</td><td>91,961.0</td><td>92,388.2</td><td>93,237.2</td></tr><tr><td>Minority interest</td><td>983.0</td><td>1,076.4</td><td>1,099.1</td><td>1,125.1</td></tr><tr><td>Total liabilities &amp; equity</td><td>255,466.0</td><td>256,455.9</td><td>252,517.0</td><td>255,080.2</td></tr><tr><td>Financial services adjustment</td><td>--</td><td>--</td><td>--</td><td>--</td></tr></table>

Balance Sheet (€ mn)

Price Performance  
![](images/e57eaac8cb13c9006e042e5ca7358828a163bd6064c3243c7164846d56fc4634.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(17.7)%</td><td>(25.7)%</td><td>(12.9)%</td></tr><tr><td>Rel. to the FTSE World Europe (EUR)</td><td>(21.3)%</td><td>(29.4)%</td><td>(26.0)%</td></tr></table>

Cash Flow (€ mn)

<table><tr><td colspan="5">Cash Flow (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>5,141.0</td><td>5,170.9</td><td>5,989.7</td><td>6,584.2</td></tr><tr><td>D&amp;A add-back</td><td>7,091.0</td><td>7,564.6</td><td>7,318.6</td><td>7,423.3</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>2,866.0</td><td>700.0</td><td>(630.2)</td><td>(493.7)</td></tr><tr><td>Other operating cash flow</td><td>(12,435.0)</td><td>1,398.0</td><td>107.3</td><td>165.2</td></tr><tr><td>Cash flow from operations</td><td>2,663.0</td><td>14,833.5</td><td>12,785.3</td><td>13,679.0</td></tr><tr><td>Capital expenditures</td><td>(9,714.0)</td><td>(9,246.6)</td><td>(8,016.2)</td><td>(7,888.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>2,731.0</td><td>(503.0)</td><td>2,000.0</td><td>2,000.0</td></tr><tr><td>Cash flow from investing</td><td>(6,360.0)</td><td>(9,771.6)</td><td>(6,016.2)</td><td>(5,888.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(4,140.0)</td><td>(3,409.8)</td><td>(3,062.5)</td><td>(3,235.2)</td></tr><tr><td>Inc/(dec) in debt</td><td>(145.0)</td><td>32.0</td><td>13.6</td><td>(4.4)</td></tr><tr><td>Other financing cash flows</td><td>918.0</td><td>(4,887.1)</td><td>(1,950.9)</td><td>(2,609.5)</td></tr><tr><td>Cash flow from financing</td><td>2,100.0</td><td>(8,924.9)</td><td>(4,999.9)</td><td>(5,849.1)</td></tr><tr><td>Total cash flow</td><td>(3,194.0)</td><td>(7,726.1)</td><td>3,538.5</td><td>3,883.9</td></tr><tr><td>Reinvestment rate (%)</td><td>NM</td><td>65.4</td><td>59.8</td><td>55.7</td></tr></table>

Source: Company data, GS estimates.  
Source: FactSet. Price as of 14 Jul 2026 close.

Income Statement (€ mn)

<table><tr><td colspan="5">Income Statement (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>132,214.0</td><td>129,414.6</td><td>132,545.6</td><td>135,794.7</td></tr><tr><td>Total operating expenses</td><td>(122,076.0)</td><td>(119,395.9)</td><td>(121,999.7)</td><td>(124,879.7)</td></tr><tr><td>R&amp;D</td><td>(6,055.0)</td><td>(5,743.2)</td><td>(5,526.2)</td><td>(5,360.4)</td></tr><tr><td>Other operating inc./(exp.)</td><td>526.0</td><td>1,703.4</td><td>1,703.4</td><td>1,703.4</td></tr><tr><td>EBITDA</td><td>11,700.0</td><td>13,543.5</td><td>14,041.7</td><td>14,681.2</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(7,091.0)</td><td>(7,564.6)</td><td>(7,318.6)</td><td>(7,423.3)</td></tr><tr><td>EBIT</td><td>4,609.0</td><td>5,978.8</td><td>6,723.0</td><td>7,258.0</td></tr><tr><td>Net interest inc./(exp.)</td><td>464.0</td><td>381.1</td><td>192.5</td><td>275.6</td></tr><tr><td>Income/(loss) from associates</td><td>1,118.0</td><td>947.6</td><td>1,315.2</td><td>1,546.5</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>93.0</td><td>245.8</td><td>245.8</td><td>245.8</td></tr><tr><td>Pre-tax profit</td><td>6,284.0</td><td>7,553.3</td><td>8,476.5</td><td>9,325.8</td></tr><tr><td>Provision for taxes</td><td>(953.0)</td><td>(2,130.6)</td><td>(2,373.4)</td><td>(2,611.2)</td></tr><tr><td>Minority interest</td><td>(190.0)</td><td>(251.9)</td><td>(113.4)</td><td>(130.4)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>5,141.0</td><td>5,170.9</td><td>5,989.7</td><td>6,584.2</td></tr><tr><td>Post-tax exceptionals</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>5,141.0</td><td>5,170.9</td><td>5,989.7</td><td>6,584.2</td></tr><tr><td>EPS (basic, pre-except) (€)</td><td>5.34</td><td>5.57</td><td>6.85</td><td>7.94</td></tr><tr><td>EPS (basic, post-except) (€)</td><td>5.34</td><td>5.31</td><td>6.85</td><td>7.94</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>962.4</td><td>974.2</td><td>875.0</td><td>829.5</td></tr><tr><td>Tax rate (%)</td><td>15.2</td><td>28.2</td><td>28.0</td><td>28.0</td></tr><tr><td>Common dividends declared</td><td>3,350.6</td><td>3,142.0</td><td>3,323.9</td><td>3,388.6</td></tr><tr><td>DPS (€)</td><td>3.50</td><td>3.50</td><td>3.90</td><td>4.20</td></tr></table>

RoE remains well above the 10–12% guidance (GSe 12.8%). At the Group level, 2Q adj. EBIT is expected within the range, but the reported figure may be impacted by the continued assessment of the carrying value of investments (i.e., potential non-cash charges). 2Q free cash flow should remain positive, albeit at a lower level than 1Q, according to the management.

China remains the largest swing factor. Management flagged intensifying pressure on both volume and pricing in China. The 1Q MSRP adjustment helped dealer profitability, but 2Q profit deteriorated significantly, and further dealer payments in 2H cannot be ruled out if the trend persists. Management also mentioned an ongoing review of the carrying amount of participations, which could trigger a non-cash impairment, in our view. On a more encouraging note, the electric GLC is launching in China with an entry model at RMB 299k - attractive pricing, in our view - and management reports strong pre-order numbers with high conversion.

Share buyback not contingent on the timing of M&A proceeds. Management said it would pursue partial monetisation of its Daimler Truck (DTG) stake if opportunities arise, but pointed out that the next buyback tranche is not contingent on a DTG book-build. The last program (€2bn from Nov-25, up to 12 months) was accelerated and concluded by end-Jun-26, implying €3bn of remaining scope within the authorised €5bn program. Given Mercedes' balance sheet strength, we are more optimistic on a further program and forecast €3.1bn of SBB in total for FY26 (cons: €2.3bn).

Exhibit 1: Mercedes estimate changes, new vs. old

<table><tr><td rowspan="2">€ mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2026-28E</td></tr><tr><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td></tr><tr><td colspan="13">Revenues</td></tr><tr><td>Mercedes Cars</td><td>93,888</td><td>94,531</td><td>-0.7%</td><td>96,536</td><td>97,191</td><td>-0.7%</td><td>99,298</td><td>99,976</td><td>-0.7%</td><td>289,721</td><td>291,698</td><td>-0.7%</td></tr><tr><td>Mercedes Vans</td><td>17,427</td><td>17,283</td><td>0.8%</td><td>17,602</td><td>17,457</td><td>0.8%</td><td>17,779</td><td>17,632</td><

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
