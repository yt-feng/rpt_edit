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
# MedTech & HCIT: 2Q26 Chart Pack Preview: Mixed Fundamental Picture Meets Discounted Valuations

Heading into 2Q26 earnings, MedTech faces a confluence of macro and stock specific considerations — both in the context of marked YTD underperformance and most of the large cap stocks under coverage trading below their 20-year average multiples (see Exhibit 10). These performance dynamics reflect (1) decelerating growth broadly across the group; (2) maturation of recent product cycles that had supported above-trend sector-wide growth; and (3) and idiosyncratic headwinds at once-considered sector bellwethers.

Exhibit 1: Relative Sector Performance
Market Cap Weighted YTD as of 07/09/2026

<table><tr><td rowspan="2">Sector/Benchmark</td><td colspan="3">Performance</td></tr><tr><td>YTD</td><td>2025</td><td>2024</td></tr><tr><td>Large Cap (LC) MedTech</td><td>(20.0%)</td><td>7.8%</td><td>11.9%</td></tr><tr><td>SMID Cap MedTech</td><td>0.9%</td><td>2.5%</td><td>21.0%</td></tr><tr><td>XLV</td><td>4.8%</td><td>12.5%</td><td>0.9%</td></tr><tr><td>S&amp;P 500</td><td>10.2%</td><td>16.4%</td><td>23.3%</td></tr><tr><td>Russell 2000 (R2K)</td><td>20.6%</td><td>11.3%</td><td>10.0%</td></tr><tr><td colspan="4">Relative Performance</td></tr><tr><td>LC MedTech vs. XLV</td><td>(24.8%)</td><td>(4.7%)</td><td>11.0%</td></tr><tr><td>LC MedTech vs. S&amp;P 500</td><td>(30.2%)</td><td>(8.6%)</td><td>(11.5%)</td></tr><tr><td>SMID Cap MedTech vs. R2K</td><td>(19.6%)</td><td>(8.8%)</td><td>11.0%</td></tr></table>

Source: FactSet, Global Investment Research

Heading into results, we take a neutral to cautious view on the broader macro backdrop. On the one hand, our 2Q26 Hospital Due Diligence Day and 2Q26 Utilization Diagnostic point to a challenged U.S. volume environment, where this quarter likely represents a step-up from last quarter but not a normalization in trend (i.e. no catch-up from what was hoped to be transient headwinds in 1Q like weather, flu, and heightened seasonality). On the other hand, most companies under coverage are not dialing in an acceleration to their forward growth outlooks nor is consensus (Visible Alpha Consensus Data, unless otherwise noted).

Specific to the quarter — and evaluating where our estimates shake our vs. consensus — our organic growth estimates sit either at or slightly below consensus (see Exhibit 8) with exceptions including ABT (GSe +60bps vs. consensus); ISRG (GSe +70bps vs. consensus); and MDLN (+130bps vs. consensus). In each case where we are above Street, drivers are specific to company-related factors (ABT: recovery from OUS Libre tender delay, Instinct shipments to MiniMed, easing Diagnostics comps, EP share gain; ISRG: higher U.S. I&A per procedure on Sp, Ion, and forced feedback mix; MDLN: quarterly phasing related to selling days and comps).

## David Roman

+1(212)357-4617 |
david.roman@gs.com
GS & Co. LLC

Jamie Perse, CFA
+1(212)902-8192 | jamie.perse@gs.com
GS & Co. LLC

Philip Coover
+1(917)343-8573 |
philip.coover@gs.com
GS & Co. LLC

Jenny Rabinowitz
+1(212)855-0819 |
jenny.rabinowitz@gs.com
GS & Co. LLC

Marco Espaillat
+1(212)902-6790 |
marco.espaillat@gs.com
GS & Co. LLC

Turning to the balance of the year and guidance, we do not see meaningful risk to top-line outlooks since most companies have not considered a meaningful acceleration in 2026 guidance. For 2Q, we note that we project aggregated top-line organic growth to improve marginally QoQ, but most of this relates to Stryker's recovery from cybersecurity disruptions in 2Q and one-time inventory timing benefits at Solventum. Therefore, while we retain a cautious view on the direction-of-travel for macro trends, no company has assumed end-markets improve through the year. Down the P&L, we continue to forecast improving margins throughout the year, largely based on revenue scale and mix. Our current estimates do place heavy emphasis on 4Q, and we would expect EPS and/or margin upside in 2Q to be utilized as a counterbalance to 2H ramps. We remain vigilant on raw material trends but note on a trailing 30-day basis, most key input costs have come down (see Exhibit 6).

