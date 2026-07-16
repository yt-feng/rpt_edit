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
# Volkswagen (VOWG\_p.DE)

Thoughts on restructuring news and Everllence transaction; revising estimates ahead of 2Q26

VOWG\_p.DE 12m Price Target: €89.00 Price: €71.88 Upside: 23.8%

Remaining cautious on execution of Future Plan: We remain cautious on VW's latest "Future" restructuring plan, given the group's organisational complexity and the internal hurdles to closing capacity. Historical plant closures have been rare, small, and geographically distant, including Audi Brussels and Dresden's Transparent Factory (both 2025), Australia (1977), Pennsylvania (1988), and various LATAM/Argentina sites in the 1990s. Nevertheless, we acknowledge management's restructuring efforts, including four ongoing programmes targeting >€6bn pa. of savings, yet the path to 8-10% RoS remains unclear.

Everllence transaction P&L lift bound on details: Volkswagen (June 24, 2026) announced the sale of a 51% stake in Everllence to Bain Capital for \~€7.4bn, with a retained 49% stake limiting. Our illustrative pro-forma framework implies an EPS uplift of €3.84-€21.42 (at 100% gain accounted) or €0.23-€11.94 (at 51% accounted). We note that key assumptions on leverage, tax treatment, accounting of the retained stake, and timing remain unconfirmed and materially influence both the realized uplift and the timing of it. See our illustrative methodology below.

Revising VW estimates ahead of 2Q26: VW continues to advance its competitive positioning through restructuring and strategic tie-ups, but structural governance layers and organizational complexity lead us to question the company's ability to respond in a timely manner to persistent headwinds. We believe investors will require evidence of sustained underlying earnings' improvement before any re-rating. We revise our reported EPS estimates by -7%/-14%/-13% for FY26E/FY27E/FY28E (we do not incorporate the Everllence transaction), incorporating our latest China views, and updated estimates for Porsche AG and Traton SE. Applying an unchanged 4.0x multiple to our blended FY27E/FY28E EPS, we derive a 12-month price target of €89 (previously €97); we reiterate our Neutral rating.

## NEUTRAL

Christian Frenes  
+44(20)7051-8641 | christian.frenes@gs.com  
GS International

Robert Triulzi
+44(20)7552-2281 | robert.triulzi@gs.com
GS International

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

Key Data

Market cap: €36.6bn / \$41.8bn  
Enterprise value: €53.0bn / \$61.2bn  
3m ADTV: €84.5mn / \$97.8mn  
Germany  
Europe Autos  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (€ mn) New</td><td>321,913.5</td><td>326,886.7</td><td>336,154.4</td><td>342,587.7</td></tr><tr><td>Revenue (€ mn) Old</td><td>321,913.5</td><td>330,616.3</td><td>339,151.0</td><td>347,180.7</td></tr><tr><td>EBIT (€ mn)</td><td>8,868.0</td><td>14,493.7</td><td>17,121.6</td><td>19,408.3</td></tr><tr><td>EPS (€) New</td><td>13.35</td><td>17.25</td><td>20.94</td><td>23.62</td></tr><tr><td>EPS (€) Old</td><td>13.35</td><td>18.56</td><td>24.27</td><td>27.15</td></tr><tr><td>P/E (X)</td><td>7.2</td><td>4.2</td><td>3.4</td><td>3.0</td></tr><tr><td>Dividend yield (%)</td><td>5.5</td><td>7.2</td><td>8.6</td><td>9.7</td></tr><tr><td>CROCI (%)</td><td>(0.5)</td><td>3.8</td><td>4.0</td><td>4.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(1.0)</td><td>(0.9)</td><td>(1.0)</td><td>(1.1)</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (€)</td><td>2.61</td><td>4.75</td><td>2.78</td><td>7.11</td></tr></table>

GS Factor Profile

