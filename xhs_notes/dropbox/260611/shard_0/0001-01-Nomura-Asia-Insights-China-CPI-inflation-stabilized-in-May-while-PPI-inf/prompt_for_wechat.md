你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China: CPI inflation stabilized in May while PPI inflation rose further

CPI inflation stabilized at 1.2% y-o-y in May, unchanged from April and slightly missing expectations (Consensus: 1.3%; NOM: 1.4%). PPI inflation rose further to 3.9% y-o-y in May from 2.8% in April, in line with expectations (Consensus: 3.9%; NOM: 4.0%).

Despite the boost from the energy component, CPI inflation remained flat, weighed on by food and core prices. According to the NBS, energy prices contributed more than half of headline CPI inflation in May. Core prices were dragged lower by services prices, despite some emerging support from consumer electronic products due to rising chip prices. Meanwhile, food prices remained a serious drag, as pork prices failed to rebound after hitting a 16-year low.

We estimate price inflation in energy and AI-related materials together boosted headline PPI inflation in May (3.9% y-o-y) by 3.96pp, excluding which PPI inflation would have been negative. We estimate oil-related industries, which account for around 14% of the PPI basket, boosted May PPI inflation by 1.90pp. Amid global demand for AI-related products and electrification demand, non-ferrous mining and processing industries contributed 1.80pp to headline PPI inflation, and tech manufacturing industries contributed 0.26pp to headline PPI inflation.

## Raising PPI and CPI inflation forecasts

Since our latest upward revision to inflation forecasts in early March, oil prices have surged to new highs. Despite the recent easing of inflation in sequential terms, prices remain elevated and supply disruptions remain intact, boosting headline inflation by raising manufacturing costs in oil-related industries and domestic retail fuel prices. At the same time, the ongoing AI supercycle is also exerting upward pressure on the prices of technology products.

In light of these latest developments, we raise our quarterly PPI inflation forecasts to 3.8% y-o-y, 4.5% and 2.2% for Q2-Q4, respectively, up from 2.4%, 1.5% and 1.0%. Our 2026 full-year forecast for PPI inflation is thus lifted to 2.5% from 1.0%. We also raise our quarterly forecasts for CPI inflation to 1.2% y-o-y, 0.5% and 0.5% for Q2-Q4, respectively, from 0.9%, 0.5% and 0.3%, with our full-year CPI forecast lifted to 0.9% from 0.6%.

## Beijing will not become complacent following the end of deflation

Although Beijing might have breathed a sigh of relief when deflation finally ended, it may not take much comfort, as China is a net importer of chips and the world's biggest net importer of energy. The worsening terms of trade could shrink its balance of payments at a macro level and squeeze most domestic producers and consumers. The broad-based disappointment from April activity data underscores that externally led reflation cannot extricate China from its economic woes. Household consumption, already sapped by payback effects from the trade-in program and the perennial property bust, could be further curtailed by supply-driven reflation, while industrial production could be impaired by supply disruptions from energy and chemical raw materials. We expect Beijing to maintain accommodative monetary policy and ramp up fiscal spending to boost domestic demand in coming months. That said, given flush market liquidity and falling CGB yields, we have pushed out our forecast for RRR and rate cuts to next year.

## Our forecast for June inflation data

We expect CPI inflation to remain flat at 1.2% y-o-y in June, as a smaller drag from food prices largely offset the smaller boost from energy prices. High-frequency data show that MARA agricultural food prices rebounded to 0.3% y-o-y in month-to-date June from -0.7% in May, primarily driven by egg and chicken prices, while pork prices remained subdued. On the energy front, the NDRC cut retail petrol prices by RMB525 per tonne in month-to-date June in response to a sequential easing of global oil prices, in contrast to the RMB325 per tonne hike in June last year. This could lessen the boost to the CPI basket

## Research Analysts

Asia Economics

Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

from the energy category.

We expect PPI inflation to rise further to $4.7\%$ y-o-y in June, in view of the continued pass-through from elevated global oil and chip prices, as well as a low base from last year. Brent oil prices eased to $37.7\%$ y-o-y in month-to-date June from $68.3\%$ in May and $77.9\%$ in April, partly driven by a high base from last year due to geopolitical tensions. Despite some easing in oil prices, supply disruptions to raw material industries remain intact, which continue to exert upward pressure to headline PPI inflation.

