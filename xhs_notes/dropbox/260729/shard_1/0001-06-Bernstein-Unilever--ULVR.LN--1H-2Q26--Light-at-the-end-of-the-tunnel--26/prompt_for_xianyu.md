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
European Food
Unilever

Rating
Outperform

Price Target

ULVR.LN 5,800.00 GBp

UNA.NA 66.90 EUR

![](images/a48fe9bfdd04fcd30a5081645ee3d326ec83f86f955f6850df9f3c9ab780679d.jpg)

Callum Elliott, CFA, ACA
+44 20 7676 7183
callum.elliott@bernsteinsg.com

![](images/ebef9c0ad8f395ba197c06f1fed64353079c4bb5c91aaec7fbe8be90112f57af.jpg)

Victoria Nice, CFA
+44 20 7762 5862
victoria.nice@bernsteinsg.com

![](images/0f85519ad4023fe7afdd8da03fabb63b188ea98bb2965502912e4f1bbd874d4d.jpg)

![](images/61c5d520a9d7c0e449980fcbf83800e2e6cf8774ff3030dd8d43716f05045c66.jpg)

Henry Dennis
+44 20 7676 6776
henry.dennis@bernsteinsg.com

Simran Cheema
+44 20 7676 6705
simran.cheema@bernsteinsg.com

## Unilever (ULVR.LN) 1H/2Q26: Light at the end of the tunnel?

Unilever reported its 1H/2Q26 results this morning with a strong set of numbers. After a challenging eighteen months in the wake of the unexpected removal of former CEO Hein Schumacher, and the volatility induced by the spin-off of ice-cream and Foods sale, these much stronger than expected results seem likely to drive a significant uptick in positivity today, and perhaps even induce investors to look beyond the noise of the ongoing Foods sale process.

Q2 Organic sales growth at +5.8%, led by +5.5% volume growth. The group delivers a stark acceleration in volume and sales growth for the second quarter, up from +3.8% and +2.9% in Q1, respectively. This stark acceleration is dramatically ahead of consensus' forecasts, which had put OSG at 4.1%, and had foreseen a slowdown in volume growth for the quarter. We can't remember the last time one of our Staples coverage companies beat consensus volume estimates by 300+bps! Importantly, at a divisional level, the strength is driven by the HPC business that will remain in the wake of the Foods sale. "HPCCo" delivers an impressive +7.6% OSG, and beats on organic volume growth by over 400bps, with all HPC divisions much stronger than expected. By contrast, we expect that there will be some questions around performance of the Foods business, which is the only blot on the metaphorical copy book this quarter. On a regional basis, both developed and emerging markets see acceleration in the quarter, but India (+10%) and LatAm (+8.9%) are both notably strong, and North America sees a return to strong volume growth in the quarter following a couple of quarters of weakness. Margins are broadly in-line with expectations, leading to EBIT/EPS around 1% ahead of consensus.

Following the very strong Q2, FY Guidance is raised. Previously management had steered OSG to the bottom end of the long-term 4-6% range, with volume volumes at around 2%. Now volume growth guidance is raised to around 3%, and the emphasis on the low-end of the 4-6% range is removed. 2H growth is expected to be in the 4-5% range, and more skewed to pricing, which makes sense in the current cost environment we think.

On net, the big volume acceleration is exactly what Staples investors have been impatiently waiting for over the past two years, and whilst there may be some questions about its sustainability, we expect it to drive a positive share price reaction today.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>ULVR.LN (EUR)</td><td>3.08</td><td>3.23</td><td>3.45</td></tr><tr><td>UNA.NA (EUR)</td><td>3.08</td><td>3.23</td><td>3.45</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Close Date</td><td></td><td></td><td colspan="2">27 Jul 2026</td></tr><tr><td>ULVR.LN Close Price (GBp)</td><td></td><td></td><td colspan="2">4,627.00</td></tr><tr><td>Price Target (GBp)</td><td></td><td></td><td colspan="2">5,800.00</td></tr><tr><td>Upside/(Downside)</td><td></td><td></td><td colspan="2">25%</td></tr><tr><td>52-Week Range</td><td></td><td colspan="3">5,525.00/4,068.00</td></tr><tr><td>EDME</td><td></td><td></td><td colspan="2">--</td></tr><tr><td>FYE</td><td></td><td></td><td colspan="2">Dec</td></tr><tr><td>Div Yield</td><td></td><td></td><td colspan="2">3.5%</td></tr><tr><td>Market Cap (GBP) (M)</td><td></td><td></td><td colspan="2">99,678</td></tr><tr><td>EV (GBp) (M)</td><td></td><td></td><td colspan="2">141,785</td></tr><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(4.8)</td><td>0.6</td><td>(4.9)</td><td>(3.4)</td></tr><tr><td>EDME (%)</td><td></td><td></td><td></td><td></td></tr><tr><td>Relative (%)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Source: Bloomberg, Bernstein estimates and analysis.</td></tr></table>

