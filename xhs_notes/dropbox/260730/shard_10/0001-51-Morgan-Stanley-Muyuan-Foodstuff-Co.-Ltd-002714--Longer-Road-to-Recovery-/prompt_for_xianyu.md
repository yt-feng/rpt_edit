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
# Muyuan Foodstuff Co. Ltd | Asia Pacific

# Longer Road to Recovery

China/Hong Kong Consumer | China

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (002714.SZ)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb57.00</td><td>Rmb48.00</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (2714.HK)</td><td></td><td></td></tr><tr><td>Price Target</td><td>HK$58.00</td><td>HK$49.00</td></tr></table>

We now expect a seasonal hog price rebound in 3Q26 and push our cyclical recovery assumption into 2027. Though we're lowering F2026 earnings estimates, we still see Muyuan as the best-positioned industry leader given its structural cost advantage. We stay OW.

2026 outlook – recovery delayed by slower supply rationalisation: Hog prices remained weaker than expected in 2Q26, with spot prices falling below Rmb10/kg. While losses have persisted even with the recent rebound to \~Rmb10.1/kg, productivity gains (higher MSY) have largely offset breeding sow reductions for output, delaying the expected supply tightening. We now forecast average industry hog prices of Rmb11/kg (-23% YoY) in 2026, followed by a modest recovery to Rmb13.6/kg (+23% YoY) in 2027 with more meaningful rebound in hog prices into 3Q27.

Structural advantages remain intact: Although lower hog prices and elevated feed costs will continue to weigh on near-term earnings, Muyuan remains best positioned given its industry-leading cost structure and biological performance (MSY of 25 versus the industry average of 20). We forecast complete hog raising costs of Rmb11.5/kg in 2026. We therefore lower our hog production gross profit forecasts to Rmb1.4bn in 2026 and Rmb27.9bn in 2027 (from Rmb21.8bn and Rmb34.4bn previously), mainly reflecting weaker hog price assumptions. This implies unit gross profit estimates for hog production at Rmb0.1/kg in 2026 and Rmb2.9/kg in 2027.

Changes to earnings estimates and price targets: We lower our 2026 earnings estimate to a loss of Rmb0.72/share and cut 2027e EPS 22%, reflecting lower hog price assumptions and a slower industry recovery. Accordingly, we reduce our A-share and H-share price targets to Rmb48 and HK\$49 (from Rmb57 and HK\$58), respectively. We now value Muyuan at 13x 2027e P/E, versus 18x 2026e P/E previously, to reflect a more prolonged destocking cycle. The revised multiple is broadly in line with valuation levels seen during the late stage of previous destocking cycles, It remains slightly below the stock's historical average trading multiple since 2018.

1H26 preliminary results: Muyuan guided for 1H26 net losses of Rmb5.7-6.7bn, driven by a 28% YoY decline in realised hog ASP, to approximately Rmb10.4/kg. Based on our 2026 estimates, the guidance implies 2H26 net profit of Rmb1.5-2.5bn.

Key points to watch: 1) the company's destocking process in 2H26 and reflection to hog price level into the peak demand season in 3Q; 2) Muyuan's cost efficiency.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td>Lillian Lou</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Lillian.Lou@morganstanley.com</td><td>+852 2848-6502</td></tr><tr><td>Charlotte Zhou</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Charlotte.Zhou@morganstanley.com</td><td>+852 3963-2111</td></tr><tr><td>Carlos Liu, CFA</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Carlos.Liu@morganstanley.com</td><td>+852 2848-5206</td></tr></table>

## Asia Summer School 2026

