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
NIO INC. (NIO/9866.HK)

# Industry-leading growth & premium margin profile with attractive valuation; upgrade to Buy from Neutral

We upgrade Nio to Buy with 12-month DCF-based target prices of US\$7.0/HK\$55, implying 46%/42% upside potential. Among our coverage, we expect Nio to not only deliver one of the fastest volume growth, but also a premium margin profile and strong profit/FCF turn-around in 2026E. This is supported by the company's successful turnaround with the launch of new ES8/ES9 (gaining No.1 position with 39% market share in the Rmb400k+ NEV segment), together with leading brand power (evidenced by top Net Promoter Score), strengthening its position in the premium NEV market, which we believe creates a higher competitive moat and is more difficult to displace by competitors. Looking ahead, we believe the company can apply similar strategy to its 5 series and 6 series models (priced between Rmb200k-400k) and rejuvenate the sales volume of these models in 2027E and beyond, further solidifying its positioning in the premium market and driving continued market share gain.

Despite the domestic NEV market growth of $-14\%$ yoy in 1H26, Nio expanded its volume by $+67\%$ yoy. For 2026E full year, we model volume/revenue growth of $+43\% / +60\%$ yoy, and non-GAAP net profit of Rmb1.6bn (vs. loss of Rmb12.4bn in 2025), we also expect free cash flow to meaningfully improve from Rmb-3.1bn in 2025 to Rmb12.1bn in 2026E. However, shares are down $-6\%$ YTD and $-32\%$ from its recent peak in Apr 2026, which is disconnected from the companies improving fundamentals, in our view. Compared with pure-NEV peers under our coverage, Nio is also trading at a $25\% / 29\%$ discount on 2026E/27E P/S and $17\%$ discount on 2027E P/E, which we see as attractive given its near term product momentum and strong growth. Catalysts include ramp-up for ES8 five-seater version delivery, profit improvement in earnings results.

Where are we different: Our 2026E-2028E earnings estimate are $30\%$ above Visible Alpha consensus (partly due to low base), mainly on higher revenue and lower opex as we believe the company's premium brand power could support more stabilized pricing and more efficient marketing spending going forward.

Estimates and TP changes: We raise our 2026E-2028E earnings estimates by 1%-9%, mainly on higher gross margin from strong sales of ES8/ES9. Accordingly, our 12-month DCF-based target prices increase by 6% to US\$7.0/HK\$55, implying 46%/42% upside potential. We upgrade Nio to Buy (from Neutral). Risks: lower sales volume, exacerbated price competition, higher cost inflation.

Tina Hou  
+86(21)2401-8694 |  
tina.hou@goldmansachs.cn  
GS (China) Securities  
Company Limited

Jenny Du  
+86(21)2401-8978 |  
jenny.x.du@goldmansachs.cn  
GS (China) Securities  
Company Limited

Exhibit 1: Nio financial summary

<table><tr><td>Profit model (Rmb mn)</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>87,488</td><td>140,339</td><td>163,491</td><td>175,745</td></tr><tr><td>Cost of goods sold</td><td>(75,572)</td><td>(115,670)</td><td>(133,960)</td><td>(143,817)</td></tr><tr><td>SG&amp;A</td><td>(16,088)</td><td>(15,588)</td><td>(17,388)</td><td>(18,688)</td></tr><tr><td>R&amp;D</td><td>(10,605)</td><td>(10,130)</td><td>(10,130)</td><td>(10,130)</td></tr><tr><td>Other operating profit/(expense)</td><td>736</td><td>736</td><td>736</td><td>736</td></tr><tr><td>EBITDA</td><td>(6,895)</td><td>7,874</td><td>12,008</td><td>14,108</td></tr><tr><td>Depreciation &amp; amortization</td><td>7,147</td><td>8,186</td><td>9,258</td><td>10,262</td></tr><tr><td>EBIT</td><td>(14,041)</td><td>(312)</td><td>2,749</td><td>3,846</td></tr><tr><td>Interest income</td><td>762</td><td>718</td><td>908</td><td>1,039</td></tr><tr><td>Interest expense</td><td>(885)</td><td>(792)</td><td>(792)</td><td>(792)</td></tr><tr><td>Income/(loss) from uncons. subs.</td><td>(1,092)</td><td>80</td><td>40</td><td>20</td></tr><tr><td>Other non-ops income/(expense)</td><td>436</td><td>125</td><td>-</td><td>-</td></tr><tr><td>Pretax profits</td><td>(14,821)</td><td>(181)</td><td>2,905</td><td>4,113</td></tr><tr><td>Income tax</td><td>(122)</td><td>(1)</td><td>(436)</td><td>(617)</td></tr><tr><td>Minorities</td><td>(18)</td><td>(0)</td><td>4</td><td>5</td></tr><tr><td>Net income (Non-GAAP)</td><td>(12,432)</td><td>1,608</td><td>4,264</td><td>5,291</td></tr><tr><td>Earnings per ADS-basic (Non-GAAP)</td><td>(5.47)</td><td>0.71</td><td>1.88</td><td>2.33</td></tr><tr><td>DPS</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

