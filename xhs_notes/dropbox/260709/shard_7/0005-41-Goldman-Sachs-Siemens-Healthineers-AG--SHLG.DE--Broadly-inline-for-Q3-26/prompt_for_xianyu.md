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
# Siemens Healthineers AG (SHLG.DE)

Broadly inline for Q3 26 but continue to see FY27 downside risk from China Dx; Neutral

SHLG.DE 12m Price Target: €42.00 Price: €35.25 Upside: 19.1%

We sit broadly in line on Q3 consensus EBIT/EPS for Healthineers. We estimate +4.1% organic revenue growth in Q3 26 (vs 4.8% Visible Alpha Consensus) and revenue of €5,783m (-1% below consensus); our top-line estimates are below consensus across the group. We expect broad based margin pressure on Y/Y basis as a result of cost pressures and FX leading to a group adjusted EBIT margin of 15.6%; our adjusted EBIT is €899m (broadly in line with consensus).

We continue to see modest downside risk to consensus expectations in FY27 due to Diagnostics. Given this risk of further policy headwinds (Unified pricing and Hemostasis VBP; updates from China peers below) we take a more cautious view on the industry and model a shallower recovery in Diagnostics profitability in FY27e; we note consensus assumes +73% Y/Y EBIT growth in FY27e (which accounts for \~20% of group EBIT growth). GSe -4% below Visible Alpha Consensus FY27 adjust EPS, driven by Diagnostics and upward pressure on finance cost from refinancing.

Recent press on diagnostics spin could be a positive, long-dated catalyst. Recent press coverage has highlighted the possibility of a Diagnostics separation within the next 24 months, with reports indicating a valuation of approximately €6bn. On our estimates, a Diagnostics separation would be accretive to group organic growth and margins (given Diagnostics is a lower growth and margin business vs Imaging/Precision Therapy) and any cash proceeds could accelerate deleveraging.

Overall we believe that the lack of positive EPS revisions will continue to weigh on shares. Despite the technical overhang associated with Siemens AG's stake reduction, Healthineers has not seen material positive earnings revisions since December 2021. Updating for latest FX, our adj. EBIT/EPS estimates are $+1\%$ in FY26/27/28e. Based on our new estimates, Healthineers is trading on 14.5x 12m fwd P/E and 11.1x EV/EBITDA. We are Neutral rated.

NEUTRAL

Richard Felton, CFA
+44(20)7552-7872 | richard.felton@gs.com
GS International

Lauren Mitchell  
+44(20)7774-8731 | lauren.r.mitchell@gs.com  
GS International

Market cap: €39.5bn / \$45.1bn  
Enterprise value: €51.6bn / \$59.0bn  
3m ADTV: €39.0mn / \$45.3mn  
Germany  
Europe MedTech  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>Revenue (€ mn) New</td><td>23,375.0</td><td>23,840.0</td><td>25,212.6</td><td>26,717.5</td></tr><tr><td>Revenue (€ mn) Old</td><td>23,375.0</td><td>23,710.1</td><td>25,075.2</td><td>26,571.9</td></tr><tr><td>EBIT (€ mn)</td><td>3,498.0</td><td>3,367.9</td><td>3,662.4</td><td>4,061.8</td></tr><tr><td>EPS (€) New</td><td>2.39</td><td>2.27</td><td>2.38</td><td>2.65</td></tr><tr><td>EPS (€) Old</td><td>2.39</td><td>2.25</td><td>2.36</td><td>2.64</td></tr><tr><td>P/E (X)</td><td>20.7</td><td>15.5</td><td>14.8</td><td>13.3</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>2.9</td><td>3.1</td><td>3.5</td></tr><tr><td>CROCI (%)</td><td>9.4</td><td>8.0</td><td>8.3</td><td>8.7</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>2.7</td><td>2.9</td><td>2.6</td><td>2.2</td></tr><tr><td></td><td>12/25</td><td>3/26</td><td>6/26E</td><td>9/26E</td></tr><tr><td>EPS (€)</td><td>0.49</td><td>0.53</td><td>0.54</td><td>0.70</td></tr></table>

GS Factor Profile

![](images/bd166f83ff66df6adf06e5dabb3e93948f1af93c311528f3b26627b7b87586b4.jpg)  
Source: Company data, GS estimates. See disclosures for details.

Siemens Healthineers AG (SHLG.DE) Rating since Jul 12, 2023  
Ratios & Valuation