While a scenario where results are marginally better than expectations could support a short-term rebound in stocks, we think a sustained turnaround for the group needs to come from (1) more proactive capital allocation (both in boosting returns to shareholders and growth-oriented cash use); (2) appropriate calibration of estimates for 2026 and outer years; and (3) visibility into pipeline or other drives to accelerate performance.

Putting this all together, we continue to recommend selectivity across MedTech and highlight stocks where not only we see upside potential in the quarter (i.e. EW, OMDA, PODD) but also where the forward narrative (i.e. 2H26-2027+) can inflect positively, including: ABT and MMED.

Fundamental Check-Up: Key Trends in Markets We are Watching  
Exhibit 2: GS Coverage Implied Guidance

<table><tr><td rowspan="2">Company</td><td rowspan="2">Next Q Guidance (1)</td><td rowspan="2">FY Guidance (Mid-point)</td><td colspan="2">Organic Growth</td><td rowspan="2">Implied 2H vs. 1H</td></tr><tr><td>1H26</td><td>2H26</td></tr><tr><td colspan="6">Large Cap MedTech</td></tr><tr><td>Abbott</td><td>4.4%</td><td>7.0%</td><td>4.0%</td><td>10.0%</td><td>Acceleration</td></tr><tr><td>Baxter</td><td>(0.1%)</td><td>0.0%</td><td>(0.6%)</td><td>0.6%</td><td>Acceleration</td></tr><tr><td>Becton Dickinson (2)</td><td>2.5%</td><td>2.0%</td><td>2.6%</td><td>1.4%</td><td>Deceleration</td></tr><tr><td>Boston Scientific</td><td>5.4%</td><td>7.3%</td><td>7.4%</td><td>7.1%</td><td>Stable</td></tr><tr><td>Cooper Companies (3)</td><td>4.2%</td><td>4.0%</td><td>4.0%</td><td>4.0%</td><td>Stable</td></tr><tr><td>Dexcom</td><td>11.2%</td><td>12.0%</td><td>11.8%</td><td>12.2%</td><td>Stable</td></tr><tr><td>Edwards</td><td>10.3%</td><td>10.0%</td><td>11.5%</td><td>8.5%</td><td>Deceleration</td></tr><tr><td>GE Healthcare</td><td>4.0%</td><td>3.5%</td><td>3.5%</td><td>3.5%</td><td>Stable</td></tr><tr><td>Intuitive Surgical (4)</td><td>14.5%</td><td>14.5%</td><td>15.1%</td><td>13.9%</td><td>Deceleration</td></tr><tr><td>Insulet</td><td>21.0%</td><td>22.0%</td><td>25.5%</td><td>18.5%</td><td>Deceleration</td></tr><tr><td>Medline</td><td>8.8%</td><td>9.0%</td><td>9.5%</td><td>8.5%</td><td>Deceleration</td></tr><tr><td>Medtronic (5)</td><td>9.9%</td><td>7.0%</td><td>9.9%</td><td>6.0%</td><td>Deceleration</td></tr><tr><td>Solventum</td><td>7.1%</td><td>2.5%</td><td>4.6%</td><td>0.4%</td><td>Deceleration</td></tr><tr><td>Stryker</td><td>9.2%</td><td>8.8%</td><td>5.8%</td><td>11.7%</td><td>Acceleration</td></tr><tr><td>Zimmer</td><td>2.2%</td><td>2.0%</td><td>2.5%</td><td>1.5%</td><td>Deceleration</td></tr><tr><td colspan="6">SMID MedTech</td></tr><tr><td>Beta Bionics</td><td>36.1%</td><td>33.0%</td><td>46.4%</td><td>19.6%</td><td>Deceleration</td></tr><tr><td>Bausch + Lomb</td><td>6.5%</td><td>6.3%</td><td>6.1%</td><td>6.4%</td><td>Stable</td></tr><tr><td>Carlsmed</td><td>48.7%</td><td>48.0%</td><td>53.4%</td><td>42.6%</td><td>Deceleration</td></tr><tr><td>Glaukos</td><td>22.3%</td><td>23.6%</td><td>30.7%</td><td>16.5%</td><td>Deceleration</td></tr><tr><td>iRhythm</td><td>17.3%</td><td>17.8%</td><td>21.5%</td><td>14.1%</td><td>Deceleration</td></tr><tr><td>LivaNova</td><td>7.4%</td><td>7.5%</td><td>9.3%</td><td>5.7%</td><td>Deceleration</td></tr><tr><td>Kestra Medical (6)</td><td>54.3%</td><td>55.5%</td><td>52.5%</td><td>58.5%</td><td>Acceleration</td></tr><tr><td>Minimed (7)</td><td>6.6%</td><td>10.0%</td><td>6.6%</td><td>11.1%</td><td>Acceleration</td></tr><tr><td>Shoulder Innovations</td><td>50.7%</td><td>40.5%</td><td>58.0%</td><td>23.0%</td><td>Deceleration</td></tr><tr><td>Tandem</td><td>5.4%</td><td>6.0%</td><td>5.4%</td><td>6.6%</td><td>Acceleration</td></tr><tr><td colspan="6">Healthcare IT</td></tr><tr><td>Doximity (8)</td><td>3.9%</td><td>3.9%</td><td>3.9%</td><td>3.9%</td><td>Stable</td></tr><tr><td>Health Equity (9)</td><td>7.0%</td><td>7.8%</td><td>7.2%</td><td>8.0%</td><td>Acceleration</td></tr><tr><td>Omada</td><td>30.7%</td><td>25.0%</td><td>36.4%</td><td>13.6%</td><td>Deceleration</td></tr><tr><td>Teladoc</td><td>(3.2%)</td><td>(0.5%)</td><td>(3.8%)</td><td>2.8%</td><td>Acceleration</td></tr></table>