<table><tr><td>Balance sheet (Rmb mn)</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; equivalents</td><td>45,776</td><td>57,867</td><td>66,205</td><td>73,254</td></tr><tr><td>Accounts receivable</td><td>17,473</td><td>25,498</td><td>26,758</td><td>25,595</td></tr><tr><td>Inventory</td><td>8,531</td><td>12,347</td><td>13,477</td><td>13,586</td></tr><tr><td>Other current assets</td><td>4,854</td><td>4,854</td><td>4,854</td><td>4,854</td></tr><tr><td>Total current assets</td><td>76,633</td><td>100,566</td><td>111,294</td><td>117,289</td></tr><tr><td>Net PP&amp;E</td><td>25,828</td><td>24,757</td><td>21,715</td><td>17,722</td></tr><tr><td>Net intangibles</td><td>226</td><td>221</td><td>216</td><td>210</td></tr><tr><td>Investments in securities</td><td>2,481</td><td>2,561</td><td>2,601</td><td>2,621</td></tr><tr><td>Other long-term assets</td><td>19,233</td><td>19,233</td><td>19,233</td><td>19,233</td></tr><tr><td>Total assets</td><td>124,401</td><td>147,339</td><td>155,058</td><td>157,075</td></tr><tr><td>Accounts payable</td><td>53,936</td><td>75,265</td><td>78,724</td><td>75,455</td></tr><tr><td>Short-term loans</td><td>6,856</td><td>6,856</td><td>6,856</td><td>6,856</td></tr><tr><td>Current lease liabilities</td><td>1,619</td><td>342</td><td>257</td><td>260</td></tr><tr><td>Other current liabilities</td><td>16,172</td><td>17,449</td><td>17,534</td><td>17,531</td></tr><tr><td>Total current liabilities</td><td>78,583</td><td>99,912</td><td>103,371</td><td>100,102</td></tr><tr><td>Long-term debt</td><td>8,626</td><td>8,626</td><td>8,626</td><td>8,626</td></tr><tr><td>Non-current lease liabilities</td><td>10,092</td><td>3,388</td><td>2,546</td><td>2,577</td></tr><tr><td>Other long-term liabilities</td><td>14,408</td><td>21,111</td><td>21,954</td><td>21,923</td></tr><tr><td>Total liabilities</td><td>111,709</td><td>133,038</td><td>136,497</td><td>133,228</td></tr><tr><td>Preferred shares</td><td>8,552</td><td>8,552</td><td>8,552</td><td>8,552</td></tr><tr><td>Total common equity</td><td>4,159</td><td>5,768</td><td>10,031</td><td>15,323</td></tr><tr><td>Minority interest</td><td>(19)</td><td>(19)</td><td>(22)</td><td>(27)</td></tr><tr><td>Total liabilities &amp; equity</td><td>124,401</td><td>147,339</td><td>155,058</td><td>157,075</td></tr><tr><td>BVPS</td><td>1.8</td><td>2.5</td><td>4.4</td><td>6.7</td></tr></table>

<table><tr><td>Growth &amp; margins (%)</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Sales growth</td><td>33.1%</td><td>60.4%</td><td>16.5%</td><td>7.5%</td></tr><tr><td>EBITDA growth</td><td>56.9%</td><td>214.2%</td><td>52.5%</td><td>17.5%</td></tr><tr><td>EBIT growth</td><td>35.8%</td><td>97.8%</td><td>980.7%</td><td>39.9%</td></tr><tr><td>Net income growth</td><td>39.0%</td><td>112.9%</td><td>165.1%</td><td>24.1%</td></tr><tr><td>Gross margin</td><td>13.6%</td><td>17.6%</td><td>18.1%</td><td>18.2%</td></tr><tr><td>EBITDA margin</td><td>-7.9%</td><td>5.6%</td><td>7.3%</td><td>8.0%</td></tr><tr><td>EBIT margin</td><td>-16.0%</td><td>-0.2%</td><td>1.7%</td><td>2.2%</td></tr><tr><td>Non-GAAP net margin</td><td>-14.2%</td><td>1.1%</td><td>2.6%</td><td>3.0%</td></tr></table>

