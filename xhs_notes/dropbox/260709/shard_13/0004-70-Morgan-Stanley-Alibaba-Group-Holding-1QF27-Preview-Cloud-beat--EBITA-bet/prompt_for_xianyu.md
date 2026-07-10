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
# Alibaba Group Holding | Asia Pacific

# 1QF27 Preview: Cloud beat, EBITA better than feared

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Alibaba Group Holding (BABA.N)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>US$190.00</td><td>US$180.00</td></tr></table>

Cloud acceleration to beat market expectations at +45%, while margin expansion to remain intact. China Ecom EBITA better than feared, thanks to QC loss narrowing quicker than expected and e-com ex-QC EBITA. Top Pick.

## Key Takeaways

■ Total group rev +9%, adj EBITA Rmb26bn (-33%).

Cloud +45% YoY (vs 40% external in 4Q), EBITA margin to expand to 11% (vs 9% in 4Q).

CMR +1-2% YoY on a LFL basis (vs 7-8% in 4Q). E-com EBITA (ex QC) -3-4% YoY. QC losses narrow to Rmb10bn (vs MSe Rmb18bn in 4Q).

China E-com EBITA + AIDC largely flat YoY. All Others loss narrow to Rmb16.5bn (vs Rmb21bn loss in 4Q).

Cloud growth accelerates to 45% YoY: Alicloud growth momentum to sustain, driven mainly by MAAS contribution, with previous Jun quarter target of Rmb10bn ARR achieved earlier than expected and AI-related revenue continuing to grow at triple digits. Cloud margin expansion intact at 11%, driven by price hikes starting in April and increasing MAAS rev mix; on track to deliver long-term target of 20%. T-head will also be included in the cloud segment from this quarter, but we expect limited impact due to serving external customers via Alicloud. We expect cloud growth to continue to accelerate in upcoming quarters.

CMR in line, +1-2% (LFL basis), but -7% under the new accounting standard: CMR grows in line with the industry (NBS Apr+May +1.4%). We estimate core EBITA (ex-QC) -3-4% YoY, gap vs LFL CMR narrows on cost efficiency gains. QC loss narrowing is better than expected, est. -Rmb10bn loss (vs Rmb18bn in 4Q), with UE improved driven by increasing AOV. We estimate total China e-com EBITA -2% YoY.

All Others losses narrow to Rmb16.5bn, removing some one-off CNY promotion expenses. We expect expenses related to Qwen model training to continue to be sizable alongside the token surge. We expect more disclosure on All Others losses breakdown going forward. We estimate All Others losses at Rmb72bn in F27.

Reiterate OW (top pick); Trim PT to US\$180: We raised our revenue estimates by 2-3% in F27-28 on higher cloud contribution, but slightly offset by lower e-comm. EBITA estimates largely unchanged. With the recent price correction, valuation is attractive at 13x F28 PE. Our DCF-derived PT implies 23x F28 P/E.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Gary Yu</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Gary.Yu@morganstanley.com</td><td>+852 2848-6918</td></tr><tr><td colspan="2">Joanne Lau</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Joanne.CY.Lau@morganstanley.com</td><td>+852 3963-1592</td></tr><tr><td colspan="2">Eddy Wang, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Eddy.Wang@morganstanley.com</td><td>+852 2239-7339</td></tr></table>

![](images/2a91db529271407aca7ede9f888cd6f092f82249505b2bdf9c7ed6d102b7791f.jpg)

## Alibaba Group Holding (BABA.N, BABA UN) Top Pick

