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
# Microsoft Corp. (MSFT)

# Four Key Themes into 4QFY EPS

MSFT

12m Price Target: \$610.00

Price: \$388.84

Upside: $56.9\%$

Microsoft will report 4QFY (June) results on 7/29. Since 3Q EPS on 4/29, the stock is down $5\%$ (vs. the Nasdaq up $5\%$ ), we believe primarily because of three overhangs: 1) upward revisions to capex with only small upward revisions to Azure, particularly given new signs that capex may be elevated for longer (e.g. Google's \$80bn equity raise); 2) concerns around Microsoft's exposure to increased memory pricing via Nvidia, relative to competitors with more mature internal silicon offerings; and 3) the potential for Microsoft's knowledge worker applications business (Office 365) to be disintermediated with new AI competition, such as Claude Cowork, fueled by mixed reviews on Copilot.

We think risk/reward is positive into the print: the near-term fundamental outlook has improved and believe investor expectations are low:

For 4QFY, Azure growth remains supply constrained but should accelerate for the second consecutive quarter. We see 40-41% cc growth as likely (vs. guidance of 39-40% cc).

For 1QFY, we expect Azure guidance of 40-41% vs. the Street at 41% cc (with the potential for Microsoft to ultimately report slightly above this). Recall that Microsoft guided Azure to accelerate modestly in 1HFY27 vs. 2HFY26.

We are raising our capex estimates for FY28-30 by \~10% based on ongoing supply/demand commentary and updated AI investment expectations from chip vendors. We are now at \$319bn for FY28 (+30% yoy) including financial leases (\$278bn excluding), vs. \$287bn prior and the Street at \$252bn including financial leases.

\- On Copilot, we think a sustainable M365 acceleration will likely take time, but we expect positive datapoints in the meanwhile e.g. with Microsoft's seat count disclosure (>20mn in 3Q and

Gabriela Borges, CFA
+1(212)902-7839 | gabriela.borges@gs.com
GS & Co. LLC

Callie Valenti  
+1(212)357-2790 | callie.valenti@gs.com  
GS & Co. LLC

Selina Zhang  
+1(212)357-9979 | selina.zhang@gs.com  
GS & Co. LLC

<table><tr><td>Key Data</td></tr><tr><td>Market cap: $2.9tr</td></tr><tr><td>Enterprise value: $2.9tr</td></tr><tr><td>3m ADTV: $16.2bn</td></tr><tr><td>United States</td></tr><tr><td>Americas Software</td></tr><tr><td>M&amp;A Rank: 3</td></tr></table>

GS Forecast

<table><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>Revenue ($ mn) New</td><td>281,724.0</td><td>329,440.2</td><td>387,103.7</td><td>466,617.4</td></tr><tr><td>Revenue ($ mn) Old</td><td>281,724.0</td><td>329,440.2</td><td>387,103.7</td><td>463,474.2</td></tr><tr><td>EBITDA ($ mn)</td><td>156,528.0</td><td>193,093.1</td><td>240,672.0</td><td>309,384.6</td></tr><tr><td>EBIT ($ mn)</td><td>128,528.0</td><td>153,454.1</td><td>178,230.1</td><td>212,522.7</td></tr><tr><td>EPS ($) New</td><td>13.91</td><td>16.75</td><td>19.32</td><td>22.93</td></tr><tr><td>EPS ($) Old</td><td>13.91</td><td>16.75</td><td>19.47</td><td>23.61</td></tr><tr><td>P/E (X)</td><td>30.5</td><td>23.2</td><td>20.1</td><td>17.0</td></tr><tr><td>Dividend yield (%)</td><td>0.8</td><td>0.9</td><td>0.9</td><td>0.9</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.3)</td><td>(0.2)</td><td>(0.2)</td><td>(0.1)</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS ($)</td><td>4.27</td><td>4.22</td><td>4.66</td><td>4.77</td></tr></table>

GS Factor Profile

![](images/dd66ab0f4489f1c71dd264bf6bf07db7ef9bb48d2390f75f848ac1e0171320f5.jpg)  
Source: Company data, GS estimates. See disclosures for details.

Microsoft Corp. (MSFT) Rating since Jan 21, 2021

Ratios & Valuation