Price Performance, 1YR

![](images/60892095db26c2d01472a44747f770e37a98d04aaec9abecb5b563260d512015.jpg)

<table><tr><td>Valuation Metrics</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>EV/EBITDA (x)</td><td>13.9</td><td>13.8</td><td>12.9</td></tr><tr><td>Adjusted P/E (x)</td><td>17.6</td><td>16.8</td><td>15.7</td></tr><tr><td>Div Yield (%)</td><td>3.4</td><td>3.6</td><td>3.8</td></tr></table>

## KEY NUMBERS:

Q2 Group organic growth of +5.8% came in +171bps ahead of consensus at +4.1%.

Q2 Group sales of EUR 13,046 million was +1.3% ahead of consensus at EUR 12,880 million.

EXHIBIT 1: ULVR Q2 sales summary versus consensus and Bernstein expectations

<table><tr><td>ULVR Q2 sales summary</td><td>2Q25</td><td>2Q26</td><td>YoY Δ</td><td>Consensus 2Q26</td><td>Δ</td><td>Bernstein 2Q26</td><td>Δ</td></tr><tr><td>Group (EUR m)</td><td>12,567</td><td>13,046</td><td>3.8%</td><td>12,880</td><td>1.3%</td><td>12,992</td><td>0.4%</td></tr><tr><td>Group (organic growth)</td><td>3.1%</td><td>5.8%</td><td>+270 bps</td><td>4.1%</td><td>+171 bps</td><td>4.3%</td><td>+153 bps</td></tr><tr><td>Price growth</td><td>2.1%</td><td>0.2%</td><td>-190 bps</td><td>1.7%</td><td>-148 bps</td><td>1.5%</td><td>-132 bps</td></tr><tr><td>Volume growth</td><td>1.1%</td><td>5.5%</td><td>+440 bps</td><td>2.4%</td><td>+310 bps</td><td>2.8%</td><td>+275 bps</td></tr><tr><td>Sales FX impact</td><td>-6.1%</td><td>-2.4%</td><td>+370 bps</td><td>-2.2%</td><td>-18 bps</td><td>-1.6%</td><td>-77 bps</td></tr><tr><td>Sales M&amp;A impact</td><td>-2.3%</td><td>0.6%</td><td>+290 bps</td><td>0.7%</td><td>-7 bps</td><td>0.8%</td><td>-20 bps</td></tr></table>

Prior year sales and growth stated ex. Ice Cream.  
Source: Company reports, Visible Alpha consensus, Bernstein analysis and estimates

EXHIBIT 2: Unilever H1 result summary vs consensus and Bernstein estimates

<table><tr><td>Unilever H1 result summary</td><td>2025 H1</td><td>2026 H1</td><td>YoY Δ</td><td>Consensus 1H26</td><td>Δ</td><td>Bernstein 1H26</td><td>Δ</td></tr><tr><td>Group Sales (€ m)</td><td>25,506</td><td>25,623</td><td>0.5%</td><td>25,475</td><td>0.6%</td><td>25,554</td><td>0.3%</td></tr><tr><td>Group Underl. Op. Profit (€ m)</td><td>5,148</td><td>5,193</td><td>0.9%</td><td>5,169</td><td>0.5%</td><td>5,148</td><td>0.9%</td></tr><tr><td>Group Underl. OPM (%)</td><td>20.2%</td><td>20.3%</td><td>8 bps</td><td>20.3%</td><td>-2 bps</td><td>20.1%</td><td>12 bps</td></tr><tr><td>Diluted Underlying EPS (€)</td><td>1.59</td><td>1.61</td><td>1.3%</td><td>1.59</td><td>1.3%</td><td>1.60</td><td>0.4%</td></tr></table>