![](images/a11f510ebaef13f6a458fc8600828b54049b69c1e813cb5b61c677ba63eae605.jpg)  
Muyuan Foodstuff Co. Ltd (002714.SZ, 002714 CH)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>Rmb48.00</td></tr><tr><td>Up/downside to price target (%)</td><td>22</td></tr><tr><td>Shr price, close (Jul 28, 2026)</td><td>Rmb39.30</td></tr><tr><td>52-Week Range</td><td>Rmb59.68-31.81</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>5,763</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb390,494</td></tr><tr><td>EV, curr (mn)</td><td>Rmb438,268</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb2,135</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>2.84</td><td>(0.72)</td><td>3.68</td><td>4.61</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>2.63</td><td>4.74</td><td>5.94</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>144,145</td><td>110,918</td><td>135,288</td><td>143,339</td></tr><tr><td>EBITDA (Rmb mn)</td><td>33,301</td><td>12,621</td><td>38,702</td><td>44,185</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>15,487</td><td>(4,156)</td><td>21,212</td><td>26,585</td></tr><tr><td>P/E</td><td>17.8</td><td>NM</td><td>10.7</td><td>8.5</td></tr><tr><td>P/BV</td><td>3.6</td><td>2.6</td><td>2.3</td><td>2.1</td></tr><tr><td>RNOA (%)</td><td>11.4</td><td>(1.6)</td><td>14.1</td><td>19.6</td></tr><tr><td>ROE (%)</td><td>21.5</td><td>(5.3)</td><td>24.6</td><td>27.1</td></tr><tr><td>EV/EBITDA</td><td>9.8</td><td>33.7</td><td>10.3</td><td>8.5</td></tr><tr><td>FCF yld ratio (%)**</td><td>7.1</td><td>(0.0)</td><td>16.2</td><td>16.4</td></tr><tr><td>Leverage (EOP) (%)</td><td>60.1</td><td>39.5</td><td>6.8</td><td>(13.7)</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
e = MS estimates

## Read Also:

## Muyuan Foodstuff Co. Ltd: 1Q26 Results: Loss Making As Industry Accelerates Destocking (21 Apr 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## AlphaSignals Earnings Preview

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Muyuan Foodstuff Co. Ltd 002714.SZ</td></tr><tr><td colspan="2">Average selling price, Averge unit cost ↑ Likely upside surprise</td><td>↓ Meaningful revision lower</td></tr><tr><td colspan="3">*Likely impact to consensus EPS is for the next 12 monthsSource:</td></tr></table>

## Muyuan: Financials

Exhibit 1: Muyuan: Financial Summary

<table><tr><td colspan="6">Income Statement</td></tr><tr><td>FY-end Dec (RMB mn)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Core Sales</td><td>137,947</td><td>144,145</td><td>110,918</td><td>135,288</td><td>143,339</td></tr><tr><td>Hog Production</td><td>136,229</td><td>140,207</td><td>104,796</td><td>129,547</td><td>136,989</td></tr><tr><td>Feed/Trade Business</td><td>1,432</td><td>3,342</td><td>3,442</td><td>3,545</td><td>3,616</td></tr><tr><td>Slaughtering</td><td>24,274</td><td>45,228</td><td>53,504</td><td>65,222</td><td>74,614</td></tr><tr><td>Others</td><td>447</td><td>1,147</td><td>1,181</td><td>1,217</td><td>1,241</td></tr><tr><td>Cost of good sold</td><td>(109,319)</td><td>(118,461)</td><td>(107,949)</td><td>(106,381)</td><td>(109,333)</td></tr><tr><td>Gross Profit</td><td>28,628</td><td>25,684</td><td>2,968</td><td>28,906</td><td>34,005</td></tr><tr><td>Hog Production</td><td>28,513</td><td>24,236</td><td>1,401</td><td>27,856</td><td>32,440</td></tr><tr><td>Slaughtering</td><td>(162)</td><td>(551)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>277</td><td>1,998</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Operating expenses</td><td>(6,175)</td><td>(6,865)</td><td>(5,437)</td><td>(5,960)</td><td>(6,118)</td></tr><tr><td>Selling &amp; Distribution Exp</td><td>(1,096)</td><td>(1,295)</td><td>(1,222)</td><td>(1,225)</td><td>(1,245)</td></tr><tr><td>Administrative Exp (incl. R&amp;D)</td><td>(5,079)</td><td>(5,571)</td><td>(4,215)</td><td>(4,735)</td><td>(4,874)</td></tr><tr><td>Operating Profit (GP - SG&amp;A)</td><td>22,230</td><td>18,543</td><td>(2,668)</td><td>22,703</td><td>27,629</td></tr><tr><td>Other gains/(losses), net</td><td>(458)</td><td>(377)</td><td>439</td><td>393</td><td>493</td></tr><tr><td>Net Interest Income (Exp)</td><td>(2,975)</td><td>(2,458)</td><td>(2,128)</td><td>(1,554)</td><td>(1,091)</td></tr><tr><td>Investment Income</td><td>100</td><td>102</td><td>103</td><td>102</td><td>102</td></tr><tr><td>Company Defined Operating Profit</td><td>20,011</td><td>16,894</td><td>(3,375)</td><td>22,669</td><td>28,130</td></tr><tr><td>Income before tax</td><td>18,896</td><td>15,810</td><td>(4,254)</td><td>21,643</td><td>27,134</td></tr><tr><td>Income tax expenses</td><td>29</td><td>2</td><td>11</td><td>14</td><td>9</td></tr><tr><td>Net profit before Minority</td><td>18,925</td><td>15,812</td><td>(4,243)</td><td>21,657</td><td>27,142</td></tr><tr><td>Minority Interest</td><td>(1,044)</td><td>(325)</td><td>87</td><td>(445)</td><td>(558)</td></tr><tr><td>Net Profit</td><td>17,881</td><td>15,487</td><td>(4,156)</td><td>21,212</td><td>26,585</td></tr><tr><td>EPS (Diluted)</td><td>3.24</td><td>2.84</td><td>(0.72)</td><td>3.68</td><td>4.61</td></tr><tr><td>EBITDA (non-CASBE)</td><td>37,183</td><td>32,774</td><td>13,153</td><td>39,112</td><td>44,665</td></tr><tr><td>EBIT</td><td>21,872</td><td>18,268</td><td>(2,126)</td><td>23,198</td><td>28,225</td></tr></table>