<table><tr><td>Cash flow statement (Rmb mn)</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income pre-preferred dividends</td><td>(14,961)</td><td>(183)</td><td>2,473</td><td>3,501</td></tr><tr><td>D&amp;A add-back</td><td>7,147</td><td>8,186</td><td>9,258</td><td>10,262</td></tr><tr><td>Minorities interests add-back</td><td>18</td><td>0</td><td>(4)</td><td>(5)</td></tr><tr><td>Net (inc)/dec working capital</td><td>15,434</td><td>9,487</td><td>1,070</td><td>(2,216)</td></tr><tr><td>Other operating cash flow</td><td>453</td><td>2,986</td><td>(4,262)</td><td>3,868</td></tr><tr><td>Cash flow from operations</td><td>2,993</td><td>19,201</td><td>14,548</td><td>13,313</td></tr><tr><td>Capital expenditures</td><td>(6,065)</td><td>(7,110)</td><td>(6,211)</td><td>(6,264)</td></tr><tr><td>Acquisitions</td><td>(6,362)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>967</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investments</td><td>(11,460)</td><td>(7,110)</td><td>(6,211)</td><td>(6,264)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>(5,461)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Common stock issuance (repurchase)</td><td>11,855</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>435</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>6,828</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total cash flow</td><td>(1,639)</td><td>12,091</td><td>8,338</td><td>7,049</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>Ratios</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>ROIC</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Inventory days</td><td>43.7</td><td>41.2</td><td>39.0</td><td>36.7</td></tr><tr><td>Receivables days</td><td>52.1</td><td>72.9</td><td>66.3</td><td>59.7</td></tr><tr><td>Payable days</td><td>214.4</td><td>260.5</td><td>237.5</td><td>214.5</td></tr><tr><td>Total liability to asset</td><td>87.4%</td><td>89.8%</td><td>90.3%</td><td>88.0%</td></tr></table>

<table><tr><td>Valuation</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td colspan="5">Target price implied valuation</td></tr><tr><td>P/E</td><td>(9.1)</td><td>70.7</td><td>26.7</td><td>21.5</td></tr><tr><td>P/S</td><td>1.3</td><td>0.8</td><td>0.7</td><td>0.6</td></tr><tr><td>P/B</td><td>9.0</td><td>8.0</td><td>6.2</td><td>4.8</td></tr><tr><td>EV/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td colspan="5">Current share price implied valuation</td></tr><tr><td>P/E</td><td>(6.2)</td><td>48.3</td><td>18.2</td><td>14.7</td></tr><tr><td>P/S</td><td>0.9</td><td>0.6</td><td>0.5</td><td>0.4</td></tr><tr><td>P/B</td><td>6.1</td><td>5.4</td><td>4.2</td><td>3.3</td></tr><tr><td>EV/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr></table>

## (1) Successful turn-around with ES8/ES9

NIO has started to successfully refresh its product lineup since Sep 2025, highlighted by the launch and delivery of the All-New ES8 with LTM monthly sales volume of 10k+ as of June 2026, ranking No.1 among Rmb400k+ SUV segment. Following the launch of ES9 and L80 in May 2026, Nio delivered 191k units in 1H26 (+67% yoy, vs. industry NEV retail at -14%) and expanded its NEV retail market share to 3.6% in 1H26 (vs. 2.1% in 1H25). As of 1H26, the Nio brand has gained No.1 position with 39% market share in the Rmb400k+ segment.

We observe that Nio has shown consistent capability to launch more competitive models over the past four quarters, based on our product comparison framework, which identifies 4 key consumer purchasing factors, i.e. price, range, size, and autopilot. Based on our product comp analysis among Rmb400k+ top selling NEV SUVs/MPVs, we see Nio's ES8 and ES9 both rank top5 among the best-selling models (esp. ES8 ranking No.1), with competitive strengths in price and size (Exhibit 4).

Exhibit 2: NEV penetration reached $50\%$ in 1H26, among Rmb400k price segment  
![](images/cb635a0fd9bcc0151a9669b074efea9a158812ea33837f96fe866ff6836b165a.jpg)  
Source: CPCA

Exhibit 3: Nio's market share increased to $39\%$ in 1H26 from $6\%$ in 1H25, among NEV Rmb400k+ price segment  
![](images/fdd6b427f97bdbd68e6f27de5635a7213321bb6abd90a6326cd6bd7789bc561c.jpg)  
Source: CPCA

Exhibit 4: Nio ES8/ES9 product comps  
Top 10 best-selling NEV SUVs/MPVs (MSRP Rmb400k+)