<table><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>EV/sales (X)</td><td>2.9</td><td>2.2</td><td>2.0</td><td>1.9</td></tr><tr><td>EV/EBITDAR (X)</td><td>14.2</td><td>11.9</td><td>11.0</td><td>9.9</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>14.7</td><td>12.4</td><td>11.4</td><td>10.2</td></tr><tr><td>EV/EBIT (X)</td><td>21.5</td><td>16.8</td><td>15.2</td><td>13.4</td></tr><tr><td>P/E (X)</td><td>20.7</td><td>15.5</td><td>14.8</td><td>13.3</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>2.9</td><td>3.1</td><td>3.5</td></tr><tr><td>EV/GCI (X)</td><td>1.7</td><td>1.2</td><td>1.2</td><td>1.1</td></tr><tr><td>CROCI (%)</td><td>9.4</td><td>8.0</td><td>8.3</td><td>8.7</td></tr><tr><td>ROIC (%)</td><td>9.2</td><td>9.1</td><td>9.5</td><td>10.3</td></tr><tr><td>ROA (%)</td><td>5.3</td><td>5.2</td><td>5.4</td><td>5.9</td></tr><tr><td>Days inventory outst, sales</td><td>64.9</td><td>65.2</td><td>65.0</td><td>64.5</td></tr><tr><td>Asset turnover (X)</td><td>5.1</td><td>4.7</td><td>4.3</td><td>4.0</td></tr><tr><td>Capex/D&amp;A (%)</td><td>55.6</td><td>84.5</td><td>82.6</td><td>80.2</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>68.0</td><td>63.1</td><td>57.2</td><td>50.2</td></tr><tr><td>EBIT interest cover (X)</td><td>7.9</td><td>6.7</td><td>6.5</td><td>7.3</td></tr><tr><td>FCF cover of dividends (X)</td><td>2.3</td><td>1.6</td><td>1.7</td><td>1.7</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>Total revenue growth</td><td>4.5</td><td>2.0</td><td>5.8</td><td>6.0</td></tr><tr><td>EBITDA growth</td><td>10.4</td><td>(9.4)</td><td>7.8</td><td>9.8</td></tr><tr><td>EBIT growth</td><td>12.4</td><td>(2.4)</td><td>9.3</td><td>11.5</td></tr><tr><td>Net inc. growth</td><td>7.6</td><td>(5.2)</td><td>4.8</td><td>11.7</td></tr><tr><td>EPS growth</td><td>7.6</td><td>(5.2)</td><td>4.8</td><td>11.7</td></tr><tr><td>DPS growth</td><td>12.1</td><td>(4.0)</td><td>6.3</td><td>14.0</td></tr></table>

Balance Sheet (€ mn)

Price Performance  
![](images/abba591fb42b7974fab42a768980979aac36e84b26c9a42e01fb95ae9605089d.jpg)

<table><tr><td colspan="5">Balance Sheet (€ mln)</td></tr><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>2,175.0</td><td>2,501.0</td><td>3,022.1</td><td>3,777.1</td></tr><tr><td>Accounts receivable</td><td>4,681.0</td><td>4,774.1</td><td>5,049.0</td><td>5,350.4</td></tr><tr><td>Inventory</td><td>4,135.0</td><td>4,380.4</td><td>4,602.2</td><td>4,844.7</td></tr><tr><td>Other current assets</td><td>3,108.0</td><td>3,145.4</td><td>3,255.6</td><td>3,376.5</td></tr><tr><td>Total current assets</td><td>14,099.0</td><td>14,800.9</td><td>15,929.0</td><td>17,348.7</td></tr><tr><td>Net PP&amp;E</td><td>4,713.0</td><td>5,495.2</td><td>6,273.6</td><td>7,052.3</td></tr><tr><td>Net intangibles</td><td>23,629.0</td><td>23,141.4</td><td>22,637.2</td><td>22,108.8</td></tr><tr><td>Total investments</td><td>19.0</td><td>8.8</td><td>(2.0)</td><td>(13.4)</td></tr><tr><td>Other long-term assets</td><td>1,910.0</td><td>1,912.0</td><td>1,914.2</td><td>1,916.5</td></tr><tr><td>Total assets</td><td>44,370.0</td><td>45,358.4</td><td>46,751.9</td><td>48,413.0</td></tr><tr><td>Accounts payable</td><td>2,296.0</td><td>2,326.4</td><td>2,444.2</td><td>2,573.0</td></tr><tr><td>Short-term debt</td><td>102.0</td><td>102.0</td><td>102.0</td><td>102.0</td></tr><tr><td>Short-term lease liabilities</td><td>166.0</td><td>166.0</td><td>166.0</td><td>166.0</td></tr><tr><td>Other current liabilities</td><td>10,080.0</td><td>10,152.4</td><td>10,366.2</td><td>10,600.6</td></tr><tr><td>Total current liabilities</td><td>12,644.0</td><td>12,746.8</td><td>13,078.4</td><td>13,441.6</td></tr><tr><td>Long-term debt</td><td>487.0</td><td>487.0</td><td>487.0</td><td>487.0</td></tr><tr><td>Long-term lease liabilities</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term liabilities</td><td>13,148.0</td><td>13,148.0</td><td>13,148.0</td><td>13,148.0</td></tr><tr><td>Total long-term liabilities</td><td>13,635.0</td><td>13,635.0</td><td>13,635.0</td><td>13,635.0</td></tr><tr><td>Total liabilities</td><td>26,279.0</td><td>26,381.8</td><td>26,713.4</td><td>27,076.6</td></tr><tr><td>Preferred shares</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total common equity</td><td>18,040.0</td><td>18,894.4</td><td>19,914.3</td><td>21,155.1</td></tr><tr><td>Minority interest</td><td>51.0</td><td>82.1</td><td>124.2</td><td>181.2</td></tr><tr><td>Total liabilities &amp; equity</td><td>44,370.0</td><td>45,358.4</td><td>46,751.9</td><td>48,413.0</td></tr><tr><td>Capital employed</td><td>18,680.0</td><td>19,565.6</td><td>20,627.5</td><td>21,925.3</td></tr><tr><td>Adj for unfunded pensions &amp; GW</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(1.9)%</td><td>(23.9)%</td><td>(24.4)%</td></tr><tr><td>Rel. to the FTSE World Europe (EUR)</td><td>(10.6)%</td><td>(29.0)%</td><td>(36.7)%</td></tr></table>

