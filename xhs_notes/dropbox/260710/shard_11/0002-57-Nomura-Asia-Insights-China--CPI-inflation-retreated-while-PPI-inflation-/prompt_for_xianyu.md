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
# Asia Insights

Economics - Asia ex-Japan

## China: CPI inflation retreated while PPI inflation climbed in June

CPI inflation slowed to 1.0% y-o-y in June from 1.2% in May, slightly missing expectations (Consensus: 1.1%; NOM: 1.2%). The decline in CPI inflation was led by external forces. Global oil and gold prices, which feed into the energy and core components of the CPI basket, retreated notably in June. According to the NBS, the combined boost from oil and gold to headline CPI inflation dropped by 0.23pp, declining to 0.60pp in June from 0.83pp y-o-y in May. This suggests that, excluding the impact of oil and gold, underlying CPI inflation remained largely stable at around 0.4% y-o-y.

PPI inflation climbed to 4.1% y-o-y in June from 3.9% in May, in line with expectations (Consensus: 4.1%; NOM: 4.0%). The rise was largely driven by a low base effect, while sequential PPI inflation turned negative amid falling global oil prices. In our sectoral contribution breakdown, we estimate that oil-related sectors, which account for around 14% of the PPI basket, boosted headline PPI inflation by 1.6pp in June, down from a 1.9pp boost in May. Non-ferrous sectors contributed 1.7pp to headline inflation in June, and chip-related tech manufacturing sectors contributed 0.4pp. Excluding the boost from energy and AI-related materials, we estimate underlying PPI inflation in June is around 0.6% y-o-y.

We revised up our 2026 CPI and PPI inflation forecasts in early June to $0.9\%$ and $2.5\%$ , respectively, from $0.6\%$ and $1.0\%$ , in view of the imported inflationary forces from global oil and chips. Since then, oil prices have retreated to near pre-war levels but sharply rebounded on 8 July due to reignited geopolitical tensions. While our inflation forecast depends heavily on the trajectories of whipsawing global oil prices, underlying inflation remains weak when excluding global commodity prices and chip prices. We expect Beijing to maintain an accommodative monetary policy and ramp up fiscal spending to boost domestic demand in coming months. That said, given flush market liquidity and low CGB yields, we maintain our forecast for no RRR and rate cuts this year.

## Our forecast for July inflation data

We expect CPI inflation to retreat further to 0.8% y-o-y in July, dragged by food prices and a smaller boost from energy and gold prices. High-frequency data show that MARA agricultural food prices fell to -2.3% y-o-y in month-to-date July from -0.4% in June, as egg prices retreated from recent peaks, while pork prices remained subdued. The NDRC cut retail petrol prices by RMB950 per tonne in early July, which contrasts with the RMB105 per tonne hike in July last year. This should lessen the energy boost to the CPI basket. That said, if the overnight oil prices surge sustains, the NDRC is likely to adjust petrol prices again later this month.

We expect PPI inflation to stay at $4.1\%$ y-o-y in July, as the global oil price retreat largely offsets a still-low base from last year. In year-on-year terms, Brent oil price inflation dropped notably to $0.5\%$ in month-to-date July from $19.8\%$ in June. In absolute terms, Brent oil prices stayed at pre-war levels at around USD70/bbl in the first week of July but spiked on 8 July to USD78/bbl due to reignited geopolitical tensions. If this sharp rebound in oil prices persists, it would represent an upside risk to our current forecast.

## Research Analysts

Asia Economics
Hannah Liu - NIHK
hannah.liu@NOM.com
+852 2252 1082

Jing Wang - NIHK
jing.wang@NOM.com
+852 2252 1011

Harrington Zhang - NIHK harrington.zhang@NOM.com +852 2252 2057

Ting Lu - NIHK  
ting.lu@NOM.com  
+852 2252 1306

## CPI inflation moderated on lower oil and gold prices

CPI inflation eased to $1.0\%$ y-o-y in June from $1.2\%$ in May, slightly below market expectations (Consensus: $1.1\%$ ; NOM: $1.2\%$ ). According to the NBS, the joint contribution of gold and oil to headline inflation was 0.23pp lower in June from May. In other words, the moderation in headline CPI inflation could be mostly explained by lower price inflation of gold and oil.

In sequential terms, CPI inflation fell to $-0.3\%$ m-o-m in June from $-0.1\%$ in May (June 2025: $-0.1\%$ ). Amid the steep decline in global oil prices, gasoline prices increased by $17.0\%$ y-o-y in June, accounting for about half of headline CPI inflation reading. Food remained a visible drag, with its inflation at $-1.6\%$ y-o-y in June, little changed from $-1.7\%$ in May, while nonfood inflation fell to $1.5\%$ from $1.9\%$ . Excluding food and energy, core inflation inched down to $1.0\%$ y-o-y in June from $1.1\%$ in May. Services inflation remained unchanged at $0.8\%$ y-o-y.