<table><tr><td>OEM Model</td><td>NIO Nio ES8 EV</td><td>Geely Zeekr 9X PHEV</td><td>Seres Aito M9 EREV</td><td>Nio Nio ES9 EV</td><td>Volvo Volvo XC70 PHEV</td><td>Li Auto Li L9 EREV</td><td>SAIC Encasa PHEV</td><td>Li Auto Li MEGA EV</td><td>Volvo Zeekr 009 EV</td><td>Seres Aito M9 EV</td></tr><tr><td>Model launch date (latest facelift entry level)</td><td>Sep-25</td><td>Sep-25</td><td>Mar-25</td><td>May-26</td><td>Apr-26</td><td>May-25</td><td>Dec-25</td><td>Apr-25</td><td>Jul-24</td><td>Mar-25</td></tr><tr><td>Body type</td><td>SUV</td><td>SUV</td><td>SUV</td><td>SUV</td><td>SUV</td><td>SUV</td><td>MPV</td><td>MPV</td><td>MPV</td><td>SUV</td></tr><tr><td>Segment</td><td>D</td><td>D</td><td>D</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td></tr><tr><td>Seat</td><td>6/7</td><td>6</td><td>5/6</td><td>6-Jan</td><td>5</td><td>6</td><td>7</td><td>7</td><td>7</td><td>6</td></tr><tr><td>Powertrain</td><td>BEV</td><td>PHEV</td><td>EREV</td><td>BEV</td><td>PHEV</td><td>EREV</td><td>PHEV</td><td>BEV</td><td>BEV</td><td>EREV</td></tr><tr><td>Entry price (Rmb k)</td><td>406.8</td><td>465.9</td><td>469.8</td><td>498.0</td><td>411.9</td><td>409.8</td><td>439.9</td><td>529.8</td><td>439.0</td><td>509.8</td></tr><tr><td>Max driving range (km)</td><td>635</td><td>1,200</td><td>1,474</td><td>620</td><td>1,203</td><td>1,412</td><td>1,320</td><td>710</td><td>740</td><td>630</td></tr><tr><td>Wheelbase (mm)</td><td>3,130</td><td>3,169</td><td>3,110</td><td>3,250</td><td>2,895</td><td>3,105</td><td>3,160</td><td>3,300</td><td>3,205</td><td>3,110</td></tr><tr><td>Hardware 0-100km/h acceleration time (s)</td><td>3.97</td><td>3.9</td><td>4.9</td><td>4.3</td><td>8</td><td>5.18</td><td>5.8</td><td>5.5</td><td>6.9</td><td>4.3</td></tr><tr><td>Battery size (kWh)</td><td>102.0</td><td>55.0</td><td>52.0</td><td>102.0</td><td>21.2</td><td>52.3</td><td>40.9</td><td>102.7</td><td>108.0</td><td>100</td></tr><tr><td>Charging speed (kWh/min)</td><td></td><td>3.7</td><td>1.0</td><td></td><td>0.4</td><td>1.2</td><td>1.0</td><td>6.0</td><td>5.7</td><td>3.3</td></tr><tr><td>Continuous voice command</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Software Highway autopilot</td><td>Optional</td><td>Standard</td><td>Standard</td><td>Optional</td><td>Optional</td><td>Standard</td><td>Standard</td><td>Standard</td><td>Optional</td><td>Standard</td></tr><tr><td>Urban autopilot</td><td>Optional</td><td>Standard</td><td>Optional</td><td>Optional</td><td>Optional</td><td>Optional</td><td>Standard</td><td>Standard</td><td>None</td><td>Optional</td></tr><tr><td>Price score</td><td>10</td><td>5</td><td>4</td><td>3</td><td>8</td><td>9</td><td>6</td><td>1</td><td>7</td><td>2</td></tr><tr><td>Range score</td><td>3</td><td>6</td><td>10</td><td>1</td><td>7</td><td>9</td><td>8</td><td>4</td><td>5</td><td>2</td></tr><tr><td>Size score</td><td>5</td><td>7</td><td>3</td><td>9</td><td>1</td><td>2</td><td>6</td><td>10</td><td>8</td><td>3</td></tr><tr><td>Autopilot score</td><td>2</td><td>4</td><td>3</td><td>2</td><td>2</td><td>3</td><td>4</td><td>4</td><td>1</td><td>3</td></tr><tr><td>Sub-total score</td><td>20</td><td>22</td><td>20</td><td>15</td><td>18</td><td>23</td><td>24</td><td>19</td><td>2

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
