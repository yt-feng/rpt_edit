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
# China Healthcare

## 1H26 Results Preview: BD Deals to alleviate Pharma sales; CDMOs solid

## CITI'S TAKE

We expect leading CDMO companies may see beat in 1H25, resting on strong backlog growth. Some leading pharmas/biopharma to miss revenue in 1H26, despite episodic BD/out-licensing deals providing bottom-line support. Medical device names are likely to see mixed results – key factors are FX loss impact and domestic ASP pressure. Hospitals and distribution continue to face headwinds from strict medical insurance budget control. Consumer-facing sub-sectors — Medical Aesthetics (Imeik, Bloomage), Healthcare Services (Aier, Topchoice), and TCM (DEEJ) — remained broadly soft in 1H26. See 30/90-day catalyst watches: +ve: WuXi Bio / WuXi AppTec/ Pharmaron/ Tigermed/ SBP/ MicroPort Medbot/ Yifeng; -ve: 3S Bio, PAGD, Weigao, United Imaging.

CRO/CDMO: strong results confirmed; potential guidance uplift in focus — Following positive results, market attention shifts to FY26 and FY27 outlook. WuXi AppTec could deliver adj. net profit beat, with TIDES strength and funding recovery as key drivers; mgmt. likely to lift guidance after result. We expect revenue beat for WuXi XDC on strong ADC/XDC momentum. WuXi Bio's revenue should be in-line; adjusted profit intact despite headline drag from FX/FV losses. Tigermed's revenue should be in-line with net profit dragged by fair value losses in 2Q26, but revenue and gross margin expansion remain on track. Pharmaron's profit alert showed inline revenue and adj. net profit; new orders grew strongly by $30\%+$ yoy in 1H26.

Pharma/Biopharma: BD deals differentiate; beats & misses — Anti-corruption campaign continued to disrupt hospital-channel sales in 2Q26. We expect SBP to beat, aided by a US\$135mn upfront fee from Sanofi; Hansoh to beat on strong EGFR TKI ramp-up; and Junshi to beat in revenue on continued PD-1 ramp-up. Hengrui could post a revenue miss as anti-corruption impact was more pronounced than expected, though net profit was cushioned by the Kailera IPO gain. Huadong Medicines missed as the company proactively destocked distribution channels on GPO pressure. 3S Bio might miss driven by TPO destocking ahead of the 2026 NRDL cycle. CMS could miss. We expect Fosun Pharma, CSPC, and Innovent to be broadly in-line.

Medical Device: overseas remains the growth engine; domestic mixed — United Imaging could miss on both revenue and profit — slower-than-expected domestic revenue growth, higher R&D/selling expense and FX losses. Mindray should be in-line; domestic IVD led the growth and overseas momentum remains strong. We anticipate MicroPort Scientific and MicroPort MedBot to deliver in-line results, confirming fundamental turnarounds. Weigao could miss as VBP impact was worse than expected on both revenue and margin.

Distribution/Pharmacy: Hospital-end under pressure; leading retail recovery on track — Sinopharm might miss on heavier medical insurance budget control and local government fiscal pressure. Yifeng Pharmacy should be in-line with SSSG recovery on track.

(More on page 5)

John Yung, CFA $^{AC}$ +852-2501-2790
john.yung@citi.com

Zoe Bian AC

+852-2501-2752

zoe.bian@citi.com

Eva Zhao, CFA $^{AC}$

+852-2501-2701

eva.zhao@citi.com