In addition to global oil prices, rising chip prices have become an emerging force exerting upward pressure on PPI inflation. The surge in chip prices passes through to headline PPI through two channels: 1) directly raising domestic producer prices of semiconductor products, including memory chips and SoCs; and 2) raising producer prices of electronic products that use chips as inputs, including laptops, smartphones and AI appliances. Both channels are reflected in the PPI inflation of the "computers, communication equipment and other electronic equipment manufacturing sector".

## CPI inflation stabilized in May

CPI inflation was unchanged at 1.2% y-o-y in May, slightly below market expectations (Consensus: 1.3%; NOM: 1.4%). In sequential terms, CPI inflation fell to -0.1% m-o-m in May from 0.3% in April (May 2025: -0.2%). Amid elevated global oil prices and a low base, gasoline prices increased by 23.5% y-o-y in May, accounting for about half of headline CPI inflation. Food remains a clear drag, with its inflation at -1.7% y-o-y in May, down from -1.6% in April, while nonfood inflation edged up to 1.9% y-o-y in May from 1.8% y-o-y in April. Excluding food and energy, core CPI inflation inched down to 1.1% y-o-y in May from 1.2% in April. Services CPI inflation also moderated to 0.8% y-o-y in May from 0.9% in April.

## Oil price inflation rose further on a low base, despite reduced sequential momentum

Amid a slight easing of inflationary pressures from global oil prices, domestic gasoline prices fell by $0.3\%$ m-o-m in May, following the $12.6\%$ increase in April, with its contribution to headline CPI inflation declining to $-0.01\mathrm{pp}$ in May from 0.39pp in April. Due to a low base, gasoline price inflation increased further to $23.5\%$ y-o-y in May from $19.3\%$ in April, contributing 0.66pp to headline inflation, up from 0.56pp in April and 0.11pp in March.

## Gold's contribution is moderating

Prices of gold-related products increased by $39.0\%$ y-o-y in May, down further from increases of $46.9\%$ in April, $65.8\%$ in March, $76.6\%$ in February and $77.4\%$ in January. As the weighting of gold in the core CPI basket is about $0.6\%$ (see China: A more realistic picture of core CPI inflation after excluding gold, 26 December 2025), we estimate gold contributed 0.23pp y-o-y to core CPI inflation. Thus, excluding gold, core CPI inflation is still around $0.9\%$ y-o-y in May, unchanged from April.

## Pork remains a substantial drag

Among food, pork remains the largest drag. Pork inflation fell further to $-16.1\%$ y-o-y in May from $-15.2\%$ in April and $-11.5\%$ in March, contributing a -0.31pp to headline CPI inflation. Given the abundant pork supply and weak domestic demand, pork prices should remain under pressure in the near term. According to the MARA, the latest data show that growth in the number of hogs slaughtered rebounded to $26.7\%$ y-o-y in April from $14.7\%$ in March.

## Other key items

Due to the seasonal decline in travels after the Labour Day holiday, prices of vehicle rentals and flight tickets shifted from increases of 8.6% m-o-m and 29.2%, respectively, in April to decreases of 6.8% and 6.3% in May, contributing a combined -0.04pp to headline CPI inflation. Owing to reduced production capacity and a supply shortage, egg prices rose by 6.1% m-o-m, with their contribution to headline CPI inflation at 0.03pp. With strong demand for AI-related products, prices of mobile phones and tablet computers increased modestly by 1.6% m-o-m and 1.1%, respectively, in May.

## PPI inflation rose strongly in May

PPI inflation surged to 3.9% y-o-y in May from 2.8% in April, in line with market expectations (Consensus: 3.9%; NOM: 4.0%). This marks three consecutive months of positive PPI readings and the highest monthly reading since July 2022, driven by the

ongoing global energy shock caused by the double blockade of the Strait of Hormuz. Sequential PPI inflation slowed to $0.5\%$ m-o-m in May from $1.7\%$ in April, suggesting some inflationary pressures are moderating.

The rise in PPI inflation was concentrated entirely in upstream sectors, while prices in downstream sectors remained subdued, which shows inflationary pressures are not yet broadening across the economy. Markets should interpret the strong reading with a certain degree of caution.

