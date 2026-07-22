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
# Guangdong Songfa Ceramics Co (603268.SS)

Private placement's issue price finalized at Rmb146/shr, implying $2\%$ discount to base price; Buy

603268.SS 12m Price Target: Rmb200.00 Price: Rmb155.69 Upside: $28.5\%$

Post market close on July $21^{\text{st}}$ , Songfa/Hengli Heavy Industry announced the final issue price at Rmb146 per share for their private placement, with 47.9mn shares issuance to raise Rmb7bn in total. This issue price implies a $2\%$ discount to the base price of Rmb149 per share, which is derived from the average closing prices of 20 trading days before the pricing benchmark date, July $8^{\text{th}}$ 2026. By combing the feedback from our conversation with investors, we believe this issue price's small discount indicates that the investors are still optimistic on this company for the longer term, given the shares issued are required to wait for half a year to be unlocked. And it implies a $6\%$ discount to the latest closing price of Rmb156 on July $21^{\text{st}}$ .

This private placement would bring 3.0% dilution to the EPS, after considering the financing cost saved. However, the company initially proposed the private placement of Rmb7bn to finance its phase III capacity expansion on Jan 15 $^{th}$ 2026, which implies a larger dilution of 5.9% to EPS at the closing price of Rmb87.5 on Jan 15 $^{th}$ . So we believe the dilution impact has already been priced in by the market.

This private placement is to finance the phase III capacity expansion, which started operation in June-2026 and we estimate could bring 1mn CGT capacity (>30% to previous two-phase capacity). We believe the existing three-phase capacity could generate Rmb14-16bn earnings in 2027-28 at full utilization. In addition, we see further earnings upside if Hengli finalises the phase IV capacity addition, which is estimated to add another up to 100% capacity to the existing three phases, as we believe the expanded capacity would be filled by strong new ship orders.

## Investment Thesis - Guangdong Songfa Ceramics

We are Buy rated on Guangdong Songfa Ceramics, whose primary asset, Hengli Heavy Industry, appears well positioned to become

## BUY

Herbert Lu
+852-2978-0726 | herbert.lu@gs.com
GS (Asia) L.L.C.

Simon Cheung, CFA
+852-2978-6102 | simon.cheung@gs.com
GS (Asia) L.L.C.

Wing Huang
+852-2978-0415 | ying.huang@gs.com
GS (Asia) L.L.C.

## Key Data

Market cap: Rmb151.1bn / \$22.3bn  
Enterprise value: Rmb159.1bn / \$23.5bn  
3m ADTV: Rmb1.3bn / \$196.6mn  
China  
Asia Transportation  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn)</td><td>21,539.6</td><td>53,595.3</td><td>72,112.1</td><td>74,561.9</td></tr><tr><td>EBITDA (Rmb mn)</td><td>4,104.8</td><td>12,397.0</td><td>18,570.1</td><td>20,456.6</td></tr><tr><td>EPS (Rmb)</td><td>2.73</td><td>9.51</td><td>14.80</td><td>16.67</td></tr><tr><td>P/E (X)</td><td>17.8</td><td>16.4</td><td>10.5</td><td>9.3</td></tr><tr><td>P/B (X)</td><td>5.0</td><td>8.1</td><td>4.7</td><td>3.2</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.6</td><td>1.0</td><td>1.1</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>1.8</td><td>0.6</td><td>(0.4)</td><td>(1.0)</td></tr><tr><td>CROCI (%)</td><td>28.5</td><td>40.9</td><td>53.6</td><td>58.2</td></tr><tr><td>FCF yield (%)</td><td>(24.0)</td><td>0.4</td><td>9.8</td><td>9.9</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>1.13</td><td>2.53</td><td>2.71</td><td>3.14</td></tr></table>

GS Factor Profile

![](images/b0cc0358e994696454a2e45d8319aca4d7abedb417c941d46398c4c27f95b1f8.jpg)  
Source: Company data, GS estimates. See disclosures for details.