<table><tr><td colspan="5">Cash Flow (€ mn)</td></tr><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>Net income</td><td>2,168.0</td><td>2,082.0</td><td>2,212.5</td><td>2,522.1</td></tr><tr><td>D&amp;A add-back</td><td>1,296.0</td><td>954.5</td><td>985.4</td><td>1,025.0</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(93.0)</td><td>(272.9)</td><td>(274.8)</td><td>(301.0)</td></tr><tr><td>Other operating cash flow</td><td>162.0</td><td>54.7</td><td>104.4</td><td>63.0</td></tr><tr><td>Cash flow from operations</td><td>3,533.0</td><td>2,818.3</td><td>3,027.5</td><td>3,309.1</td></tr><tr><td>Capital expenditures</td><td>(818.0)</td><td>(953.6)</td><td>(958.1)</td><td>(961.8)</td></tr><tr><td>Acquisitions</td><td>(216.0)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>3.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>126.0</td><td>(2.0)</td><td>(2.2)</td><td>(2.3)</td></tr><tr><td>Cash flow from investing</td><td>(905.0)</td><td>(955.6)</td><td>(960.2)</td><td>(964.1)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(1,079.0)</td><td>(1,196.5)</td><td>(1,150.6)</td><td>(1,224.3)</td></tr><tr><td>Inc/(dec) in debt</td><td>(185.0)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(1,775.0)</td><td>(340.2)</td><td>(395.6)</td><td>(365.7)</td></tr><tr><td>Cash flow from financing</td><td>(3,039.0)</td><td>(1,536.6)</td><td>(1,546.2)</td><td>(1,590.0)</td></tr><tr><td>Total cash flow</td><td>(508.0)</td><td>326.0</td><td>521.1</td><td>755.0</td></tr><tr><td>Reinvestment rate (%)</td><td>22.6</td><td>30.8</td><td>29.0</td><td>26.6</td></tr></table>

Source: Company data, GS estimates.  
Source: FactSet. Price as of 7 Jul 2026 close.

Income Statement (€ mn)