## Oil price inflation dropped on the US-Iran MOU

Amid the sharp decline in global oil prices, domestic gasoline prices fell markedly by 4.9% m-o-m in June, following the 0.3% decline in May, with its contribution to headline CPI inflation falling to -0.15pp in June from -0.01pp in May and +0.39pp in April. In year-on-year terms, gasoline price inflation dropped to 17.0% in June from 23.5% in May, contributing 0.51pp to headline inflation, down from a 0.66pp contribution in May.

## Gold's contribution declined further

Prices of gold-related products increased by $28.1\%$ y-o-y in June, down further from increases of $39.0\%$ in May, $46.9\%$ in April, $65.8\%$ in March, $76.6\%$ in February and $77.4\%$ in January. As the weighting of gold in the core CPI basket is about $0.6\%$ (see China: A more realistic picture of core CPI inflation after excluding gold, 26 December 2025), we estimate gold contributed 0.17pp y-o-y to core CPI inflation. Thus, excluding gold, core CPI inflation would be $0.83\%$ y-o-y in June, similar to the $0.9\%$ reading in May.

## Pork remains a material drag

Among food, pork remains the largest drag. Pork inflation, at $-15.9\%$ y-o-y in June, was little changed from $-16.1\%$ in May and $-15.2\%$ in April, with a contribution of $-0.3pp$ to headline CPI inflation. Given abundant pork supply and weak domestic demand, pork prices should remain under pressure in the near term. According to the MARA, the latest data show that growth in the number of hogs slaughtered remained elevated at $21.6\%$ y-o-y in June, albeit moderating from $26.7\%$ in May.

## Other components

The contributions from other components were largely steady. Egg price inflation jumped to $16.0\%$ y-o-y in June from $6.6\%$ in May on limited supply amid heatwaves, while its impact on headline inflation was only 0.08pp. Amid rising chip prices, inflation of communication facilities, which include mobile phones, increased further to $7.6\%$ y-o-y in June from $6.6\%$ in May and $4.2\%$ in April. By contrast, due to the payback effects from the durable goods trade-in program (see China: Retail sales revisited, 2 July 2026), price inflation for home appliances fell to $2.2\%$ y-o-y in June from $3.4\%$ in May.

## PPI inflation edged up in June

PPI inflation rose further to 4.1% y-o-y in June from 3.9% in May, in line with market expectations (Consensus: 4.1%; NOM: 4.0%). This marks four consecutive months of positive PPI readings and the highest monthly reading since July 2022, driven by the global energy shock. Sequential PPI inflation turned negative, as expected, falling to -0.3% m-o-m in June from 0.5% in May, which suggests inflationary pressures are moderating following the pullback of global crude prices.

The rise in PPI inflation was concentrated entirely in upstream sectors, while prices in downstream sectors actually declined even in year-over-year terms, which shows that inflationary pressures are not broadening across the economy. Markets should still interpret the strong reading with a certain degree of caution.

PPI inflation in upstream sectors increased to $5.5\%$ y-o-y in June from $5.2\%$ in May, contributing 4.28pp to the headline PPI inflation reading. Within upstream sectors, PPI inflation across mining and manufacturing sectors increased to $16.5\%$ y-o-y and $3.0\%$ , respectively, in June from $15.8\%$ and $2.3\%$ in May. However, PPI inflation in the raw materials sector moderated to $8.6\%$ y-o-y in June from $9.2\%$ in May, making a negative contribution of headline PPI inflation in May. For downstream sectors (consumer goods), PPI inflation edged down to $-0.9\%$ y-o-y in June from $-0.8\%$ in May, signalling still-muted

price pressures on the consumer side.

In specific sectors, PPI inflation in the petroleum and natural gas extraction industry eased significantly to 16.8% y-o-y in June from 35.7% in May. PPI inflation in petroleum, coal and other fuel processing also moderated to 16.7% y-o-y in June from 18.4% in May. PPI inflation in the ferrous and non-ferrous metals smelting and pressing sectors was little changed at 3.1 y-o-y and 23.4% y-o-y, respectively, in June, versus 1.0% and 24.0% in May.

Fig. 1: Selected sector breakdown and contribution of PPI inflation