China Internet and Other Services | China

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>US$180.00</td></tr><tr><td>Up/downside to price target (%)</td><td>83</td></tr><tr><td>Shr price, close (Jul 7, 2026)</td><td>US$98.14</td></tr><tr><td>52-Week Range</td><td>US$192.67-92.87</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>2,475</td></tr><tr><td>Mkt cap, curr (mn)</td><td>US$242,909</td></tr><tr><td>EV, curr (mn)</td><td>US$148,840</td></tr><tr><td>Avg daily trading value (mn)</td><td>US$290</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>03/26</td><td>03/27e</td><td>03/28e</td><td>03/29e</td></tr><tr><td>EPS (Rmb)**</td><td>44.00</td><td>30.27</td><td>45.34</td><td>63.20</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>30.4</td><td>46.3</td><td>64.3</td></tr><tr><td>Revenue, net (Rmb bn)</td><td>1,024</td><td>1,125</td><td>1,239</td><td>1,367</td></tr><tr><td>Net income (Rmb bn)**</td><td>106</td><td>75</td><td>112</td><td>157</td></tr><tr><td>P/E**</td><td>19.7</td><td>22.0</td><td>14.7</td><td>10.5</td></tr><tr><td>EV/EBITDA</td><td>16.1</td><td>7.2</td><td>4.6</td><td>3.2</td></tr><tr><td>EV/revenue*</td><td>1.9</td><td>1.4</td><td>1.3</td><td>1.1</td></tr><tr><td>P/BV</td><td>2.0</td><td>1.5</td><td>1.3</td><td>1.2</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
\* = GAAP or approximated based on GAAP
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Alibaba Group Holding BABA.N</td></tr><tr><td>Cloud revenue growth</td><td>↑ Likely upside surprise</td><td>— Largely unchanged</td></tr><tr><td colspan="3">• Cloud +45% YoY (vs 40% external in 4Q), EBITA margin to expand to 11% (vs 9% in 4Q).</td></tr><tr><td colspan="3">*Likely impact to consensus EPS is for the next 12 monthsSource: Company data, MS</td></tr></table>

Preview to earnings

<table><tr><td>Alibaba GroupYE MarRMB mn</td><td>Jun-251Q26Actual</td><td>Mar-264Q26Actual</td><td>Jun-261Q27eMse</td><td>YoY%</td><td>1Q27Consensus</td><td>Diff%</td></tr><tr><td>Revenue</td><td>247,652</td><td>243,380</td><td>269,045</td><td>8.6%</td><td>268,956</td><td>0.0%</td></tr><tr><td>Income from operations</td><td>34,988</td><td>(848)</td><td>22,281</td><td>-36.3%</td><td>19,974</td><td>11.6%</td></tr><tr><td>Adjusted EBITA</td><td>38,844</td><td>5,102</td><td>26,099</td><td>-32.8%</td><td>25,974</td><td>0.5%</td></tr><tr><td>Non-GAAP net profit</td><td>33,510</td><td>86</td><td>24,148</td><td>-27.9%</td><td>23,945</td><td>0.8%</td></tr><tr><td>Adj. EBITA margin</td><td>15.7%</td><td>2.1%</td><td>9.7%</td><td>-6.0 ppts</td><td>9.7%</td><td>0.0 ppts</td></tr><tr><td>Non-GAAP net profit margin</td><td>13.5%</td><td>0.0%</td><td>9.0%</td><td>-4.6 ppts</td><td>8.9%</td><td>0.1 ppts</td></tr><tr><td>By Segment</td><td>1Q26</td><td>4Q26</td><td>1Q27e</td><td>YoY</td><td>1Q27</td><td>Diff</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alibaba China E-commerce Group</td><td>140,072</td><td>122,220</td><td>141,692</td><td>1.2%</td><td>145,719</td><td>-2.8%</td></tr><tr><td>Customer management (CMR)</td><td>89,252</td><td>73,024</td><td>83,004</td><td>-7.0%</td><td>88,565</td><td>-6.3%</td></tr><tr><td>Quick commerce</td><td>14,784</td><td>19,988</td><td>21,437</td><td>45.0%</td><td>20,810</td><td>3.0%</td></tr><tr><td>Alibaba International Digital Commerce Group</td><td>34,741</td><td>35,429</td><td>36,478</td><td>5.0%</td><td>36,770</td><td>-0.8%</td></tr><tr><td>Cloud Intelligence Group</td><td>33,398</td><td>41,626</td><td>48,427</td><td>45.0%</td><td>47,004</td><td>3.0%</td></tr><tr><td>All others</td><td>58,599</td><td>65,459</td><td>60,357</td><td>3.0%</td><td>61,836</td><td>-2.4%</td></tr><tr><td>Unallocated</td><td>519</td><td>641</td><td>545</td><td>5.0%</td><td>567</td><td>-3.9%</td></tr><tr><td>Inter-segment elimination</td><td>(19,677)</td><td>(21,995)</td><td>(18,454)</td><td>-6.2%</td><td>(23,401)</td><td>-21.1%</td></tr><tr><td>Consolidated revenue</td><td>247,652</td><td>243,380</td><td>269,045</td><td>8.6%</td><td>268,956</td><td>0.0%</td></tr><tr><td>Adjusted EBITA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alibaba China E-commerce Group</td><td>38,389</td><td>24,010</td><td>37,549</td><td>-2.2%</td><td>33,900</td><td>10.8%</td></tr><tr><td>Alibaba International Digital Commerce Group</td><td>(59)</td><td>(138)</td><td>800</td><td></td><td>240</td><td></td></tr><tr><td>Cloud Intelligence Group</td><td>2,954</td><td>3,796</td><td>5,327</td><td>80.3%</td><td>4,908</td><td>8.5%</td></tr><tr><td>All others</td><td>(1,415)</td><td>(21,160)</td><td>(16,500)</td><td></td><td>(14,922)</td><td>10.6%</td></tr><tr><td>Unallocated</td><td>(419)</td><td>(788)</td><td>(440)</td><td>5.0%</td><td>(973)</td><td></td></tr><tr><td>Inter-segment elimination</td><td>(606)</td><td>(618)</td><td>(636)</td><td>5.0%</td><td>(625)</td><td></td></tr><tr><td>Consolidated adjusted EBITA</td><td>38,844</td><td>5,102</td><td>26,099</td><td>-32.8%</td><td>25,974</td><td>0.5%</td></tr><tr><td>Adjusted EBITA margin</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alibaba China E-commerce Group</td><td>27.4%</td><td>19.6%</td><td>26.5%</td><td>-0.9 ppts</td><td>23.3%</td><td>3.2 ppts</td></tr><tr><td>Alibaba International Digital Commerce Group</td><td>-0.2%</td><td>-0.4%</td><td>2.2%</td><td>2.4 ppts</td><td>0.7%</td><td>1.5 ppts</td></tr><tr><td>Cloud Intelligence Group</td><td>8.8%</td><td>9.1%</td><td>11.0%</td><td>2.2 ppts</td><td>10.4%</td><td>0.6 ppts</td></tr><tr><td>All others</td><td>-2.4%</td><td>-32.3%</td><td>-27.3%</td><td>-24.9 ppts</td><td>-24.1%</td><td>-3.2 ppts</td></tr><tr><td>Consolidated adjusted EBITA margin</td><td>15.7%</td><td>2.1%</td><td>9.7%</td><td>-6.0 ppts</td><td>9.7%</td><td>0.0 ppts</td></tr></table>