<table><tr><td colspan="6">Balance Sheet</td></tr><tr><td>FY-end Dec (RMB mn)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Current assets</td><td>61,319</td><td>54,576</td><td>67,823</td><td>86,468</td><td>105,467</td></tr><tr><td>Cash and cash equivalents</td><td>16,952</td><td>13,862</td><td>21,951</td><td>45,378</td><td>63,256</td></tr><tr><td>Account Receivables</td><td>384</td><td>697</td><td>416</td><td>507</td><td>537</td></tr><tr><td>Prepayment</td><td>524</td><td>700</td><td>471</td><td>575</td><td>609</td></tr><tr><td>Inventories</td><td>41,970</td><td>37,177</td><td>42,884</td><td>37,889</td><td>38,941</td></tr><tr><td>Other Receivable</td><td>91</td><td>119</td><td>80</td><td>98</td><td>104</td></tr><tr><td>Other current assets</td><td>1,398</td><td>2,021</td><td>2,021</td><td>2,021</td><td>2,021</td></tr><tr><td>Non-current assets</td><td>126,330</td><td>117,165</td><td>110,359</td><td>100,237</td><td>89,875</td></tr><tr><td>Fixed Assets</td><td>106,751</td><td>100,634</td><td>93,773</td><td>83,595</td><td>73,174</td></tr><tr><td>Construction in progress</td><td>2,018</td><td>2,489</td><td>2,489</td><td>2,489</td><td>2,489</td></tr><tr><td>Biological Assets</td><td>9,355</td><td>6,797</td><td>6,865</td><td>6,934</td><td>7,003</td></tr><tr><td>Right of use assets</td><td>5,122</td><td>3,902</td><td>3,902</td><td>3,902</td><td>3,902</td></tr><tr><td>Intangible Assets</td><td>1,187</td><td>1,245</td><td>1,212</td><td>1,179</td><td>1,146</td></tr><tr><td>Deferred income tax assets</td><td>101</td><td>140</td><td>140</td><td>140</td><td>140</td></tr><tr><td>Other non-current assets</td><td>1,796</td><td>1,958</td><td>1,978</td><td>1,999</td><td>2,020</td></tr><tr><td>Total assets</td><td>187,649</td><td>171,741</td><td>178,182</td><td>186,705</td><td>195,342</td></tr><tr><td>Current liabilities</td><td>85,477</td><td>69,840</td><td>68,086</td><td>64,908</td><td>62,743</td></tr><tr><td>Notes Payable</td><td>2,724</td><td>714</td><td>1,566</td><td>1,544</td><td>1,587</td></tr><tr><td>Account Payable</td><td>17,993</td><td>12,613</td><td>14,833</td><td>15,491</td><td>16,820</td></tr><tr><td>Short-term loans</td><td>45,258</td><td>41,155</td><td>37,040</td><td>33,336</td><td>30,002</td></tr><tr><td>Customer Advance</td><td>600</td><td>1,107</td><td>656</td><td>801</td><td>848</td></tr><tr><td>Tax payable</td><td>62</td><td>62</td><td>62</td><td>62</td><td>62</td></tr><tr><td>Wage payable</td><td>1,107</td><td>772</td><td>772</td><td>772</td><td>772</td></tr><tr><td>Other payable</td><td>8,348</td><td>5,517</td><td>5,406</td><td>5,298</td><td>5,192</td></tr><tr><td>Other current liabilities</td><td>9,386</td><td>7,899</td><td>7,750</td><td>7,603</td><td>7,459</td></tr><tr><td>Non-current liabilities</td><td>24,636</td><td>23,159</td><td>22,728</td><td>22,318</td><td>21,928</td></tr><tr><td>Long term debt</td><td>8,797</td><td>7,733</td><td>7,347</td><td>6,979</td><td>6,630</td></tr><tr><td>Bond Payable</td><td>9,466</td><td>11,695</td><td>11,695</td><td>11,695</td><td>11,695</td></tr><tr><td>Deferred tax liabilities</td><td>841</td><td>874</td><td>874</td><td>874</td><td>874</td></tr><tr><td>Lease Liabilities</td><td>4,355</td><td>2,179</td><td>2,136</td><td>2,093</td><td>2,051</td></tr><tr><td>Other non-current liabilities</td><td>1,178</td><td>677</td><td>677</td><td>677</td><td>677</td></tr><tr><td>Equity</td><td>72,032</td><td>77,689</td><td>86,402</td><td>98,069</td><td>108,703</td></tr><tr><td>Share capital</td><td>5,463</td><td>5,463</td><td>5,773</td><td>5,773</td><td>5,773</td></tr><tr><td>Capital Reserve</td><td>13,729</td><td>13,039</td><td>23,727</td><td>23,727</td><td>23,727</td></tr><tr><td>Convertible bond</td><td>1,017</td><td>1,017</td><td>1,017</td><td>1,017</td><td>1,017</td></tr><tr><td>Preferred stock</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Reserves</td><td>54,822</td><td>62,182</td><td>59,896</td><td>71,563</td><td>82,197</td></tr><tr><td>Minus: Treasury stock</td><td>3,000</td><td>4,011</td><td>4,011</td><td>4,011</td><td>4,011</td></tr><tr><td>Minorities</td><td>5,504</td><td>1,053</td><td>966</td><td>1,411</td><td>1,968</td></tr><tr><td>Total Liabilities + Equity</td><td>187,649</td><td>171,741</td><td>178,182</td><td>186,705</td><td>195,342</td></tr><tr><td>Net cash (debt)/Equity</td><td>52%</td><td>45%</td><td>26%</td><td>-5%</td><td>-24%</td></tr><tr><td>Total capital employed</td><td>126,087</td><td>126,578</td><td>130,789</td><td>138,384</td><td>145,336</td></tr><tr><td>Net cash / (debt)</td><td>(37,103)</td><td>(35,026)</td><td>(22,436)</td><td>5,063</td><td>26,623</td></tr></table>