<table><tr><td>Categories</td><td>Weight %</td><td>Contribution (June) pp</td><td>Contribution (May) pp</td><td>Jun-26</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td></tr><tr><td>PPI</td><td></td><td></td><td></td><td>4.1</td><td>3.9</td><td>2.8</td><td>0.5</td><td>-0.9</td><td>-1.4</td></tr><tr><td>Oil-related</td><td></td><td>1.6</td><td>1.9</td><td>0.4</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Petroleum &amp; Natural Gas Mining</td><td>0.8</td><td>0.14</td><td>0.29</td><td>16.8</td><td>35.7</td><td>28.6</td><td>5.2</td><td>-12.9</td><td>-16.7</td></tr><tr><td>Petroleum, Coal and Other Fuel Processing</td><td>3.8</td><td>0.64</td><td>0.71</td><td>16.7</td><td>18.4</td><td>14.2</td><td>-4.5</td><td>-12.0</td><td>-11.5</td></tr><tr><td>Chemical Material &amp; Product Manufacturing</td><td>6.5</td><td>0.73</td><td>0.83</td><td>11.3</td><td>12.7</td><td>8.9</td><td>-0.3</td><td>-3.7</td><td>-5.0</td></tr><tr><td>Chemical Fiber Manufacturing</td><td>0.7</td><td>0.06</td><td>0.06</td><td>7.4</td><td>8.5</td><td>5.4</td><td>-2.3</td><td>-6.0</td><td>-6.4</td></tr><tr><td>Rubber &amp; Plastic Product Manufacturing</td><td>2.2</td><td>0.03</td><td>0.01</td><td>1.4</td><td>0.5</td><td>-1.3</td><td>-3.4</td><td>-4.2</td><td>-4.1</td></tr><tr><td>Non-ferrous-related</td><td></td><td>1.7</td><td>1.8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non Ferrous Metal Mining</td><td>0.3</td><td>0.08</td><td>0.11</td><td>25.5</td><td>36.5</td><td>38.9</td><td>36.4</td><td>30.2</td><td>22.7</td></tr><tr><td>Non Ferrous Metal Smelting &amp; Pressing</td><td>7.0</td><td>1.65</td><td>1.69</td><td>23.4</td><td>24.0</td><td>22.5</td><td>22.4</td><td>22.1</td><td>17.1</td></tr><tr><td>Ferrous-related</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ferrous Metal Mining</td><td>0.3</td><td>0.02</td><td>0.01</td><td>5.2</td><td>3.3</td><td>1.3</td><td>0.1</td><td>1.0</td><td>3.0</td></tr><tr><td>Ferrous Metal Smelting &amp; Pressing</td><td>5.6</td><td>0.17</td><td>0.06</td><td>3.1</td><td>1.0</td><td>-1.1</td><td>-2.5</td><td>-3.4</td><td>-3.7</td></tr><tr><td>Coal-related</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Coal Mining</td><td>1.9</td><td>0.39</td><td>0.19</td><td>20.6</td><td>10.0</td><td>3.1</td><td>-2.2</td><td>-7.0</td><td>-9.8</td></tr><tr><td>Non-metal Mineral Smelting &amp; Pressing</td><td>0.3</td><td>-0.01</td><td>-0.01</td><td>-3.3</td><td>-3.4</td><td>-4.1</td><td>-4.2</td><td>-5.0</td><td>-4.6</td></tr><tr><td>Non-metal Mineral Product Manufacturing</td><td>3.3</td><td>-0.15</td><td>-0.17</td><td>-4.4</td><td>-5.1</td><td>-5.5</td><td>-4.9</td><td>-4.9</td><td>-5.4</td></tr><tr><td>Selected manufacturing products</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Computer, Communication &amp; Other Electronic Equipment Manufacturing</td><td>12.5</td><td>0.41</td><td>0.26</td><td>3.3</td><td>2.1</td><td>1.5</td><td>0.4</td><td>-0.9</td><td>-1.6</td></tr><tr><td>Electrical Machinery &amp; Equipment Manufacturing</td><td>8.4</td><td>0.43</td><td>0.38</td><td>5.1</td><td>4.5</td><td>3.6</td><td>3.2</td><td>2.0</td><td>0.8</td></tr><tr><td>Automobile Manufacturing</td><td>8.0</td><td>-0.17</td><td>-0.16</td><td>-2.1</td><td>-2.0</td><td>-2.0</td><td>-2.5</td><td>-2.4</td><td>-2.5</td></tr><tr><td>Fabricated Metal Product Manufacturing</td><td>3.4</td><td>0.05</td><td>0.03</td><td>1.6</td><td>0.8</td><td>0.5</td><td>0.2</td><td>-0.2</td><td>-0.7</td></tr><tr><td>General Equipment Manufacturing</td><td>3.7</td><td>-0.03</td><td>-0.03</td><td>-0.7</td><td>-0.9</td><td>-1.0</td><td>-1.2</td><td>-1.1</td><td>-1.3</td></tr><tr><td>Special Equipment Manufacturing</td><td>2.8</td><td>0.00</td><td>-0.02</td><td>0.0</td><td>-0.8</td><td>-0.9</td><td>-1.0</td><td>-1.0</td><td>-0.9</td></tr></table>