Exhibit 1: Summary of 1QF27 forecasts  
Source: Company data, VisibleAlpha consensus, MS (E) estimates.

## 1QF27 Earnings Forecasts

## Estimate Changes

Exhibit 2: Estimate changes

<table><tr><td rowspan="2">Years Ending December 31Rmb mn</td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">Change</td></tr><tr><td>2027E</td><td>2028E</td><td>2029E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Revenue</td><td>1,124,656</td><td>1,239,461</td><td>1,366,835</td><td>1,099,618</td><td>1,203,947</td><td>1,313,645</td><td>2.3%</td><td>2.9%</td><td>4.0%</td></tr><tr><td>Net income attributable to Alibaba Group Holding</td><td>75,018</td><td>112,322</td><td>156,539</td><td>75,389</td><td>114,756</td><td>159,299</td><td>-0.5%</td><td>-2.1%</td><td>-1.7%</td></tr><tr><td>Adjusted EBITA</td><td>95,184</td><td>142,744</td><td>197,398</td><td>95,007</td><td>145,054</td><td>199,812</td><td>0.2%</td><td>-1.6%</td><td>-1.2%</td></tr><tr><td>Adjusted EBITDA</td><td>154,006</td><td>230,628</td><td>307,550</td><td>153,275</td><td>231,696</td><td>308,555</td><td>0.5%</td><td>-0.5%</td><td>-0.3%</td></tr><tr><td>Adjusted Net Profit</td><td>89,038</td><td>126,823</td><td>171,460</td><td>88,893</td><td>128,712</td><td>173,574</td><td>0.2%</td><td>-1.5%</td><td>-1.2%</td></tr><tr><td>Adjusted NP to Ordinary shareholders</td><td>89,412</td><td>126,828</td><td>171,411</td><td>89,267</td><td>128,718</td><td>173,523</td><td>0.2%</td><td>-1.5%</td><td>-1.2%</td></tr><tr><td>GAAP EPS for consensus (Rmb)</td><td>30.27</td><td>45.34</td><td>63.20</td><td>30.42</td><td>46.32</td><td>64.32</td><td>-0.5%</td><td>-2.1%</td><td>-1.7%</td></tr><tr><td>Non-GAAP Diluted EPS (Rmb)</td><td>36.08</td><td>51.20</td><td>69.21</td><td>36.02</td><td>51.96</td><td>70.07</td><td>0.2%</td><td>-1.5%</td><td>-1.2%</td></tr><tr><td>yoy %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>9.9%</td><td>10.2%</td><td>10.3%</td><td>7.4%</td><td>9.5%</td><td>9.1%</td><td>2.4 ppts</td><td>0.7 ppts</td><td>1.2 ppts</td></tr><tr><td>Adjusted EBITA</td><td>-0.6%</td><td>11.0%</td><td>16.7%</td><td>-2.4%</td><td>11.3%</td><td>16.1%</td><td>1.7 ppts</td><td>-0.3 ppts</td><td>0.6 ppts</td></tr><tr><td>Adjusted NP to Ordinary shareholders</td><td>38.5%</td><td>41.8%</td><td>35.2%</td><td>38.3%</td><td>44.2%</td><td>34.8%</td><td>0.2 ppts</td><td>-2.3 ppts</td><td>0.3 ppts</td></tr></table>