<table><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>P/E (X)</td><td>30.5</td><td>23.2</td><td>20.1</td><td>17.0</td></tr><tr><td>EV/EBITDA (X)</td><td>19.8</td><td>14.7</td><td>11.9</td><td>9.3</td></tr><tr><td>EV/sales (X)</td><td>11.0</td><td>8.6</td><td>7.4</td><td>6.2</td></tr><tr><td>FCF yield (%)</td><td>2.3</td><td>2.1</td><td>1.0</td><td>0.6</td></tr><tr><td>EV/DACF (X)</td><td>22.1</td><td>15.7</td><td>13.2</td><td>10.3</td></tr><tr><td>CROCI (%)</td><td>29.6</td><td>30.9</td><td>28.5</td><td>27.9</td></tr><tr><td>ROE (%)</td><td>33.9</td><td>32.0</td><td>28.9</td><td>27.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.3)</td><td>(0.2)</td><td>(0.2)</td><td>(0.1)</td></tr><tr><td>Net debt/equity (%)</td><td>(15.0)</td><td>(9.4)</td><td>(6.9)</td><td>(3.3)</td></tr><tr><td>Interest cover (X)</td><td>53.9</td><td>52.6</td><td>72.5</td><td>113.3</td></tr><tr><td>Inventory days</td><td>4.5</td><td>3.6</td><td>3.6</td><td>3.5</td></tr><tr><td>Receivable days</td><td>82.2</td><td>82.9</td><td>81.0</td><td>77.4</td></tr><tr><td>Days payable outstanding</td><td>103.3</td><td>114.2</td><td>126.2</td><td>129.2</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>Total revenue growth</td><td>14.9</td><td>16.9</td><td>17.5</td><td>20.5</td></tr><tr><td>EBITDA growth</td><td>20.9</td><td>23.4</td><td>24.6</td><td>28.6</td></tr><tr><td>EPS growth</td><td>17.9</td><td>20.5</td><td>15.3</td><td>18.7</td></tr><tr><td>DPS growth</td><td>10.6</td><td>9.9</td><td>2.2</td><td>0.0</td></tr><tr><td>Gross margin</td><td>68.8</td><td>67.7</td><td>65.1</td><td>62.2</td></tr><tr><td>EBIT margin</td><td>45.6</td><td>46.6</td><td>46.0</td><td>45.5</td></tr></table>

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>30,242.0</td><td>30,736.0</td><td>43,715.0</td><td>41,557.3</td></tr><tr><td>Accounts receivable</td><td>69,905.0</td><td>79,687.5</td><td>92,138.8</td><td>105,723.6</td></tr><tr><td>Inventory</td><td>938.0</td><td>1,149.4</td><td>1,492.1</td><td>1,923.5</td></tr><tr><td>Other current assets</td><td>90,046.0</td><td>83,838.5</td><td>62,103.4</td><td>44,428.3</td></tr><tr><td>Total current assets</td><td>191,131.0</td><td>195,411.4</td><td>199,449.4</td><td>193,632.8</td></tr><tr><td>Net PP&amp;E</td><td>229,789.0</td><td>338,629.0</td><td>524,350.5</td><td>748,223.0</td></tr><tr><td>Net intangibles</td><td>142,113.0</td><td>137,986.0</td><td>135,086.0</td><td>133,086.0</td></tr><tr><td>Total investments</td><td>15,405.0</td><td>33,683.0</td><td>33,683.0</td><td>33,683.0</td></tr><tr><td>Other long-term assets</td><td>40,565.0</td><td>42,052.0</td><td>42,038.3</td><td>45,697.7</td></tr><tr><td>Total assets</td><td>619,003.0</td><td>747,761.4</td><td>934,607.2</td><td>1,154,322.5</td></tr><tr><td>Accounts payable</td><td>27,724.0</td><td>38,803.2</td><td>54,572.7</td><td>70,349.7</td></tr><tr><td>Short-term debt</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Current lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>113,494.0</td><td>123,623.5</td><td>138,063.4</td><td>159,122.3</td></tr><tr><td>Total current liabilities</td><td>141,218.0</td><td>162,426.7</td><td>192,636.1</td><td>229,472.0</td></tr><tr><td>Long-term debt</td><td>40,152.0</td><td>27,003.5</td><td>18,164.5</td><td>9,325.5</td></tr><tr><td>Non-current lease liabilities</td><td>17,437.0</td><td>16,703.0</td><td>16,703.0</td><td>16,703.0</td></tr><tr><td>Other long-term liabilities</td><td>74,007.0</td><td>101,442.2</td><td>143,527.2</td><td>183,884.6</td></tr><tr><td>Total long-term liabilities</td><td>134,306.0</td><td>148,235.4</td><td>181,933.3</td><td>213,976.0</td></tr><tr><td>Total liabilities</td><td>275,524.0</td><td>310,662.1</td><td>374,569.4</td><td>443,448.0</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>343,479.0</td><td>437,099.3</td><td>560,037.8</td><td>710,874.5</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total liabilities &amp; equity</td><td>619,003.0</td><td>747,761.4</td><td>934,607.2</td><td>1,154,322.5</td></tr><tr><td>BVPS ($)</td><td>46.21</td><td>58.84</td><td>75.27</td><td>95.24</td></tr></table>