# Guangdong Songfa Ceramics Co (603268.SS)

Cash Flow (Rmb mn)  
Rating since Apr 2, 2026  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>17.8</td><td>16.4</td><td>10.5</td><td>9.3</td></tr><tr><td>P/B (X)</td><td>5.0</td><td>8.1</td><td>4.7</td><td>3.2</td></tr><tr><td>FCF yield (%)</td><td>(24.0)</td><td>0.4</td><td>9.8</td><td>9.9</td></tr><tr><td>EV/EBITDAR (X)</td><td>13.6</td><td>12.8</td><td>7.8</td><td>6.4</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>13.3</td><td>12.7</td><td>7.8</td><td>6.4</td></tr><tr><td>CROCI (%)</td><td>28.5</td><td>40.9</td><td>53.6</td><td>58.2</td></tr><tr><td>ROE (%)</td><td>41.7</td><td>65.6</td><td>56.5</td><td>41.0</td></tr><tr><td>Net debt/equity (%)</td><td>90.8</td><td>42.7</td><td>(18.2)</td><td>(41.3)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>77.6</td><td>36.9</td><td>(21.3)</td><td>(43.2)</td></tr><tr><td>Interest cover (X)</td><td>6.0</td><td>14.9</td><td>26.5</td><td>46.2</td></tr><tr><td>Days inventory outst, sales</td><td>59.5</td><td>55.3</td><td>61.0</td><td>64.2</td></tr><tr><td>Receivable days</td><td>3.0</td><td>1.5</td><td>1.8</td><td>2.0</td></tr><tr><td>Days payable outstanding</td><td>254.1</td><td>222.3</td><td>260.8</td><td>286.0</td></tr><tr><td>DuPont ROE (%)</td><td>28.1</td><td>49.4</td><td>44.7</td><td>34.5</td></tr><tr><td>Turnover (X)</td><td>0.4</td><td>0.6</td><td>0.7</td><td>0.6</td></tr><tr><td>Leverage (X)</td><td>5.2</td><td>4.6</td><td>3.3</td><td>2.5</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>21,316.7</td><td>29,953.4</td><td>29,549.6</td><td>30,793.6</td></tr><tr><td>Average capital employed (Rmb)</td><td>10,909.9</td><td>21,184.4</td><td>25,437.2</td><td>25,960.5</td></tr><tr><td>BVPS (Rmb)</td><td>9.74</td><td>19.25</td><td>33.10</td><td>48.29</td></tr></table>

Income Statement (Rmb mn)

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>277.6</td><td>148.8</td><td>34.5</td><td>3.4</td></tr><tr><td>EBITDA growth</td><td>595.4</td><td>202.0</td><td>49.8</td><td>10.2</td></tr><tr><td>EPS growth</td><td>1,083.1</td><td>247.9</td><td>55.6</td><td>12.6</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>55.6</td><td>12.6</td></tr><tr><td>EBIT margin</td><td>16.7</td><td>22.0</td><td>24.3</td><td>26.0</td></tr><tr><td>EBITDA margin</td><td>19.1</td><td>23.1</td><td>25.8</td><td>27.4</td></tr><tr><td>Net income margin</td><td>12.3</td><td>17.2</td><td>19.9</td><td>21.7</td></tr></table>