Source: MS estimates.

## Valuation Methodology

## We trim our DCF-derived PT to US\$180 (was US\$190)

DCF is our primary valuation methodology. We think this is a prudent approach to capture the company's long-term earnings and overall cash flow outlook. Our key DCF assumptions – WACC of 10% and terminal growth rate of 3% – are unchanged.

Exhibit 3: DCF matrix – unlevered free cash flow

<table><tr><td rowspan="2">Years Ending March 31Rmb mn</td><td rowspan="2">2024</td><td rowspan="2">2025</td><td rowspan="2">2026EScenario</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td><td>2033E</td><td>2034E</td><td>2035E</td><td>2036E</td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">DCF</td></tr><tr><td>Adjusted EBITA (non-GAAP; incl. SBC)</td><td>146,482</td><td>159,095</td><td>65,236</td><td>81,585</td><td>128,525</td><td>182,321</td><td>225,876</td><td>267,118</td><td>289,223</td><td>311,198</td><td>334,585</td><td>359,571</td><td>386,332</td></tr><tr><td>D&amp;A</td><td>22,912</td><td>36,123</td><td>42,039</td><td>65,474</td><td>94,586</td><td>116,945</td><td>135,676</td><td>151,307</td><td>167,635</td><td>176,818</td><td>184,415</td><td>190,742</td><td>196,042</td></tr><tr><td>Capex</td><td>(32,929)</td><td>(85,972)</td><td>(126,937)</td><td>(163,075)</td><td>(185,919)</td><td>(191,357)</td><td>(195,720)</td><td>(213,790)</td><td>(198,091)</td><td>(199,980)</td><td>(201,736)</td><td>(203,353)</td><td>(204,807)</td></tr><tr><td>Taxes</td><td>(23,680)</td><td>(31,306)</td><td>(22,804)</td><td>(14,685)</td><td>(23,134)</td><td>(32,818)</td><td>(40,658)</td><td>(48,081)</td><td>(52,060)</td><td>(56,016)</td><td>(60,225)</td><td>(64,723)</td><td>(69,540)</td></tr><tr><td>Licensed copyrights</td><td>(9,054)</td><td>(5,912)</td><td>(6,403)</td><td>(6,595)</td><td>(6,760)</td><td>(6,895)</td><td>(6,999)</td><td>(7,069)</td><td>(7,139)</td><td>(7,211)</td><td>(7,283)</td><td>(7,356)</td><td>(7,429)</td></tr><tr><td>Non-controlling interests</td><td>8,409</td><td>3,494</td><td>3,777</td><td>259</td><td>(110)</td><td>(168)</td><td>(221)</td><td>(268)</td><td>(317)</td><td>(369)</td><td>(423)</td><td>(480)</td><td>(540)</td></tr><tr><td>Working capital</td><td>(4,695)</td><td>(18,076)</td><td>(16,144)</td><td>(26,902)</td><td>(33,852)</td><td>(32,087)</td><td>(24,233)</td><td>(11,105)</td><td>(19,889)</td><td>(13,079)</td><td>(14,110)</td><td>(15,265)</td><td>(16,560)</td></tr><tr><td>Unlevered FCF (FCFF)</td><td>107,445</td><td>57,446</td><td>(61,236)</td><td>(63,939)</td><td>(26,665)</td><td>35,942</td><td>93,722</td><td>138,112</td><td>179,362</td><td>211,362</td><td>235,223</td><td>259,136</td><td>283,499</td></tr><tr><td>% YoY</td><td>-11.3%</td><td>-46.5%</td><td>-206.6%</td><td>4.4%</td><td>-58.3%</td><td>-234.8%</td><td>160.8%</td><td>47.4%</td><td>29.9%</td><td>17.8%</td><td>11.3%</td><td>10.2%</td><td>9.4%</td></tr><tr><td>% of revenue</td><td>11.4%</td><td>5.8%</td><td>-6.0%</td><td>-5.7%</td><td>-2.2%</td><td>2.6%</td><td>6.3%</td><td>8.1%</td><td>10.9%</td><td>12.2%</td><td>12.8%</td><td>13.4%</td><td>13.8%</td></tr><tr><td>WACC</td><td></td><td></td><td></td><td>10.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TGR</td><td></td><td></td><td></td><td>3.0%</td><td></td><td