PY sales and operating profit stated ex. Ice Cream. PY EPS as reported.
Source: Company reports, Visible Alpha consensus, Bernstein analysis and estimates

EXHIBIT 3: ULVR Q2 sales by product div. versus consensus and Bernstein expectations

<table><tr><td>ULVR Q2 sales by product div.</td><td>2Q25</td><td>2Q26</td><td>YoY Δ</td><td>Consensus 2Q26</td><td>Δ</td><td>Bernstein 2Q26</td><td>Δ</td></tr><tr><td>Group (EUR m)</td><td>12,567</td><td>13,046</td><td>3.8%</td><td>12,880</td><td>1.3%</td><td>12,992</td><td>0.4%</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>3,219</td><td>3,403</td><td>5.7%</td><td>3,290</td><td>3.4%</td><td>3,377</td><td>0.8%</td></tr><tr><td>Personal Care</td><td>3,296</td><td>3,535</td><td>7.3%</td><td>3,492</td><td>1.2%</td><td>3,392</td><td>4.2%</td></tr><tr><td>Home Care</td><td>2,865</td><td>3,009</td><td>5.0%</td><td>2,938</td><td>2.4%</td><td>2,997</td><td>0.4%</td></tr><tr><td>Foods</td><td>3,187</td><td>3,099</td><td>-2.8%</td><td>3,159</td><td>-1.9%</td><td>3,227</td><td>-4.0%</td></tr><tr><td>Group (organic growth)</td><td>3.1%</td><td>5.8%</td><td>+270 bps</td><td>4.1%</td><td>+171 bps</td><td>4.3%</td><td>+153 bps</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>3.4%</td><td>8.1%</td><td>+470 bps</td><td>4.6%</td><td>+353 bps</td><td>4.3%</td><td>+380 bps</td></tr><tr><td>Personal Care</td><td>4.5%</td><td>5.9%</td><td>+140 bps</td><td>4.9%</td><td>+103 bps</td><td>4.9%</td><td>+100 bps</td></tr><tr><td>Home Care</td><td>1.8%</td><td>9.1%</td><td>+730 bps</td><td>5.3%</td><td>+379 bps</td><td>5.5%</td><td>+360 bps</td></tr><tr><td>Foods</td><td>2.8%</td><td>0.2%</td><td>-260 bps</td><td>2.2%</td><td>-198 bps</td><td>2.5%</td><td>-230 bps</td></tr><tr><td>Group (Price Growth)</td><td>2.1%</td><td>0.2%</td><td>-190 bps</td><td>1.7%</td><td>-148 bps</td><td>1.5%</td><td>-132 bps</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>2.4%</td><td>1.1%</td><td>-130 bps</td><td>1.7%</td><td>-62 bps</td><td>1.6%</td><td>-50 bps</td></tr><tr><td>Personal Care</td><td>4.3%</td><td>-0.9%</td><td>-520 bps</td><td>2.5%</td><td>-336 bps</td><td>2.4%</td><td>-330 bps</td></tr><tr><td>Home Care</td><td>0.4%</td><td>0.5%</td><td>+10 bps</td><td>1.5%</td><td>-105 bps</td><td>1.0%</td><td>-50 bps</td></tr><tr><td>Foods</td><td>1.0%</td><td>0.2%</td><td>-80 bps</td><td>1.1%</td><td>-93 bps</td><td>1.0%</td><td>-80 bps</td></tr><tr><td>Group (Volume Growth)</td><td>1.1%</td><td>5.5%</td><td>+440 bps</td><td>2.4%</td><td>+310 bps</td><td>2.8%</td><td>+275 bps</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>1.0%</td><td>6.9%</td><td>+590 bps</td><td>2.8%</td><td>+409 bps</td><td>2.7%</td><td>+420 bps</td></tr><tr><td>Personal Care</td><td>0.2%</td><td>6.8%</td><td>+660 bps</td><td>2.4%</td><td>+442 bps</td><td>2.5%</td><td>+430 bps</td></tr><tr><td>Home Care</td><td>1.3%</td><td>8.6%</td><td>+730 bps</td><td>3.7%</td><td>+487 bps</td><td>4.5%</td><td>+410 bps</td></tr><tr><td>Foods</td><td>1.7%</td><td>-0.1%</td><td>-180 bps</td><td>1.0%</td><td>-113 bps</td><td>1.5%</td><td>-160 bps</td></tr></table>