1) Visible Alpha Consensus used if no explicit guidance provided; 2) Next Q = 3Q26; 3) Next Q = 3Q26; 4) WW Procedure Growth; 5) MDT Next Q=1Q27, 1H=1Q, 2H=Q2-Q4; inclusive of extra week; 6) KMTS Next Q guide is implied 4Q26; 7) MMED Next Q=1Q27, 1H=1Q, 2H=Q2-Q4; inclusive of extra week; 8) DOCS Next Q=1Q27 guidance, 1H=1Q, 2H=Q2-Q4; 9) HQY FY 2027  
Source: Visible Alpha Consensus Data, Company data, GS Global Investment Research

Exhibit 3: Weighted Average Covered Large Cap Organic Growth (%)
Large Cap MedTech (includes JNJ, ABT MedTech and ISRG Procedure growth)

![](images/ad77e9f3e20065055bf074049d515bdb9bd834f36cac49894f48d79f8bb29b82.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: Weighted Average Covered Large Cap Gross Margin (%)  
![](images/cdfcceb2e4ee0236e4035802bd908bbe55dcb00bc8cedcdb59d60aa9e0239564.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: Weighted Average Covered Large Cap Operating Margin (%)  
![](images/cd839ce8a4a1370d906912eaf6d8343684c426bf29816ee0dac164fa95d82e17.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 6: MedTech Key Raw Materials

<table><tr><td>Raw Materials</td><td>Primary Use Cases</td><td>Key Manufacturers(1)</td><td>MoM % Change</td><td>YTD% Change</td></tr><tr><td>Aluminum Alloys</td><td>Imaging equipment frames, portable monitors</td><td>BAX, BDX, GEHC</td><td>(13.2)%</td><td>13.4 %</td></tr><tr><td>Copper</td><td>MRI coils, wearable circuits, robotic sensors</td><td>BBNX, DXCM, GEHC, MMEDISRG, PODD, TNDM</td><td>(0.9)%</td><td>10.3 %</td></tr><tr><td>DRAM Memory (2)</td><td>Advanced computing</td><td>All MedTech Coverage</td><td>-</td><td>81.0 %</td></tr><tr><td>Freight</td><td>Global Distribution</td><td>All MedTech Coverage</td><td>20-30%+</td><td>52.4 %</td></tr><tr><td>Fuel</td><td>Global Distribution</td><td>All MedTech Coverage</td><td>(16.6)%</td><td>25.4 %</td></tr><tr><td>Nickel</td><td>Self-expanding stents, neurovascular guidewires</td><td>ABT, BSX, MDT, SYK</td><td>(8.8)%</td><td>(0.8)%</td></tr><tr><td>Polycarbonate (PC)(3)</td><td>IV connectors, instrument housings, blood oxygenators</td><td>BAX, BDX, GEHC, LIVN</td><td>(6.2)%</td><td>16.6 %</td></tr><tr><td>Polyetheretherketone (PEEK)(4)</td><td>Spinal fusion cages, 3D-printed cranial implants</td><td>MDT, SYK</td><td>(6.2)%</td><td>16.6 %</td></tr><tr><td>Polyethylene</td><td>Joint replacement liners, catheters, medical tubing</td><td>BAX, BDX, MDT, SYK, ZBH</td><td>(9.4)%</td><td>11.0 %</td></tr><tr><td>Polypropylene (PP)</td><td>Syringes, non-woven surgical gowns, vials, drapes</td><td>BAX, BDX, MDLN, SOLV</td><td>(12.6)%</td><td>20.9 %</td></tr><tr><td>Silicone (Medical Grade)(5)</td><td>Catheters, seals, respiratory masks, lenses</td><td>BAX, BDX, BLCO, COO</td><td>(6.2)%</td><td>16.6 %</td></tr><tr><td>Stainless Steel</td><td>Scalpels, needles, orthopedic pins, surgical tools</td><td>BSX, ISRG, MDT, SYK, ZBH</td><td>4.2 %</td><td>22.7 %</td></tr><tr><td>Titanium &amp; Alloys</td><td>Orthopedic implants (hips/knees), pacemaker casings</td><td>ABT, BSX, MDT, SYK, ZBH</td><td>(2.8)%</td><td>(8.0)%</td></tr></table>

(1) Key Manufacturers are GS estimates (2) DRAM Memory estimates are 4Q25 to 1Q26 (3) Refers to FactSet aggregate commodity basket change (4) Refers to FactSet aggregate commodity basket change (5) Refers to FactSet aggregate commodity basket change  
Source: FactSet, Company data, GS Global Investment Research

## Earnings Outlook Summary: GS vs. Consensus

## Exhibit 7: Current Quarter & Fiscal Year Outlook (GS vs Street) \$s in millions, except per share data

Current Quarter

<table><tr><td rowspan="3">Company</td><td colspan="4">Current Quarter</td></tr><tr><td colspan="2">GS</td><td colspan="2">Consensus</td></tr><tr><td>Sales</td><td>EPS</td><td>Sales</td><td>EPS</td></tr><tr><td colspan="5">Large Cap MedTech</td></tr><tr><td>Abbott (ABT)</td><td>$12,610</td><td>$1.27</td><td>$12,499</td><td>$1.28</td></tr><tr><td>Baxter (BAX)</td><td>$2,846</td><td>$0.39</td><td>$2,797</td><td>$0.37</td></tr><tr><td>Becton Dickinson (BDX)</td><td>$4,823</td><td>$3.15</td><td>$4,883</td><td>$3.13</td></tr><tr><td>Boston Scientific (BSX)</td><td>$5,312</td><td>$0.82</td><td>$5,365</td><td>$0.83</td></tr><tr><td>Cooper Companies (COO)</td><td>$1,096</td><td>$1.12</td><td>$1,098</td><td>$1.12</td></tr><tr><td>Dexcom (DXCM)</td><td>$1,289</td><td>$0.62</td><td>$1,290</td><td>$0.61</td></tr><tr><td>Edwards (EW)</td><td>$1,702</td><td>$0.76</td><td>$1,700</td><td>$0.75</td></tr><tr><td>GE Healthcare (GEHC)</td><td>$5,323</td><td>$1.04</td><td>$5,276</td><td>$1.04</td></tr><tr><td>Insulet (PODD)</td><td>$782</td><td>$1.41</td><td>$787</td><td>$1.45</td></tr><tr><td>Intuitive Surgical (ISRG)</td><td>$2,809</td><td>$2.51</td><td>$2,820</td><td>$2.50</td></tr><tr><td>Medline Inc (MDLN)(1)</td><td>$7,584</td><td>$809</td><td>$7,507</td><td>$800</td></tr><tr><td>Medtronic (MDT)</td><td>$9,578</td><td>$1.39</td><td>$9,549</td><td>$1.39</td></tr><tr><td>Solventum (SOLV)</td><td>$2,158</td><td>$1.86</td><td>$2,155</td><td>$1.90</td></tr><tr><td>Stryker (SYK)</td><td>$6,565</td><td>$3.50</td><td>$6,571</td><td>$3.47</td></tr><tr><td>Zimmer (ZBH)</td><td>$2,132</td><td>$2.01</td><td>$2,133</td><td>$2.01</td></tr></table>

Fiscal Year

<table><tr><td colspan="2">GS</td><td colspan="2">Consensus</td></tr><tr><td>Sales</td><td>EPS</td><td>Sales</td><td>EPS</td></tr><tr><td>$50,219</td><td>$5.47</td><td>$50,311</td><td>$5.48</td></tr><tr><td>$11,433</td><td>$1.90</td><td>$11,361</td><td>$1.91</td></tr><tr><td>$19,076</td><td>$12.37</td><td>$19,210</td><td>$12.59</td></tr><tr><td>$21,387</td><td>$3.32</td><td>$21,603</td><td>$3.35</td></tr><tr><td>$4,304</td><td>$4.54</td><td>$4,307</td><td>$4.62</td></tr><tr><td>$5,206</td><td>$2.58</td><td>$5,224</td><td>$2.59</td></tr><tr><td>$6,787</td><td>$3.04</td><td>$6,754</td><td>$3.01</td></tr><tr><td>$21,883</td><td>$4.82</td><td>$21,811</td><td>$4.88</td></tr><tr><td>$3,339</td><td>$6.41</td><td>$3,328</td><td>$6.47</td></tr><tr><td>$11,596</td><td>$10.31</td><td>$11,686</td><td>$10.42</td></tr><tr><td>$31,126</td><td>$3,502</td><td>$31,069</td><td>$3,535</td></tr><tr><td>$38,875</td><td>$5.91</td><td>$38,872</td><td>$5.94</td></tr><tr><td>$8,199</td><td>$6.43</td><td>$8,193</td><td>$6.54</td></tr><tr><td>$27,143</td><td>$14.96</td><td>$27,267</td><td>$14.98</td></tr><tr><td>$8,471</td><td>$8.42</td><td>$8,546</td><td>$8.48</td></tr></table>

Current Quarter

<table><tr><td rowspan="3">SMID MedTech</td><td colspan="4">Current Quarter</td></tr><tr><td colspan="2">GS</td><td colspan="2">Consensus</td></tr><tr><td>Sales</td><td>EBITDA</td><td>Sales</td><td>EBITDA</td></tr><tr><td>Beta Bionics (BBNX)</td><td>$33</td><td>($20)</td><td>$32</td><td>($22)</td></tr><tr><td>Bausch and Lomb (BLCO)</td><td>$1,377</td><td>$244</td><td>$1,370</td><td>$236</td></tr><tr><td>Carlsmed (CARL)</td><td>$18</td><td>($8)</td><td>$18</td><td>($9)</td></tr><tr><td>Glaukos (GKOS)</td><td>$153</td><td>$16</td><td>$151</td><td>($0)</td></tr><tr><td>iRhythm (IRTC)</td><td>$219</td><td>$29</td><td>$219</td><td>$26</td></tr><tr><td>Minimed (MMED)</td><td>$837</td><td>$131</td><td>$830</td><td>$118</td></tr><tr><td>Mobia Medical (MOBI)</td><td>$12</td><td>($14)</td><td>$12</td><td>($14)</td></tr><tr><td>Kestra Medical (KMTS)</td><td>$26</td><td>($21)</td><td>$26</td><td>($22)</td></tr><tr><td>LivaNova (LIVN)(2)</td><td>$381</td><td>$1.07</td><td>$381</td><td>$1.09</td></tr><tr><td>Shoulder Innovations (SI)</td><t

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