Note: Sector weight is calculated by their 2025 industrial revenue.  
Source: Wind, NOM Global Economics.

Fig. 2: A breakdown of inflation by major component

<table><tr><td rowspan="2">Categories</td><td colspan="6">% y-o-y</td></tr><tr><td>Jun 26</td><td>May 26</td><td>Q2 26</td><td>Q1 26</td><td>2025</td><td>2024</td></tr><tr><td>CPI</td><td>1.0</td><td>1.2</td><td>1.1</td><td>0.9</td><td>0.0</td><td>0.2</td></tr><tr><td>Food</td><td>-1.6</td><td>-1.7</td><td>-1.6</td><td>0.4</td><td>-1.5</td><td>-0.6</td></tr><tr><td>Grain</td><td>-0.5</td><td>-0.3</td><td>-0.4</td><td>-0.3</td><td>-1.0</td><td>-0.1</td></tr><tr><td>Vegetable</td><td>-0.3</td><td>1.6</td><td>0.3</td><td>7.6</td><td>-3.9</td><td>5.0</td></tr><tr><td>Pork</td><td>-15.9</td><td>-16.1</td><td>-15.7</td><td>-11.3</td><td>-6.1</td><td>7.7</td></tr><tr><td>Aquatic</td><td>-0.4</td><td>0.6</td><td>0.5</td><td>3.5</td><td>1.4</td><td>1.0</td></tr><tr><td>Egg</td><td>16.0</td><td>6.6</td><td>7.7</td><td>-5.2</td><td>-7.4</td><td>-4.4</td></tr><tr><td>Milk</td><td>-1.7</td><td>-1.2</td><td>-1.4</td><td>-0.9</td><td>-1.5</td><td>-1.6</td></tr><tr><td>Fruit</td><td>-0.7</td><td>-2.2</td><td>-1.3</td><td>4.3</td><td>1.2</td><td>-3.5</td></tr><tr><td>Non-Food</td><td>1.5</td><td>1.9</td><td>1.7</td><td>0.9</td><td>0.4</td><td>0.4</td></tr><tr><td>Apparel</td><td>1.4</td><td>1.4</td><td>1.4</td><td>1.8</td><td>1.5</td><td>1.4</td></tr><tr><td>Residence</td><td>-0.3</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>0.1</td><td>0.1</td></tr><tr><td>Household articles &amp; services</td><td>1.3</td><td>1.8</td><td>1.5</td><td>2.3</td><td>0.9</td><td>0.5</td></tr><tr><td>Transportation and communication</td><td>4.1</td><td>5.4</td><td>4.7</td><td>-1.1</td><td>-2.6</td><td>-1.9</td></tr><tr><td>Education, culture and recreation</td><td>1.4</td><td>1.3</td><td>1.3</td><td>1.0</td><td>0.8</td><td>1.5</td></tr><tr><td>Medicine and healthcare services</td><td>2.3</td><td>2.1</td><td>2.2</td><td>1.8</td><td>0.8</td><td>1.3</td></tr><tr><td>Other goods and services</td><td>6.6</td><td>9.9</td><td>9.2</td><td>14.1</td><td>9.3</td><td>3.8</td></tr><tr><td>Goods</td><td>1.1</td><td>1.6</td><td>1.4</td><td>0.9</td><td>-0.3</td><td>-0.1</td></tr><tr><td>Services</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.5</td><td>0.7</td></tr><tr><td>Core CPI (excluding food and energy)</td><td>1.0</td><td>1.1</td><td>1.1</td><td>1.2</td><td>0.7</td><td>0.5</td></tr><tr><td>PPI</td><td>4.1</td><td>3.9</td><td>3.6</td><td>-0.6</td><td>-2.6</td><td>-2.2</td></tr><tr><td>Upstream</td><td>5.5</td><td>5.2</td><td>4.8</td><td>-0.3</td><td>-3.0</td><td>-2.5</td></tr><tr><td>Mining</td><td>16.5</td><td>15.8</td><td>14.3</td><td>-3.8</td><td>-9.0</td><td>-2.9</td></tr><tr><td>Raw materials</td><td>8.6</td><td>9.2</td><td>8.3</td><td>-0.9</td><td>-3.4</td><td>-1.7</td></tr><tr><td>Man

[中间内容因长度限制已省略]

ed or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

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