PPI inflation in upstream sectors improved to 5.2% y-o-y in May from 3.8% in April, contributing 4.08pp to the headline PPI inflation reading. Within upstream sectors, PPI inflation across mining and raw materials sectors increased strongly to 15.8% y-o-y and 9.2% y-o-y, respectively, in May from 10.6% and 7.1% in April. However, PPI inflation in the manufacturing sector rose only moderately to 2.3% y-o-y in May from 1.5% in April, notably lagging the increase in headline PPI inflation. For downstream sectors (consumer goods), PPI inflation remained negative at -0.8% y-o-y in May, albeit up slightly from -1.0% in April, signalling still-muted price pressures on the consumer side.

In specific sectors, PPI inflation in the petroleum and natural gas extraction industry surged further to $35.7\%$ y-o-y in May from $28.6\%$ in April. PPI inflation in petroleum, coal and other fuel processing increased to $18.4\%$ y-o-y in May from $14.2\%$ in April. PPI inflation in the ferrous and non-ferrous metals smelting and pressing sectors improved slightly to $1.0\%$ y-o-y and $24.0\%$ y-o-y, respectively, in May from $-1.1\%$ and $22.5\%$ in April.

According to the NBS, non-ferrous metal mining (36.5% y-o-y), non-ferrous metal smelting and pressing (24.0%), coal mining and washing (10.0%), electrical machinery and equipment manufacturing (4.5%), computer, communications and other electronic equipment manufacturing (2.1%), and ferrous metal smelting and rolling (1.0%) together contributed 2.56pp to headline PPI in May, 0.51pp more than in April. On external factors, rising global crude oil prices have pushed up prices in domestic petroleum-related industries. Oil and natural gas extraction (35.7% y-o-y), petroleum/coal and other fuel processing increased (18.4%), and chemical raw materials and chemical products manufacturing (12.7%) contributed around 1.96pp to the year-on-year PPI increase in May, 0.46pp more than in April.

Fig. 1: Selected sector breakdown and contribution of PPI inflation

<table><tr><td>Categories</td><td>Weight %</td><td>Contribution (May) pp</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td></tr><tr><td colspan="8">PPI</td></tr><tr><td colspan="8">Oil-related</td></tr><tr><td>Petroleum &amp; Natural Gas Mining</td><td>0.8</td><td>0.29</td><td>35.7</td><td>28.6</td><td>5.2</td><td>-12.9</td><td>-16.7</td></tr><tr><td>Petroleum, Coal and Other Fuel Processing</td><td>3.8</td><td>0.71</td><td>18.4</td><td>14.2</td><td>-4.5</td><td>-12.0</td><td>-11.5</td></tr><tr><td>Chemical Material &amp; Product Manufacturing</td><td>6.5</td><td>0.83</td><td>12.7</td><td>8.9</td><td>-0.3</td><td>-3.7</td><td>-5.0</td></tr><tr><td>Chemical Fiber Manufacturing</td><td>0.7</td><td>0.06</td><td>8.5</td><td>5.4</td><td>-2.3</td><td>-6.0</td><td>-6.4</td></tr><tr><td>Rubber &amp; Plastic Product Manufacturing</td><td>2.2</td><td>0.01</td><td>0.5</td><td>-1.3</td><td>-3.4</td><td>-4.2</td><td>-4.1</td></tr><tr><td colspan="8">Non-ferrous-related</td></tr><tr><td>Non Ferrous Metal Mining</td><td>0.3</td><td>0.11</td><td>36.5</td><td>38.9</td><td>36.4</td><td>30.2</td><td>22.7</td></tr><tr><td>Non Ferrous Metal Smelting &amp; Pressing</td><td>7.0</td><td>1.69</td><td>24.0</td><td>22.5</td><td>22.4</td><td>22.1</td><td>17.1</td></tr><tr><td colspan="8">Ferrous-related</td></tr><tr><td>Ferrous Metal Mining</td><td>0.3</td><td>0.01</td><td>3.3</td><td>1.3</td><td>0.1</td><td>1.0</td><td>3.0</td></tr><tr><td>Ferrous Metal Smelting &amp; Pressing</td><td>5.6</td><td>0.06</td><td>1.0</td><td>-1.1</td><td>-2.5</td><td>-3.4</td><td>-3.7</td></tr><tr><td colspan="8">Coal-related</td></tr><tr><td>Coal Mining</td><td>1.9</td><td>0.19</td><td>10.0</td><td>3.1</td><td>-2.2</td><td>-7.0</td><td>-9.8</td></tr><tr><td>Non-metal Mineral Smelting &amp; Pressing</td><td>0.3</td><td>-0.01</td><td>-3.4</td><td>-4.1</td><td>-4.2</td><td>-5.0</td><td>-4.6</td></tr><tr><td>Non-metal Mineral Product Manufacturing</td><td>3.3</td><td>-0.17</td><td>-5.1</td><td>-5.5</td><td>-4.9</td><td>-4.9</td><td>-5.4</td></tr><tr><td colspan="8">Selected manufacturing products</td></tr><tr><td>Computer, Communication &amp; Other Electronic Equipment Manufacturing</td><td>12.5</td><td>0.26</td><td>2.1</td><td>1.5</td><td>0.4</td><td>-0.9</td><td>-1.6</td></tr><tr><td>Electrical Machinery &amp; Equipment Manufacturing</td><td>8.4</td><td>0.00</td><td>0.0</td><td>3.6</td><td>3.2</td><td>2.0</td><td>0.8</td></tr><tr><td>Automobile Manufacturing</td><td>8.0</td><td>-0.16</td><td>-2.0</td><td>-2.0</td><td>-2.5</td><td>-2.4</td><td>-2.5</td></tr><tr><td>Fabricated Metal Product Manufacturing</td><td>3.4</td><td>0.03</td><td>0.8</td><td>0.5</td><td>0.2</td><td>-0.2</td><td>-0.7</td></tr><tr><td>General Equipment Manufacturing</td><td>3.7</td><td>-0.03</td><td>-0.9</td><td>-1.0</td><td>-1.2</td><td>-1.1</td><td>-1.3</td></tr><tr><td>Special Equipment Manufacturing</td><td>2.8</td><td>0.00</td><td>0.0</td><td>-0.9</td><td>-1.0</td><td>-1.0</td><td>-0.9</td></tr><tr><td>Rail, Ship, Aircraft &amp; Other Transport Equipment Manufacturing</td><td>1.3</td><td>0.00</td><td>-0.3</td><td>-0.3</td><td>-0.1</td><td>-0.3</td><td>-0.3</td></tr></table>