Price Performance  
![](images/c3a3370dfb807267abf632d2d672d39446cb3e9e46ce8e4a4a31281645134bd4.jpg)

Cash Flow (\$ mn)

<table><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>Net income</td><td>101,832.0</td><td>129,372.9</td><td>144,251.5</td><td>171,710.4</td></tr><tr><td>D&amp;A add-back</td><td>34,153.0</td><td>43,999.3</td><td>62,442.0</td><td>96,861.9</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(5,350.0)</td><td>(8,324.0)</td><td>15,616.0</td><td>15,192.7</td></tr><tr><td>Others</td><td>5,527.0</td><td>9,510.0</td><td>10,478.4</td><td>11,434.2</td></tr><tr><td>Cash flow from operations</td><td>136,162.0</td><td>174,558.2</td><td>232,787.9</td><td>295,199.3</td></tr><tr><td>Capital expenditures</td><td>(64,551.0)</td><td>(112,596.1)</td><td>(203,178.5)</td><td>(278,376.9)</td></tr><tr><td>Acquisitions</td><td>(5,978.0)</td><td>(1,291.0)</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(2,070.0)</td><td>(3,232.0)</td><td>24,000.0</td><td>22,167.0</td></tr><tr><td>Cash flow from investing</td><td>(72,599.0)</td><td>(117,119.1)</td><td>(179,178.5)</td><td>(256,209.9)</td></tr><tr><td>Dividends paid</td><td>(24,082.0)</td><td>(26,442.9)</td><td>(27,076.2)</td><td>(27,162.6)</td></tr><tr><td>Share issuance/(repurchase)</td><td>(16,364.0)</td><td>(21,010.7)</td><td>(4,715.3)</td><td>(5,145.4)</td></tr><tr><td>Inc/(dec) in debt</td><td>(8,962.0)</td><td>(7,419.5)</td><td>(8,839.0)</td><td>(8,839.0)</td></tr><tr><td>Others</td><td>(2,228.0)</td><td>(2,072.0)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>(51,636.0)</td><td>(56,945.1)</td><td>(40,630.4)</td><td>(41,147.0)</td></tr><tr><td>Total cash flow</td><td>11,927.0</td><td>494.0</td><td>12,979.0</td><td>(2,157.6)</td></tr><tr><td>Free cash flow</td><td>71,611.0</td><td>61,962.1</td><td>29,609.4</td><td>16,822.3</td></tr><tr><td>Free cash flow per share (basic) ($)</td><td>9.63</td><td>8.34</td><td>3.98</td><td>2.25</td></tr></table>

Source: FactSet. Price as of 7 Jul 2026 close.

Income Statement (\$ mn)