Source: Company Data, MS. E=MS estimates

<table><tr><td colspan="6">Ratio Analysis</td></tr><tr><td>FY-end Dec</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Chg (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>24.4%</td><td>4.5%</td><td>-23.1%</td><td>22.0%</td><td>6.0%</td></tr><tr><td>Gross profit</td><td>730.8%</td><td>-10.3%</td><td>-88.4%</td><td>873.8%</td><td>17.6%</td></tr><tr><td>Operating</td><td>-5.2%</td><td>11.2%</td><td>-20.8%</td><td>9.6%</td><td>2.7%</td></tr><tr><td>EBITDA</td><td>212.8%</td><td>-9.4%</td><td>-59.9%</td><td>197.4%</td><td>14.2%</td></tr><tr><td>EBIT</td><td>-2059.9%</td><td>-16.5%</td><td>-111.6%</td><td>-1191.1%</td><td>21.7%</td></tr><tr><td>Net profit</td><td>-554.1%</td><td>-16.5%</td><td>-126.8%</td><td>-610.4%</td><td>25.3%</td></tr><tr><td>Margins (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross</td><td>20.8%</td><td>17.8%</td><td>2.7%</td><td>21.4%</td><td>23.7%</td></tr><tr><td>Hog Production</td><td>20.9%</td><td>17.3%</td><td>1.3%</td><td>21.5%</td><td>23.7%</td></tr><tr><td>Slaughtering</td><td>-0.7%</td><td>-1.2%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>SG&amp;A</td><td>4.5%</td><td>4.8%</td><td>4.9%</td><td>4.4%</td><td>4.3%</td></tr><tr><td>Operating</td><td>16.1%</td><td>12.9%</td><td>-2.4%</td><td>16.8%</td><td>19.3%</td></tr><tr><td>E

[中间内容因长度限制已省略]

>U (03/04/2025)</td><td>Rmb12.26</td></tr><tr><td>Ecovacs Robotics Co Ltd (603486.SS)</td><td>O (07/09/2026)</td><td>Rmb58.07</td></tr><tr><td>Foshan Haitian Flavouring and Food (603288.SS)</td><td>E (07/28/2025)</td><td>Rmb37.01</td></tr><tr><td>Foshan Haitian Flavouring and Food (3288.HK)</td><td>E (05/21/2026)</td><td>HK$32.54</td></tr><tr><td>Haidilao International Holding Ltd (6862.HK)</td><td>O (05/26/2021)</td><td>HK$11.62</td></tr><tr><td>Hangzhou Robam Appliances Co Ltd (002508.SZ)</td><td>U (02/21/2024)</td><td>Rmb16.14</td></tr><tr><td>Laopu Gold (6181.HK)</td><td>O (10/20/2025)</td><td>HK$302.20</td></tr><tr><td>Super Hi (HDL.O)</td><td>E (01/14/2025)</td><td>US$13.12</td></tr><tr><td>Zhejiang Supor Co. Ltd. (002032.SZ)</td><td>U (07/27/2026)</td><td>Rmb41.49</td></tr><tr><td colspan="3">Lillian Lou</td></tr><tr><td>Anhui Gujing Distillery Company Limited (000596.SZ)</td><td>U (02/13/2026)</td><td>Rmb90.45</td></tr><tr><td>Budweiser Brewing Company APAC Ltd (1876.HK)</td><td>O (11/04/2019)</td><td>HK$6.79</td></tr><tr><td>Chagee Holdings Ltd (CHA.O)</td><td>O (06/02/2025)</td><td>US$11.64</td></tr><tr><td>China Mengniu Dairy (2319.HK)</td><td>O (09/14/2017)</td><td>HK$18.68</td></tr><tr><td>China Resources Beer Holdings Co Ltd (0291.HK)</td><td>O (12/11/2018)</td><td>HK$23.70</td></tr><tr><td>Chongqing Brewery Co. Ltd. (600132.SS)</td><td>U (07/30/2021)</td><td>Rmb44.69</td></tr><tr><td>Eastroc Beverages (605499.SS)</td><td>O (03/12/2026)</td><td>Rmb135.16</td></tr><tr><td>Eastroc Beverages (9980.HK)</td><td>O (03/12/2026)</td><td>HK$117.70</td></tr><tr><td>Gree Electric Appliances Inc of Zhuhai (000651.SZ)</td><td>E (07/09/2026)</td><td>Rmb40.80</td></tr><tr><td>Haier Smart Home Co Ltd (600690.SS)</td><td>E (01/17/2022)</td><td>Rmb22.40</td></tr><tr><td>Haier Smart Home Co Ltd (6690.HK)</td><td>E (01/17/2022)</td><td>HK$21.78</td></tr><tr><td>Kweichow Moutai Company Ltd. (600519.SS)</td><td>O (10/17/2014)</td><td>Rmb1,320.00</td></tr><tr><td>Luzhou Lao Jiao Co. Ltd (000568.SZ)</td><td>E (01/23/2019)</td><td>Rmb87.00</td></tr><tr><td>Midea Group Co Ltd. (0300.HK)</td><td>O (11/01/2024)</td><td>HK$96.35</td></tr><tr><td>Midea Group Co Ltd. (000333.SZ)</td><td>O (01/17/2022)</td><td>Rmb85.37</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (2714.HK)</td><td>O (03/17/2026)</td><td>HK$32.98</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (002714.SZ)</td><td>O (03/17/2026)</td><td>Rmb39.30</td></tr><tr><td>Nongfu Spring Co Ltd (9633.HK)</td><td>E (07/30/2021)</td><td>HK$41.86</td></tr><tr><td>Shanxi Xinghuacun Fen Wine Factory Co. (600809.SS)</td><td>O (10/28/2020)</td><td>Rmb126.25</td></tr><tr><td>Shuanghui Development (000895.SZ)</td><td>U (03/16/2021)</td><td>Rmb25.70</td></tr><tr><td>Tingyi (Cayman Islands) (0322.HK)</td><td>E (07/25/2025)</td><td>HK$11.77</td></tr><tr><td>Tsingtao Brewery Co Ltd (0168.HK)</td><td>E (11/01/2024)</td><td>HK$46.42</td></tr><tr><td>Tsingtao Brewery Co Ltd (600600.SS)</td><td>E (02/28/2024)</td><td>Rmb54.44</td></tr><tr><td>Uni-President China (0220.HK)</td><td>E (07/25/2025)</td><td>HK$7.44</td></tr><tr><td>Want Want China Holdings Ltd (0151.HK)</td><td>E (11/29/2023)</td><td>HK$3.46</td></tr><tr><td>WH Group (0288.HK)</td><td>O (02/24/2025)</td><td>HK$8.40</td></tr><tr><td>Wuliangye Yibin Company Ltd. (000858.SZ)</td><td>E (08/15/2024)</td><td>Rmb74.80</td></tr><tr><td>Yanghe Brewery (002304.SZ)</td><td>U (01/05/2021)</td><td>Rmb40.12</td></tr><tr><td>Yanjing Brewery (000729.SZ)</td><td>U (09/02/2015)</td><td>Rmb12.37</td></tr><tr><td>Yili Industrial (600887.SS)</td><td>O (01/29/2014)</td><td>Rmb26.58</td></tr><tr><td>Yum China Holdings Inc. (YUMC.N)</td><td>O (03/20/2018)</td><td>US$45.53</td></tr><tr><td>ZJLD Group (6979.HK)</td><td>E (02/13/2026)</td><td>HK$8.04</td></tr><tr><td colspan="3">Terence Cheng</td></tr><tr><td>Chervon Holdings Ltd. (2285.HK)</td><td>E (04/12/2024)</td><td>HK$18.66</td></tr><tr><td>Crystal International Group Ltd. (2232.HK)</td><td>E (06/23/2025)</td><td>HK$5.73</td></tr><tr><td>Gongniu Group Co Ltd (603195.SS)</td><td>O (05/08/2023)</td><td>Rmb40.01</td></tr><tr><td>Hangzhou Greatstar Industrial Co Ltd (002444.SZ)</td><td>E (10/26/2022)</td><td>Rmb29.49</td></tr><tr><td>Huali Industrial Group Co (300979.SZ)</td><td>U (02/10/2026)</td><td>Rmb35.92</td></tr><tr><td>Shenzhou International Group Holdings (2313.HK)</td><td>O (07/13/2017)</td><td>HK$43.52</td></tr><tr><td>Stella International Holdings Ltd (1836.HK)</td><td>E (06/23/2025)</td><td>HK$13.98</td></tr><tr><td>Techtronic Industries Co Ltd (0669.HK)</td><td>O (12/05/2019)</td><td>HK$128.00</td></tr><tr><td>Yue Yuen Industrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$13.92</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