Note: Sector weight is calculated by their 2025 industrial revenue.  
Source: Wind, NOM Global Economics.

Fig. 2: A breakdown of inflation by major component

<table><tr><td rowspan="2">Categories</td><td colspan="7">% y-o-y</td></tr><tr><td>May 26</td><td>Apr 26</td><td>Mar 26</td><td>Q1 26</td><td>Q4 25</td><td>2025</td><td>2024</td></tr><tr><td>CPI</td><td>1.2</td><td>1.2</td><td>1.0</td><td>0.9</td><td>0.6</td><td>0.0</td><td>0.2</td></tr><tr><td>Food</td><td>-1.7</td><td>-1.6</td><td>0.3</td><td>0.4</td><td>-0.5</td><td>-1.5</td><td>-0.6</td></tr><tr><td>Grain</td><td>-0.3</td><td>-0.3</td><td>-0.3</td><td>-0.3</td><td>-0.5</td><td>-1.0</td><td>-0.1</td></tr><tr><td>Vegetable</td><td>1.6</td><td>-0.5</td><td>4.9</td><td>7.6</td><td>8.5</td><td>-3.9</td><td>5.0</td></tr><tr><td>Pork</td><td>-16.1</td><td>-15.2</td><td>-11.5</td><td>-11.3</td><td>-15.2</td><td>-6.1</td><td>7.7</td></tr><tr><td>Aquatic</td><td>0.6</td><td>1.3</td><td>3.7</td><td>3.5</td><td>1.7</td><td>1.4</td><td>1.0</td></tr><tr><td>Egg</td><td>6.6</td><td>0.5</td><td>-3.1</td><td>-5.2</td><td>-12.3</td><td>-7.4</td><td>-4.4</td></tr><tr><td>Milk</td><td>-1.2</td><td>-1.2</td><td>-0.7</td><td>-0.9</td><td>-1.7</td><td>-1.5</td><td>-1.6</td></tr><tr><td>Fruit</td><td>-2.2</td><td>-1.0</td><td>4.0</td><td>4.3</td><td>1.0</td><td>1.2</td><td>-3.5</td></tr><tr><td>Non-Food</td><td>1.9</td><td>1.8</td><td>1.2</td><td>0.9</td><td>0.8</td><td>0.4</td><td>0.4</td></tr><tr><td>Apparel</td><td>1.4</td><td>1.5</td><td>1.6</td><td>1.8</td><td>1.8</td><td>1.5</td><td>1.4</td></tr><tr><td>Residence</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>0.0</td><td>0.1</td><td>0.1</td></tr><tr><td>Household articles &amp; services</td><td>1.8</td><td>1.4</td><td>1.5</td><td>2.3</td><td>2.1</td><td>0.9</td><td>0.5</td></tr><tr><td>Transportation and communication</td><td>5.4</td><td>4.6</td><td>0.9</td><td>-1.1</td><td>-2.1</td><td>-2.6</td><td>-1.9</td></tr><tr><td>Education, culture and recreation</td><td>1.3</td><td>1.3</td><td>1.1</td><td>1.0</td><td>0.9</td><td>0.8</td><td>1.5</td></tr><tr><td>Medicine and healthcare services</td><td>2.1</td><td>2.2</td><td>1.9</td><td>1.8</td><td>1.6</td><td>0.8</td><td>1.3</td></tr><tr><td>Other goods and services</td><td>9.9</td><td>11.0</td><td>13.5</td><td>14.1</td><td>14.8</td><td>9.3</td><td>3.8</td></tr><tr><td>Goods</td><td>1.6</td><td>1.4</td><td>1.3</td><td>0.9</td><td>0.5</td><td>-0.3</td><td>-0.1</td></tr><tr><td>Services</td><td>0.8</td><td>0.9</td><td>0.8</td><td>0.8</td><td>0.7</td><td>0.5</td><td>0.7</td></tr><tr><td>Core CPI (excluding food and energy)</td><td>1.1</td><td>1.2</td><td>1.1</td><td>1.2</td><td>1.2</td><td>0.7</td><td>0.5</td></tr><tr><td>PPI</td><td>3.9</td><td>2.8</td><td>0.5</td><td>-0.6</td><td>-2.1</td><td>-2.6</td><td>-2.2</td></tr><tr><td>Upstream</td><td>5.2</td><td>3.8</td><td>1.0</td><td>-0.3</td><td>-2.3</td><td>-3.0</td><td>-2.5</td></tr><tr><td>Mining</td><td>15.8</td><td>10.6</td><td>2.0</td><td>-3.8</td><td>-6.2</td><td>-9.0</td><td>-2.9</td></tr><tr><td>Raw materials</td><td>9.2</td><td>7.1</td><td>1.1</td><td>-0.9</td><td>-2.7</td><td>-3.4</td><td>-1.7</td></tr><tr><td>Manufacturing</td><td>2.3</td><td>1.5</td><td>0.9</td><td>0.3</td><td>-1.8</td><td>-2.4</td><td>-2.9</td></tr><tr><td>Downdstream</td><td>-0.8</td><td>-1.0</td><td>-1.3</td><td>-1.5</td><td>-1.4</td><td>-1.5</td><td>-1.1</td></tr><tr><td>Food</td><td>-1.8</td><td>-1.9</td><td>-1.7</td><td>-1.8</td><td>-1.5</td><td>-1.6</td><td>-1.1</td></tr><tr><td>Apparel</td><td>-1.0</td><td>-1.1</td><td>-1.1</td><td>-0.9</td><td>-0.2</td><td>-0.1</td><td>-0.1</td></tr><tr><td>Daily articles</td><td>-1.0</td><td>-1.1</td><td>-1.4</td><td>-1.7</td><td>1.2</td><td>0.8</td><td>0.0</td></tr><tr><td>Durable goods</td><td>0.0</td><td>-0.3</td><td>-1.0</td><td>-1.5</td><td>-3.4</td><td>-3.3</td><td>-2.2</td></tr></table>

Source: NBS, Wind, NOM Global Economics

Fig. 3: CPI and PPI inflation  
![](images/1fae4aeae46008c61e7cde8827fd0ccea88aa9a9df86cef2ecd5449493072526.jpg)

<details>
<summary>line chart</summary>

| Date   | CPI inflation | PPI inflation |
|--------|---------------|---------------|
| May-16 | 2.0           | -3.0          |
| May-17 | 1.5           | 8.0           |
| May-18 | 2.0

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