![](images/a99c49ca88fb1151f493cd904206120c26857e1a4b0a3bb29904fc5019fc3c95.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Volkswagen (VOWG\_p.DE)

Rating since Nov 23, 2025

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>EV/sales (X)</td><td>0.5</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>EV/EBITDAR (X)</td><td>4.3</td><td>3.7</td><td>3.4</td><td>3.0</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>4.3</td><td>3.7</td><td>3.4</td><td>3.0</td></tr><tr><td>EV/EBIT (X)</td><td>17.4</td><td>9.5</td><td>7.7</td><td>6.5</td></tr><tr><td>P/E (X)</td><td>7.2</td><td>4.2</td><td>3.4</td><td>3.0</td></tr><tr><td>FCF yield (%)</td><td>(12.1)</td><td>8.5</td><td>13.6</td><td>13.0</td></tr><tr><td>Dividend yield (%)</td><td>5.5</td><td>7.2</td><td>8.6</td><td>9.7</td></tr><tr><td>EV/GCI (X)</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.0</td></tr><tr><td>CROCI (%)</td><td>(0.5)</td><td>3.8</td><td>4.0</td><td>4.0</td></tr><tr><td>ROIC (%)</td><td>3.9</td><td>6.2</td><td>7.2</td><td>7.9</td></tr><tr><td>ROA (%)</td><td>1.2</td><td>1.7</td><td>2.0</td><td>2.2</td></tr><tr><td>Days inventory outst, sales</td><td>56.3</td><td>55.7</td><td>54.8</td><td>53.8</td></tr><tr><td>Asset turnover (X)</td><td>4.5</td><td>4.6</td><td>4.8</td><td>5.0</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(17.0)</td><td>(16.6)</td><td>(18.3)</td><td>(19.5)</td></tr><tr><td>Capex/D&amp;A (%)</td><td>90.9</td><td>102.1</td><td>103.4</td><td>101.3</td></tr><tr><td>FCF cover of dividends (X)</td><td>(3.7)</td><td>2.4</td><td>3.0</td><td>2.6</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(0.8)</td><td>1.5</td><td>2.8</td><td>1.9</td></tr><tr><td>EBITDA growth</td><td>(10.6)</td><td>4.9</td><td>5.1</td><td>4.8</td></tr><tr><td>EBIT growth</td><td>(53.5)</td><td>63.4</td><td>18.1</td><td>13.4</td></tr><tr><td>Net inc. growth</td><td>(37.8)</td><td>29.3</td><td>21.4</td><td>12.8</td></tr><tr><td>EPS growth</td><td>(37.7)</td><td>29.2</td><td>21.4</td><td>12.8</td></tr><tr><td>DPS growth</td><td>(17.3)</td><td>(1.9)</td><td>19.4</td><td>13.0</td></tr></table>

Balance Sheet (€ mn)

<table><tr><td colspan="5">Balance Sheet (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>30,546.0</td><td>31,832.9</td><td>36,568.8</td><td>40,419.6</td></tr><tr><td>Accounts receivable</td><td>61,112.0</td><td>61,797.9</td><td>62,392.4</td><td>63,457.7</td></tr><tr><td>Inventory</td><td>48,761.0</td><td>50,932.3</td><td>50,051.0</td><td>50,905.7</td></tr><tr><td>Financial services assets</td><td>224,782.8</td><td>187,262.8</td><td>192,016.8</td><td>196,761.8</td></tr><tr><td>Other current assets</td><td>107,445.9</td><td>125,391.2</td><td>128,468.8</td><td>131,506.7</td></tr><tr><td>Total current assets</td><td>247,864.9</td><td>269,954.3</td><td>277,481.1</td><td>286,289.7</td></tr><tr><td>Net PP&amp;E</td><td>71,112.0</td><td>70,471.3</td><td>69,271.4</td><td>67,712.9</td></tr><tr><td>Net intangibles</td><td>91,026.0</td><td>93,087.7</td><td>95,052.4</td><td>96,899.8</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>234,463.7</td><td>180,071.1</td><td>183,147.5</td><td>186,254.6</td></tr><tr><td>Total assets</td><td>644,466.6</td><td>613,584.4</td><td>624,952.4</td><td>637,157.0</td></tr><tr><td>Accounts payable</td><td>32,118.0</td><td>33,591.8</td><td>33,287.3</td><td>33,044.6</td></tr><tr><td>Short-term debt</td><td>18,273.0</td><td>18,966.0</td><td>18,966.0</td><td>18,966.0</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>176,134.0</td><td>195,247.1</td><td>195,247.1</td><td>195,247.1</td></tr><tr><td>Total current liabilities</td><td>226,525.0</td><td>247,804.9</td><td>247,500.4</td><td>247,257.7</td></tr><tr><td>Long-term debt</td><td>55,767.0</td><td>52,649.0</td><td>52,649.0</td><td>52,649.0</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>159,120.5</td><td>103,708.1</td><td>106,470.7</td><td>108,833.9</td></tr><tr><td>Total long-term liabilities</td><td>214,887.5</td><td>156,357.1</td><td>159,119.7</td><td>161,482.9</td></tr><tr><td>Total liabilities</td><td>441,412.5</td><td>404,162.0</td><td>406,620.1</td><td>408,740.6</td></tr><tr><td>Preferred shares</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total common equity</td><td>174,002.0</td><td>182,051.3</td><td>190,961.1</td><td>201,045.2</td></tr><tr><td>Minority interest</td><td>29,052.4</td><td>27,371.0</td><td>27,371.0</td><td>27,371.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>644,466.9</td><td>613,584.2</td><td>624,952.2</td><td>637,156.8</td></tr><tr><td>Financial services adjustment</td><td>45,717.0</td><td>47,720.3</td><td>49,397.9</td><td>51,035.8</td></tr></table>

Price Performance  
![](images/7e64d42b1033f06554e7ce1c45e4e45ccbe621f205cb9d375c060f9a3c2130de.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(20.6)%</td><td>(30.7)%</td><td>(22.0)%</td></tr><tr><td>Rel. to the FTSE World Europe (EUR)</td><td>(23.5)%</td><td>(34.1)%</td><td>(33.9)%</td></tr></table>

<table><tr><td colspan="5">Cash Flow (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>6,709.0</td><td>11,537.1</td><td>12,938.8</td><td>15,533.5</td></tr><tr><td>D&amp;A add-back</td><td>26,823.0</td><td>22,933.7</td><td>22,203.3</td><td>21,791.8</td></tr><tr><td>Minority interest add-back</td><td>231.0</td><td>1,111.0</td><td>665.0</td><td>1,177.8</td></tr><tr><td>Net (inc)/dec working capital</td><td>3,094.0</td><td>(1,747.5)</td><td>(17.7)</td><td>(2,162.6)</td></tr><tr><td>Other operating cash flow</td><td>(21,847.9)</td><td>(4,989.5)</td><td>(4,116.3)</td><td>(5,938.9)</td></tr><tr><td>Cash flow from operations</td><td>15,009.1</td><td>28,844.7</td><td>31,673.1</td><td>30,401.7</td></tr><tr><td>Capital expenditures</td><td>(24,394.0)</td><td>(23,404.7)</td><td>(22,968.2)</td><td>(22,080.6)</td></tr><tr><td>Acquisitions</td><td>(1,499.0)</td><td>(1,741.0)</td><td>(1,400.0)</td><td>(1,400.0)</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(1,590.0)</td><td>(1,505.0)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(27,483.0)</td><td>(26,650.7)</td><td>(24,368.2)</td><td>(23,480.6)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(2,619.0)</td><td>(2,619.1)</td><td>(2,569.0)</td><td>(3,070.3)</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>14,536.5</td><td>9,988.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>11,917.5</td><td>7,368.9</td><td>(2,569.0)</td><td>(3,070.3)</td></tr><tr><td>Total cash flow</td><td>(1,494.9)</td><td>9,981.5</td><td>4,735.9</td><td>3,850.8</td></tr><tr><td>Reinvestment rate (%)</td><td>204.7</td><td>76.5</td><td>72.5</td><td>67.8</td></tr></table>

Source: FactSet. Price as of 14 Jul 2026 close.  
Source: Company data, GS estimates.

Income Statement (€ mn)

<table><tr><td colspan="5">Income Statement (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>321,913.5</td><td>326,886.7</td><td>336,154.4</td><td>342,587.7</td></tr><tr><td>Total operating expenses</td><td>(287,581.5)</td><td>(291,224.8)</td><td>(298,056.5)</td><td>(302,219.7)</td></tr><tr><td>R&amp;D</td><td>(18,434.0)</td><td>(18,063.9)</td><td>(17,614.7)</td><td>(17,533.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>(7,029.0)</td><td>(3,106.3)</td><td>(3,361.5)</td><td>(3,425.9)</td></tr><tr><td>EBITDA</td><td>35,691.0</td><td>37,427.4</td><td>39,324.9</td><td>41,200.1</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(26,823.0)</td><td>(22,933.7)</td><td>(22,203.3)</td><td>(21,791.8)</td></tr><tr><td>EBIT</td><td>8,868.0</td><td>14,493.7</td><td>17,121.6</td><td>19,408.3</td></tr><tr><td>Net interest inc./(exp.)</td><td>(1,421.0)</td><td>(1,639.4)</td><td>(1,673.7)</td><td>(1,484.3)</td></tr><tr><td>Income/(loss) from associates</td><td>930.5</td><td>524.9</td><td>(179.1)</td><td>(115.7)</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>930.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>9,307.5</td><td>13,341.2</td><td>15,268.8</td><td>17,808.4</td></tr><tr><td>Provision for taxes</td><td>(2,403.0)</td><td>(3,599.2)</td><td>(4,122.6)</td><td>(4,808.3)</td></tr><tr><td>Minority interest</td><td>(231.0)</td><td>(1,111.0)</td><td>(665.0)</td><td>(1,177.8)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>6,673.5</td><td>8,631.0</td><td>10,481.2</td><td>11,822.3</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>6,673.5</td><td>8,631.0</td><td>10,481.2</td><td>11,822.3</td></tr><tr><td>EPS (basic, pre-except) (€)</td><td>13.31</td><td>17.22</td><td>20.91</td><td>23.58</td></tr><tr><td>EPS (basic, post-except) (€)</td><td>13.31</td><td>17.22</td><td>20.91</td><td>23.58</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>501.3</td><td>501.3</td><td>501.3</td><td>501.3</td></tr><tr><td>Tax rate (%)</td><td>25.8</td><td>27.0</td><td>27.0</td><td>27.0</td></tr><tr><td>Common dividends declared</td><td>2,636.8</td><td>2,586.7</td><td>3,088.0</td><td>3,489.0</td></tr><tr><td>DPS (€)</td><td>5.26</td><td>5.16</td><td>6.16</td><td>6.96</td></tr></table>

## Restructuring optimism overdone; execution remains the key hurdle

Recent restructuring headlines have driven a rebound in investor sentiment but, in our view, the market is likely mispricing the execution risk inherent to Volkswagen's organizational complexity. Press coverage ahead of the CEO's July 9, 2026 proposal to the Supervisory Board outlined a materially more aggressive restructuring package than that which was ultimately detailed in consecutive company releases on the proposal. The initial press speculation talked to personnel reductions of up to 100k globally, and the potential closure of four German plants, said to be Hanover, Emden, Zwickau, and Audi's Neckarsulm, with phased shutdowns between 2031 and 2034. Per the subsequent company announcements, VW is now targeting a reduction of the model line-up of up to 50%, a cut in its offering complexity of up to 75%, and a resizing of its global production capacity to approximately \~9m units per year (from \~12m pre-COVID). The press release following the presentation of the proposal to the Supervisory Board also reconfirmed Volkswagen Group's commitment to a RoS margin of 8%-10% by 2030.

Exhibit 1: Volkswagen is currently executing four separate restructuring programmes simultaneously and aims to realise a total of >€6bn pa of cost savings
VW restructuring overview

<table><tr><td>Programme</td><td>Targets</td></tr><tr><td>Future Volkswagen (Zukunft Volkswagen)</td><td>€1.5bn p.a. labor savings from the wage settlement by 2029Technical capacity reduction by ~730k units by 2028E&gt;35k employee reduction by 2030Net cost effects &gt;€4bn p.a by 2030</td></tr><tr><td>Audi &quot;Agreement for the Future&quot;</td><td>Workforce reduction ~7,500 positions-25% German site capacity reductionBrussels site closure reduces capacity by ~120k units&gt;€1bn p.a. mid-term savings</td></tr><tr><td>Porsche AG strategic realignment</td><td>15% total workforce reduction by 2029 (~3,900)Rescale China dealerships from 150 

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