![](images/dbbed644467ba88c934de73dd15d54f1d6bbb0642b2f3f68ba2b032b38e2dba2.jpg)  
Price Performance

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>21,539.6</td><td>53,595.3</td><td>72,112.1</td><td>74,561.9</td></tr><tr><td>Cost of goods sold</td><td>(17,223.7)</td><td>(40,472.4)</td><td>(53,134.5)</td><td>(53,689.1)</td></tr><tr><td>SG&amp;A</td><td>(710.3)</td><td>(1,346.1)</td><td>(1,448.9)</td><td>(1,498.1)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>4,104.8</td><td>12,397.0</td><td>18,570.1</td><td>20,456.6</td></tr><tr><td>Depreciation &amp; amortization</td><td>(499.3)</td><td>(620.2)</td><td>(1,041.4)</td><td>(1,082.0)</td></tr><tr><td>EBIT</td><td>3,605.6</td><td>11,776.8</td><td>17,528.7</td><td>19,374.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>(556.9)</td><td>(754.0)</td><td>(623.0)</td><td>(336.7)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>3,181.3</td><td>11,068.5</td><td>16,905.7</td><td>19,037.9</td></tr><tr><td>Provision for taxes</td><td>(526.7)</td><td>(1,832.4)</td><td>(2,535.9)</td><td>(2,855.7)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>2,654.6</td><td>9,236.2</td><td>14,369.8</td><td>16,182.2</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>2,654.6</td><td>9,236.2</td><td>14,369.8</td><td>16,182.2</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>2.73</td><td>9.51</td><td>14.80</td><td>16.67</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>2.73</td><td>9.51</td><td>14.80</td><td>16.67</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>2.73</td><td>9.51</td><td>14.80</td><td>16.67</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>2.73</td><td>9.51</td><td>14.80</td><td>16.67</td></tr><tr><td>DPS (Rmb)</td><td>-</td><td>0.95</td><td>1.48</td><td>1.67</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>10.0</td><td>10.0</td><td>10.0</td></tr></table>

Source: FactSet. Price as of 21 Jul 2026 close.

Balance Sheet (Rmb mn)

