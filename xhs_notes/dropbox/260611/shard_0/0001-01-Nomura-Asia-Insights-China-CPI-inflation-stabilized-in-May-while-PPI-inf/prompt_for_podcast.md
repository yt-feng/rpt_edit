你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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