<table><tr><td colspan="5">Income Statement ($ mn)</td></tr><tr><td></td><td>6/25</td><td>6/26E</td><td>6/27E</td><td>6/28E</td></tr><tr><td>Total revenue</td><td>281,724.0</td><td>329,440.2</td><td>387,103.7</td><td>466,617.4</td></tr><tr><td>Cost of goods sold</td><td>(87,831.0)</td><td>(106,274.8)</td><td>(135,052.6)</td><td>(176,457.0)</td></tr><tr><td>SG&amp;A</td><td>(32,877.0)</td><td>(34,522.8)</td><td>(35,817.3)</td><td>(36,593.7)</td></tr><tr><td>R&amp;D</td><td>(32,488.0)</td><td>(35,188.6)</td><td>(38,003.7)</td><td>(41,044.0)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>156,528.0</td><td>193,093.1</td><td>240,672.0</td><td>309,384.6</td></tr><tr><td>Depreciation &amp; amortization</td><td>(28,000.0)</td><td>(39,639.0)</td><td>(62,442.0)</td><td>(96,861.9)</td></tr><tr><td>EBIT</td><td>128,528.0</td><td>153,454.1</td><td>178,230.1</td><td>212,522.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>262.0</td><td>266.8</td><td>(141.7)</td><td>(534.5)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>126,319.0</td><td>154,741.9</td><td>178,088.3</td><td>211,988.2</td></tr><tr><td>Provision for taxes</td><td>(22,442.0)</td><td>(29,852.1)</td><td>(33,836.8)</td><td>(40,277.8)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>103,877.0</td><td>124,889.9</td><td>144,251.5</td><td>171,710.4</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>101,832.0</td><td>129,372.9</td><td>144,251.5</td><td>171,710.4</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>13.97</td><td>16.81</td><td>19.39</td><td>23.00</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>13.91</td><td>16.75</td><td>19.32</td><td>22.93</td></tr><tr><td>EPS (ex-ESO exp., dil.) ($)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS ($)</td><td>3.24</td><td>3.56</td><td>3.64</td><td>3.64</td></tr><tr><td>Div. payout ratio (%)</td><td>23.2</td><td>21.2</td><td>18.8</td><td>15.8</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>7,433.8</td><td>7,429.0</td><td>7,440.3</td><td>7,464.1</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>7,467.8</td><td>7,454.0</td><td>7,465.3</td><td>7,489.1</td></tr></table>

Source: Company data, GS estimates.

15mn in 2QFY), in its AI disclosure (\$37mn in ARR/+123\% yoy in 3Q, likely 42-43mn /+115\%-120\% yoy in 4Q), and in more commentary around a frontier ecosystem being built alongside frontier models.

For the stock to begin outperforming, we believe addressing overhangs will be key: a) new supply coming online, such that Azure can beat and raise even while Microsoft makes internal investments; b) more datapoints on production progress with Maia, AMD as a second source, and memory procurement strategy; c) more Copilot seat monetization alongside better user feedback and engagement. We see 12-month risk/reward as favorable at current levels and continue to view Microsoft as well positioned in our coverage to compound AI driven product cycles, from AI compute leadership to Copilot and agent orchestration at the platform and application layers.

## 1) 4Q Azure Expectations

We see a reasonable case where Microsoft reports Azure growth of 40-41% cc (a similar beat to last quarter at 1%) and guides to 40-41% cc for 4Q26 vs. the Street at 41% cc. Recall that Azure growth in any given quarter is a function of new capacity coming online, and Microsoft's strategic allocation to internal use cases vs. external customers.

Supply remains constrained but capacity has been increasing. While guidance continues to be supply driven, we are encouraged by Microsoft's ability to drive more revenue out of its existing infrastructure and by capacity continuing to come online, such that Azure growth accelerated in 3QFY and is on track to accelerate in 4Q and 1H. In particular, the Fairwater datacenter in Wisconsin is expected to scale to 2GW of capacity in 2026, although capacity will come online unevenly, which makes it challenging to track from the outside.

■ Strategic allocation of capacity towards internal use cases trades off Azure growth. Microsoft is prioritizing compute for first party applications (Copilot) and internal R&D (e.g., MAI) over short-term Azure revenue to ultimately drive greater strategic AI positioning across multiple layers of the technology stack and better returns over the medium term. Recall that in 2Q, Microsoft stated that Azure would have grown >40% (44% GSe) if it had allocated all incremental GPU capacity to Azure. We expect the company to continue making such strategic allocation decisions between internal initiatives and external customers; post a step up in LTM investment, we believe this internal mix as a % of total allocations is closer to a steady-state trajectory. Please see our February deep dive into capacity allocation here.

Exhibit 1: We estimate FY26 compute capex by use case to inform our Azure estimates  
![](images/a5b40e5761f075642adca1cc3b414d6ba7363637c1386ad16180a1a6ed5092fb.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: Our estimate of external vs. internal compute allocation  
![](images/84cf504d55806be014f24d0a7faa6953496b17e38e1717b2b7e3183d4cdd42e7.jpg)  


[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