Prior year sales and growth stated ex. Ice Cream.  
Source: Company reports, Visible Alpha consensus, Bernstein analysis and estimates

EXHIBIT 4: Unilever H1 results vs consensus and Bernstein estimates

<table><tr><td>Unilever H1 results</td><td>2025 H1</td><td>2026 H1</td><td>YoY Δ</td><td>Consensus 1H26</td><td>Δ</td><td>Bernstein 1H26</td><td>Δ</td></tr><tr><td>Group Sales (€ m)</td><td>25,506</td><td>25,623</td><td>0.5%</td><td>25,475</td><td>0.6%</td><td>25,554</td><td>0.3%</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>6,489</td><td>6,509</td><td>0.3%</td><td>6,405</td><td>1.6%</td><td>6,480</td><td>0.4%</td></tr><tr><td>Personal Care</td><td>6,545</td><td>6,817</td><td>4.2%</td><td>6,775</td><td>0.6%</td><td>6,670</td><td>2.2%</td></tr><tr><td>Home Care</td><td>5,904</td><td>5,992</td><td>1.5%</td><td>5,919</td><td>1.2%</td><td>5,974</td><td>0.3%</td></tr><tr><td>Foods</td><td>6,568</td><td>6,305</td><td>-4.0%</td><td>6,376</td><td>-1.1%</td><td>6,431</td><td>-2.0%</td></tr><tr><td>Group Underl. Op. Profit (€ m)</td><td>5,148</td><td>5,193</td><td>0.9%</td><td>5,169</td><td>0.5%</td><td>5,148</td><td>0.9%</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>1,256</td><td>1,269</td><td>1.0%</td><td>1,231</td><td>3.1%</td><td>1,251</td><td>1.5%</td></tr><tr><td>Personal Care</td><td>1,444</td><td>1,513</td><td>4.8%</td><td>1,518</td><td>-0.3%</td><td>1,467</td><td>3.1%</td></tr><tr><td>Home Care</td><td>915</td><td>944</td><td>3.2%</td><td>921</td><td>2.5%</td><td>938</td><td>0.7%</td></tr><tr><td>Foods</td><td>1,533</td><td>1,467</td><td>-4.3%</td><td>1,492</td><td>-1.7%</td><td>1,492</td><td>-1.7%</td></tr><tr><td>Group Underl. OPM (%)</td><td>20.2%</td><td>20.3%</td><td>8 bps</td><td>19.3%</td><td>93 bps</td><td>20.1%</td><td>12 bps</td></tr><tr><td>Beauty &amp; Wellbeing</td><td>19.4%</td><td>19.5%</td><td>14 bps</td><td>19.2%</td><td>26 bps</td><td>19.3%</td><td>20 bps</td></tr><tr><td>Personal Care</td><td>22.1%</td><td>22.2%</td><td>13 bps</td><td>22.3%</td><td>-14 bps</td><td>22.0%</td><td>19 bps</td></tr><tr><td>Home Care</td><td>15.5%</td><td>15.8%</td><td>26 bps</td><td>15.5%</td><td>22 bps</td><td>15.7%</td><td>6 bps</td></tr><tr><td>Foods</td><td>23.3%</td><td>23.3%</td><td>-7 bps</td><td>23.5%</td><td>-22 bps</td><td>23.2%</td><td>7 bps</td></tr></table>

PY sales and operating profit stated ex. Ice Cream.  
Source: Company reports, Visible Alpha consensus, Bernstein analysis and estimates

EXHIBIT 5: ULVR Q2 sales by region versus consensus