<table><tr><td></td><td>9/25</td><td>9/26E</td><td>9/27E</td><td>9/28E</td></tr><tr><td>Total revenue</td><td>23,375.0</td><td>23,840.0</td><td>25,212.6</td><td>26,717.5</td></tr><tr><td>Total operating expenses</td><td>(18,232.0)</td><td>(18,720.0)</td><td>(19,664.1)</td><td>(20,639.8)</td></tr><tr><td>R&amp;D</td><td>(1,958.0)</td><td>(2,008.9)</td><td>(2,137.1)</td><td>(2,278.1)</td></tr><tr><td>Other operating inc./(exp.)</td><td>(31.0)</td><td>(31.6)</td><td>(46.4)</td><td>(49.1)</td></tr><tr><td>EBITDA</td><td>4,451.0</td><td>4,034.0</td><td>4,350.4</td><td>4,775.5</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(1,296.0)</td><td>(954.5)</td><td>(985.4)</td><td>(1,025.0)</td></tr><tr><td>EBIT</td><td>3,155.0</td><td>3,079.5</td><td>3,364.9</td><td>3,750.5</td></tr><tr><td>Net interest inc./(exp.)</td><td>(301.0)</td><td>(340.0)</td><td>(395.1)</td><td>(365.1)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>2,854.0</td><td>2,739.5</td><td>2,969.8</td><td>3,385.4</td></tr><tr><td>Provision for taxes</td><td>(686.0)</td><td>(657.5)</td><td>(757.3)</td><td>(863.3)</td></tr><tr><td>Minority interest</td><td>(23.0)</td><td>(31.1)</td><td>(42.1)</td><td>(57.0)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>2,145.0</td><td>2,050.9</td><td>2,170.4</td><td>2,465.2</td></tr><tr><td>Post-tax exceptionals</td><td>531.7</td><td>486.9</td><td>489.7</td><td>506.0</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>2,676.7</td><td>2,537.8</td><td>2,660.1</td><td>2,971.2</td></tr><tr><td>EPS (basic, pre-except) (€)</td><td>1.92</td><td>1.83</td><td>1.94</td><td>2.20</td></tr><tr><td>EPS (basic, post-except) (€)</td><td>2.39</td><td>2.27</td><td>2.38</td><td>2.65</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>1,119.5</td><td>1,119.5</td><td>1,119.5</td><td>1,119.5</td></tr><tr><td>Tax rate (%)</td><td>24.0</td><td>24.0</td><td>25.5</td><td>25.5</td></tr><tr><td>Common dividends declared</td><td>1,192.4</td><td>1,145.1</td><td>1,216.9</td><td>1,387.2</td></tr><tr><td>DPS (€)</td><td>1.07</td><td>1.02</td><td>1.09</td><td>1.24</td></tr></table>

## We sit slightly below consensus on Q3 26 sales, but in line on EBIT/EPS

We estimate 4.1% organic revenue growth in Q3 26 (vs 4.8% consensus) driving €5,783m sales (-1% below consensus). We sit below consensus divisional organic sales growth expectations for all divisions; Imaging/Precision Therapy we sit -60/80bps below and -120bps below for Diagnostics. Additionally, we expect a y/y margin decline in Q3 (GSe 15.6% adj. EBIT margin, -130bps y/y and broadly in line with consensus). While we do not expect material impacts from tariffs (in the base as of Q3 26) we expect margins to decline across all divisions due to FX and additional cost inflation.

In Imaging we forecast +5% organic growth in Q3 (-70bps below consensus) and €3,056m sales, -1% below consensus. While within the stated FY26 range of MSD divisional growth, we expect Imaging growth to decelerate in Q3 (+6% growth in Q2 26) on a tough comp (+12% in Q3 25). We forecast €694m adj. EBIT in Q3 (+1% vs consensus) driving 22.7% adj. EBIT margin (-100bps y/y, +30bps vs consensus) as FX and incremental supply chain inflation weigh on margins against a particularly favourable prior-year business mix in Q3 2025.

In Diagnostics we forecast a -3% sales decline (-120bps below consensus) in Q3 driving €1,008m sales, -1% below consensus. We note this decline is less than the 5% decline in Diagnostics in H1 as China headwinds ease but do not abate, in our view (see note here). Our adj. EBIT margin estimate of 3% (down >600bps y/y, -50bps below consensus) contemplates a similar contraction in margin as Q2 (\~5pp) as China/top-line headwinds continue to weigh on profitability, as well as a tougher comp (>9% margin Q3 25).

For Precision Therapy we forecast +7% organic growth in Q3 (-80bps below consensus) driving €1,702m sales, -1% below consensus. We expect this acceleration in growth (+5% in Q2 26) to be driven by Advanced Therapies (new portfolio launching in 2026) after a softer start to the year. We expect adj. EBIT margins of 14% (-40bps y/y, +20bps vs consensus) to be down y/y driven by FX and supply chain inflation; our adj. EBIT expectation of €238m is +1% above consensus.

Exhibit 1: We sit slightly below consensus on sales, but broadly inline on adj. EBIT/EPS in Q3 26 GS vs Visible Alpha Consensus

<table><tr><td></td><td></td><td>Gse Q3 26e</td><td>VA Consensus Q3 26e</td><td>Gse vs Consensus Q3 26e</td></tr><tr><td colspan="5">Group</t

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