## Data Summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>3SBio</td><td>1530.HK</td><td>HK$</td><td>16.92</td><td>42,800</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>-</td><td>36.00</td><td>nc</td><td>112.8</td><td>1.2</td><td>113.9</td><td>Dec-25</td><td>1.033</td><td>nc</td><td>0.949</td><td>nc</td></tr><tr><td>Huadong Medicine</td><td>000963.SZ</td><td>Rmb</td><td>30.890</td><td>54,173</td><td>21 Jul 15:00</td><td>1</td><td>nc</td><td>Downside^</td><td>48.000</td><td>nc</td><td>55.4</td><td>1.6</td><td>57.0</td><td>Dec-25</td><td>2.323</td><td>nc</td><td>2.718</td><td>nc</td></tr><tr><td>MicroPort MedBot</td><td>2252.HK</td><td>HK$</td><td>21.44</td><td>22,112</td><td>21 Jul 16:10</td><td>1H</td><td>nc</td><td>Upside^</td><td>41.00</td><td>nc</td><td>91.2</td><td>0.0</td><td>91.2</td><td>Dec-25</td><td>11</td><td>nc</td><td>39</td><td>nc</td></tr><tr><td>Pharmaron</td><td>3759.HK</td><td>HK$</td><td>23.62</td><td>75,702</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Upside^</td><td>45.00</td><td>nc</td><td>90.5</td><td>1.3</td><td>91.8</td><td>Dec-25</td><td>1.196</td><td>nc</td><td>1.502</td><td>nc</td></tr><tr><td>Ping AN Healthcare and Technology</td><td>1833.HK</td><td>HK$</td><td>7.67</td><td>16,578</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Downside^</td><td>18.00</td><td>nc</td><td>134.7</td><td>0.0</td><td>134.7</td><td>Dec-25</td><td>0.221</td><td>nc</td><td>0.319</td><td>nc</td></tr><tr><td>Shandong Weigao Group</td><td>1066.HK</td><td>HK$</td><td>3.45</td><td>15,557</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Downside^</td><td>6.00</td><td>nc</td><td>73.9</td><td>6.1</td><td>80.0</td><td>Dec-25</td><td>0.335</td><td>nc</td><td>0.365</td><td>nc</td></tr><tr><td>Sino Biopharmaceutical</td><td>1177.HK</td><td>HK$</td><td>5.11</td><td>95,470</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Upside^</td><td>10.00</td><td>nc</td><td>95.7</td><td>1.2</td><td>96.9</td><td>Dec-25</td><td>0.186</td><td>nc</td><td>0.206</td><td>nc</td></tr><tr><td>Sinopharm Group</td><td>1099.HK</td><td>HK$</td><td>17.32</td><td>54,050</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Downside^</td><td>22.60</td><td>nc</td><td>30.5</td><td>4.3</td><td>34.8</td><td>Dec-25</td><td>2.468</td><td>nc</td><td>2.694</td><td>nc</td></tr><tr><td>Tigermed</td><td>3347.HK</td><td>HK$</td><td>37.54</td><td>47,524</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Upside^</td><td>73.00</td><td>nc</td><td>94.5</td><td>0.5</td><td>95.0</td><td>Dec-25</td><td>1.175</td><td>nc</td><td>1.627</td><td>nc</td></tr><tr><td>Tigermed</td><td>300347.SZ</td><td>Rmb</td><td>50.180</td><td>41,017</td><td>21 Jul 15:00</td><td>1</td><td>nc</td><td>Upside^</td><td>67.000</td><td>nc</td><td>33.5</td><td>0.3</td><td>33.8</td><td>Dec-25</td><td>1.175</td><td>nc</td><td>1.627</td><td>nc</td></tr><tr><td>United Imaging</td><td>688271.SS</td><td>Rmb</td><td>114.520</td><td>94,383</td><td>21 Jul 15:00</td><td>1</td><td>nc</td><td>Downside^</td><td>175.000</td><td>nc</td><td>52.8</td><td>0.4</td><td>53.2</td><td>Dec-25</td><td>3.127</td><td>nc</td><td>4.130</td><td>nc</td></tr><tr><td>Wuxi AppTec</td><td>2359.HK</td><td>HK$</td><td>158.40</td><td>440,025</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Upside^</td><td>183.00</td><td>nc</td><td>15.5</td><td>1.5</td><td>17.0</td><td>Dec-25</td><td>6.634</td><td>nc</td><td>8.009</td><td>nc</td></tr><tr><td>Wuxi AppTec</td><td>603259.SS</td><td>Rmb</td><td>126.450</td><td>379,781</td><td>21 Jul 15:00</td><td>1</td><td>nc</td><td>Upside^</td><td>160.000</td><td>nc</td><td>26.5</td><td>1.6</td><td>28.1</td><td>Dec-25</td><td>6.634</td><td>nc</td><td>8.009</td><td>nc</td></tr><tr><td>Wuxi Biologics</td><td>2269.HK</td><td>HK$</td><td>38.82</td><td>160,853</td><td>21 Jul 16:10</td><td>1</td><td>nc</td><td>Upside</td><td>42.00</td><td>nc</td><td>8.2</td><td>0.0</td><td>8.2</td><td>Dec-25</td><td>1.256</td><td>nc</td><td>1.474</td><td>nc</td></tr><tr><td>Yifeng Pharmacy Chain</td><td>603939.SS</td><td>Rmb</td><td>21.660</td><td>26,260</td><td>21 Jul 15:00</td><td>1</td><td>nc</td><td>Upside^</td><td>34.000</td><td>nc</td><td>57.0</td><td>3.8</td><td>60.8</td><td>Dec-25</td><td>1.588</td><td>nc</td><td>1.752</td><td>nc</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High RiskSource: Citi</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change ^Catalyst Watch</td></tr></table>

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="4">Last Reported Year</td><td></td><td colspan="4">Current Fiscal Year</td><td></td><td colspan="4">Next Fiscal Year</td><td></td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>3SBio</td><td>1530.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3.534</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.033</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.949</td></tr><tr><td>Huadong Medicine</td><td>000963.SZ</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.946</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.323</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.718</td></tr><tr><td>MicroPort MedBot</td><td>2252.HK</td><td>Dec-25</td><td>f</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-24</td><td>-</td><td>-</td><td>-</td><td>-</td><td>11</td><td>-</td><td>-</td><td>-</td><td>-</td><td>39</td></tr><tr><td>Pharmaron</td><td>3759.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.939</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.196</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.502</td></tr><tr><td rowspan="2">Ping AN Healthcare and Technology</td><td>1833.HK</td><td>Dec-25</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.182</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.221</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.319</td></tr><tr><td></td><td></td><td>Rmb</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shandong Weigao Group</td><td>1066.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.296</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.335</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.365</td></tr><tr><td>Sino Biopharmaceutical</td><td>1177.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.130</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.186</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.206</td></tr><tr><td>Sinopharm Group</td><td>1099.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.293</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.468</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.694</td></tr><tr><td>Tigermed</td><td>3347.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.037</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.175</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.627</td></tr><tr><td>Tigermed</td><td>300347.SZ</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.037</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.175</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.627</td></tr><tr><td>United Imaging</td><td>688271.SS</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.268</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3.127</td><td>-</td><td>-</td><td>-</td><td>-</td><td>4.130</td></tr><tr><td>Wuxi AppTec</td><td>2359.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>6.610</td><td>-</td><td>-</td><td>-</td><td>-</td><td>6.634</td><td>-</td><td>-</td><td>-</td><td>-</td><td>8.009</td></tr><tr><td>Wuxi AppTec</td><td>603259.SS</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>6.610</td><td>-</td><td>-</td><td>-</td><td>-</td><td>6.634</td><td>-</td><td>-</td><td>-</td><td>-</td><td>8.009</td></tr><tr><td>Wuxi Biologics</td><td>2269.HK</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.175</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.256</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.474</td></tr><tr><td>Yifeng Pharmacy Chain</td><td>603939.SS</td><td>Dec-25</td><td>Rmb</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.360</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.588</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.752</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