<table><tr><td colspan="5">Balance Sheet (Kmb mln)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>7,215.2</td><td>7,814.2</td><td>16,546.2</td><td>25,459.1</td></tr><tr><td>Accounts receivable</td><td>122.5</td><td>304.7</td><td>410.0</td><td>423.9</td></tr><tr><td>Inventory</td><td>5,175.2</td><td>11,051.9</td><td>13,053.8</td><td>13,190.1</td></tr><tr><td>Other current assets</td><td>16,519.6</td><td>32,581.0</td><td>42,179.6</td><td>44,103.0</td></tr><tr><td>Total current assets</td><td>29,032.5</td><td>51,751.9</td><td>72,189.6</td><td>83,176.1</td></tr><tr><td>Net PP&amp;E</td><td>18,136.7</td><td>31,484.3</td><td>31,718.9</td><td>31,921.5</td></tr><tr><td>Net intangibles</td><td>2,076.4</td><td>2,088.9</td><td>2,101.9</td><td>2,115.4</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>146.5</td><td>146.5</td><td>146.5</td><td>146.5</td></tr><tr><td>Total assets</td><td>49,392.0</td><td>85,471.5</td><td>106,156.9</td><td>117,359.5</td></tr><tr><td>Accounts payable</td><td>15,216.6</td><td>34,092.8</td><td>41,847.5</td><td>42,284.3</td></tr><tr><td>Short-term debt</td><td>10,908.2</td><td>10,908.2</td><td>7,908.2</td><td>4,908.2</td></tr><tr><td>Short-term lease liabilities</td><td>217.7</td><td>190.8</td><td>170.2</td><td>154.9</td></tr><tr><td>Other current liabilities</td><td>5,497.1</td><td>13,464.6</td><td>18,067.1</td><td>18,676.0</td></tr><tr><td>Total current liabilities</td><td>31,839.6</td><td>58,656.4</td><td>67,992.9</td><td>66,023.2</td></tr><tr><td>Long-term debt</td><td>3,643.6</td><td>3,797.9</td><td>1,797.9</td><td>297.9</td></tr><tr><td>Long-term lease liabilities</td><td>1,032.2</td><td>904.5</td><td>807.0</td><td>734.1</td></tr><tr><td>Other long-term liabilities</td><td>3,424.5</td><td>3,424.5</td><td>3,424.5</td><td>3,424.5</td></tr><tr><td>Total long-term liabilities</td><td>8,100.3</td><td>8,126.9</td><td>6,029.4</td><td>4,456.5</td></tr><tr><td>Total liabilities</td><td>39,939.9</td><td>66,783.3</td><td>74,022.4</td><td>70,479.7</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>9,452.1</td><td>18,688.3</td><td>32,134.5</td><td>46,879.7</td></tr><tr><td>Minority interest</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total liabilities &amp; equity</td><td>49,392.0</td><td>85,471.5</td><td>106,156.9</td><td>117,359.5</td></tr><tr><td>Net debt, adjusted</td><td>7,336.6</td><td>6,891.8</td><td>(6,840.2)</td><td>(20,253.1)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>2,654.6</td><td>9,236.2</td><td>14,369.8</td><td>16,182.2</td></tr><tr><td>D&amp;A add-back</td><td>499.3</td><td>620.2</td><td>1,041.4</td><td>1,082.0</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(5,217.9)</td><td>4,723.4</td><td>651.4</td><td>(1,027.9)</td></tr><tr><td>Other operating cash flow</td><td>334.8</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>(1,729.3)</td><td>14,579.7</td><td>16,062.6</td><td>16,236.3</td></tr><tr><td>Capital expenditures</td><td>(9,630.5)</td><td>(13,980.3)</td><td>(1,289.0)</td><td>(1,298.1)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>21.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(34.2)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(9,643.3)</td><td>(13,980.3)</td><td>(1,289.0)</td><td>(1,298.1)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>(923.6)</td><td>(1,437.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>10,172.4</td><td>154.3</td><td>(5,000.0)</td><td>(4,500.0)</td></tr><tr><td>Other financing cash flows</td><td>6,043.6</td><td>(154.7)</td><td>(118.0)</td><td>(88.3)</td></tr><tr><td>Cash flow from financing</td><td>16,216.0</td><td>(0.4)</td><td>(6,041.6)</td><td>(6,025.3)</td></tr><tr><td>Total cash flow</td><td>4,843.5</td><td>599.0</td><td>8,732.0</td><td>8,912.9</td></tr><tr><td>Free cash flow</td><td>(11,359.8)</td><td>599.4</td><td>14,773.6</td><td>14,938.2</td></tr></table>

Source: Company data, GS estimates.

the second-largest shipbuilder globally by 2027E (GSe). We expect Hengli to be a major capacity addition player with a 29% CAGR in 2025-27E, factoring in the completion of its phase III yard, vs. a 3% CAGR for global peers. We expect this to drive its capacity market share to 7% by end-2026E and reduce its orderbook cover years to 2.7x (vs. global / China avg 3.6x/4.0x), one of the lowest among global major shipyards. On the other hand, we expect tanker super-cycle and an aging fleet to continue to bring new tanker orders, driving the orderbook to rise by c.50% to US\$39bn. Risks: Delays in ship delivery or new capacity release; Higher-than-expected steel prices;

Less-than-expected new order wins; Lower-than-expected ASP;

Stronger-than-expected RMB appreciation vs. USD; Faster-than-expected capacity expansion from other shipyards. Key catalysts: Earnings uptrend and new order wins.

## Price Target Risks and Methodology - Guangdong Songfa Ceramics Co

Our 12-m target price of Rmb200/share is based on a 2028E P/E of 12x, based on the average of Chinese and Korean shipyards. Risks: Delays in ship delivery or new capacity release; Higher-than-expected steel prices; Less-than-expected new order wins; Lower-than-expected ASP; Stronger-than-expected RMB appreciation vs. USD; Faster-than-expected capacity expansion from other shipyards.

## Disclosure Appendix

## Reg AC

We, Herbert Lu and Wing Huang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Herbert Lu GS (Asia) L.L.C., Simon Cheung, CFA GS (Asia) L.L.C., Wing Huang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four 

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