[中间内容因长度限制已省略]

ich this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Internet and Other Services

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/07/2026)</td></tr><tr><td colspan="3">Eddy Wang, CFA</td></tr><tr><td>Autohome Inc (ATHM.N)</td><td>E (02/09/2023)</td><td>US$18.67</td></tr><tr><td>Full Truck Alliance Co. Ltd (YMM.N)</td><td>O (07/05/2023)</td><td>US$8.35</td></tr><tr><td>JD.com, Inc. (JD.O)</td><td>U (11/10/2025)</td><td>US$26.49</td></tr><tr><td>Kanzhun Ltd (BZ.O)</td><td>O (08/04/2021)</td><td>US$14.02</td></tr><tr><td>KE Holdings Inc (BEKE.N)</td><td>O (03/16/2022)</td><td>US$14.86</td></tr><tr><td>PDD Holdings Inc (PDD.O)</td><td>O (03/02/2023)</td><td>US$82.53</td></tr><tr><td>Vipshop Holdings Ltd (VIPS.N)</td><td>E (02/24/2022)</td><td>US$13.54</td></tr><tr><td colspan="3">Gary Yu</td></tr><tr><td>Alibaba Group Holding (BABA.N)</td><td>O (02/24/2025)</td><td>US$98.14</td></tr><tr><td>Baidu Inc (BIDU.O)</td><td>E (05/17/2024)</td><td>US$112.09</td></tr><tr><td>Meituan (3690.HK)</td><td>O (08/29/2024)</td><td>HK$80.90</td></tr><tr><td>Tencent Holdings Ltd. (0700.HK)</td><td>O (03/19/2020)</td><td>HK$478.80</td></tr><tr><td colspan="3">Rebecca Xu</td></tr><tr><td>HUYA Inc (HUYA.N)</td><td>E (05/16/2024)</td><td>US$2.35</td></tr><tr><td>IQIYI Inc (IQ.O)</td><td>E (01/19/2023)</td><td>US$1.00</td></tr><tr><td>JOYY Inc. (JOYY.O)</td><td>E (06/02/2022)</td><td>US$69.60</td></tr><tr><td>Weibo Corp (WB.O)</td><td>U (05/17/2024)</td><td>US$7.47</td></tr><tr><td colspan="3">Yang Liu</td></tr><tr><td>Bilibili Inc (BILI.O)</td><td>O (04/13/2026)</td><td>US$17.60</td></tr><tr><td>Kuaishou Technology (1024.HK)</td><td>O (05/26/2026)</td><td>HK$43.98</td></tr><tr><td>NetEase, Inc (NTES.O)</td><td>O (01/08/2025)</td><td>US$130.82</td></tr><tr><td>Tongcheng Travel Holdings (0780.HK)</td><td>O (01/04/2019)</td><td>HK$13.01</td></tr><tr><td>Trip.com Group Ltd (TCOM.O)</td><td>O (05/17/2021)</td><td>US$40.81</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