<table><tr><td>ULVR Q2 sales by region</td><td>2Q25</td><td>2Q26</td><td>YoY Δ</td><td>Consensus 2Q26</td><td>Δ</td><td>Bernstein 2Q26</td><td>Δ</td></tr><tr><td>Group (EUR m)</td><td>12,567</td><td>13,046</td><td>3.8%</td><td>12,880</td><td>1.3%</td><td></td><td></td></tr><tr><td>APA - Asia Pacific / Africa</td><td>5,531</td><td>5,694</td><td>2.9%</td><td>5,639</td><td>1.0%</td><td></td><td></td></tr><tr><td>Americas</td><td>4,680</td><td>5,067</td><td>8.3%</td><td>4,953</td><td>2.3%</td><td></td><td></td></tr><tr><td>Europe</td><td>2,356</td><td>2,285</td><td>-3.0%</td><td>2,369</td><td>-3.5%</td><td></td><td></td></tr><tr><td>Group (organic growth)</td><td>3.1%</td><td>5.8%</td><td>+270 bps</td><td>4.1%</td><td>+171 bps</td><td></td><td></td></tr><tr><td>APA - Asia Pacific / Africa</td><td>4.0%</td><td>8.8%</td><td>+480 bps</td><td>5.8%</td><td>+303 bps</td><td></td><td></td></tr><tr><td>Americas</td><td>2.8%</td><td>5.7%</td><td>+290 bps</td><td>5.1%</td><td>+64 bps</td><td></td><td></td></tr><tr><td>Europe</td><td>1.8%</td><td>-1.3%</td><td>-310 bps</td><td>0.4%</td><td>-174 bps</td><td></td><td></td></tr><tr><td>Group (Price Growth)</td><td>2.1%</td><td>0.2%</td><td>-190 bps</td><td>1.7%</td><td>-148 bps</td><td></td><td></td></tr><tr><td>APA - Asia Pacific / Africa</td><td>1.7%</td><td>1.5%</td><td>-20 bps</td><td>2.2%</td><td>-68 bps</td><td></td><td></td></tr><tr><td>Americas</td><td>3.5%</td><td>-0.5%</td><td>-400 bps</td><td>1.7%</td><td>-218 bps</td><td></td><td></td></tr><tr><td>Europe</td><td>-0.1%</td><td>-1.6%</td><td>-150 bps</td><td>0.9%</td><td>-251 bps</td><td></td><td></td></tr><tr><td>Group (Volume Growth)</td><td>1.1%</td><td>5.5%</td><td>+440 bps</td><td>2.4%</td><td>+310 bps</td><td></td><td></td></tr><tr><td>APA - Asia Pacific / Africa</td><td>2.2%</td><td>7.2%</td><td>+500 bps</td><td>3.6%</td><td>+364 bps</td><td></td><td></td></tr><tr><td>Americas</td><td>-0.7%</td><td>6.2%</td><td>+690 bps</td><td>3.3%</td><td>+286 bps</td><td></td><td></td></tr><tr><td>Europe</td><td>1.9%</td><td>0.3%</td><td>-160 bps</td><td>-0.5%</td><td>+77 bps</td><td></td><td></td></tr></table>

Prior year sales and growth stated ex. Ice Cream.  
Source: Company reports, Visible Alpha consensus, Bernstein analysis and estimates

## INVESTMENT IMPLICATIONS

We rate Unilever Outperform with a Price Target of GBp 5,800.00 / EUR 66.90.

## BERNSTEIN TICKER TABLE

<table><tr><td></td><td colspan="4">27 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">EV/EBITDA (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>ULVR.LN (Unilever)</td><td>O</td><td>GBp</td><td>4,627.00</td><td>5,800.00</td><td>(3.4)%</td><td>EUR</td><td>3.08</td><td>3.23</td><td>3.45</td><td>13.9</td><td>13.8</td><td>12.9</td></tr><tr><td>UNA.NA (Unilever)</td><td>O</td><td>EUR</td><td>54.10</td><td>66.90</td><td>(1.8)%</td><td>EUR</td><td>3.08</td><td>3.23</td><td>3.45</td><td>13.9</td

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