Healthcare Service: ASP pressure stabilizes; consumer spending sluggish — For Hygeia, we expect revenue miss but earnings beat, as margin improvement on efficiency gains and ASP stabilization. Jinxin should be in-line, with Chengdu performance remaining sluggish despite Shenzhen and US recovery. Aier is likely to miss as surgery volume slowed from May and a one-off tax payment pressured margins. Gushengtang should be in-line; patient volume sustained 15%+ YoY growth in 2Q26 though ASP was slightly dragged by consumer health mix. PAGD's revenue could miss while net profit might be inline on margin improvement. Topchoice should be broadly in-line.

Medical Aesthetics: consumption headwinds persist — Imeik is likely to miss on net profit as core product (Hearty, CureWhite) sales pressure was worse than expected with associated margin contraction. We think Bloomage will miss as weak consumption continued particularly in skincare.

TCM: overall lackluster 1H26E — CR999 and Tasly reported 1H26 preliminary results with weak toplines; Tasly delivered strong net profit growth driven by higher GM, while CR999's net profit was dragged by net loss of KPC. DEEJ is likely to miss due to mild Ejiao series growth in 2Q26 despite a relatively low base.

Figure 1. 1H26 China Healthcare Earnings Preview

<table><tr><td>Company Code</td><td>Company Name</td><td>Result Date</td><td>Citi Rating</td><td>TP</td><td>Currency</td><td>Market 1H26E Revenue</td><td>Actual 1H25 Revenue</td><td>Market 1H26E Revenue YoY</td><td>Market 1H26E Net Profit</td><td>Actual 1H25 Net Profit</td><td>Market 1H26E Net profit YoY</td><td>Versus Market</td><td>Citi Comment on 1H26E results</td></tr><tr><td>603259 CH Equity/2359 HK Equity</td><td>Wuxi Apptec-A/H</td><td>8/3/2026</td><td>Buy</td><td>Rmb160/ HK$183</td><td>Rmbm</td><td>25,096</td><td>20,799</td><td>20.7%</td><td>8,799</td><td>8,561</td><td>2.8%</td><td>Adj. net profit beat.</td><td>Strong top line growth persists with higher margin; Net profit miss on higher-than-expected FX loss; Adj. net profit likely to beat.</td></tr><tr><td>1093 HK Equity</td><td>CSPC</td><td>8/14/2026 *</td><td>Buy</td><td>11.5</td><td>Rmbm</td><td>13,913</td><td>13,273</td><td>4.8%</td><td>2,457</td><td>2,548</td><td>-3.6%</td><td>Inline</td><td>Moderate impact from anti-corruption campaign; US$1.2bn upfront from AZ recognized in 2Q26</td></tr><tr><td>1099 HK Equity</td><td>Sinopharm</td><td>8/14/2026 *</td><td>Buy</td><td>22.6</td><td>Rmbm</td><td>289,574</td><td>286,043</td><td>1.2%</td><td>3,633</td><td>3,466</td><td>4.8%</td><td>Miss</td><td>Greater-than-expected pressure from medical insurance budgeting and local government fiscal constraints</td></tr><tr><td>1177 HK Equity</td><td>Sino Biopharm</td><td>8/14/2026 *</td><td>Buy</td><td>10.0</td><td>Rmbm</td><td>18,592</td><td>17,575</td><td>5.8%</td><td>2,132</td><td>3,389</td><td>-37.1%</td><td>Beat</td><td>Rev: moderate impact from anti-corruption campaign in 2Q26; Profit: lower selling expense ratio, $135mn upfront fee from Sanofi booked in 1H26</td></tr><tr><td>600763 CH Equity</td><td>Topchoice</td><td>8/14/2026</td><td>Sell/H</td><td>30.0</td><td>Rmbm</td><td>1,513</td><td>1,448</td><td>4.5%</td><td>317</td><td>321</td><td>-1.3%</td><td>Inline</td><td>We believe the flattish trend will continue</td></tr><tr><td>1833 HK Equity</td><td>PAGD</td><

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be

reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
