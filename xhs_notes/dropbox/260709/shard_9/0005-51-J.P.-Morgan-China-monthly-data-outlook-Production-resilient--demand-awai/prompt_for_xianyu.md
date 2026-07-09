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
# China monthly data outlook

## Production resilient, demand awaits fiscal execution

We expect some stabilization in June data after the April–May soft patch, but the recovery remains narrow and externally supported. PMIs improved modestly, exports remain helped by high-tech and AI-related demand, and lower oil prices eased cost pressure. Domestic demand weakened further: May retail sales fell 0.6% oya, FAI contracted 10.7% oya, infrastructure FAI dropped 9.4% oya, and real estate FAI declined 24.3% oya. The near-term question is whether fiscal execution can turn available funding into activity before external demand becomes less reliable. PMIs point to a floor in industrial momentum, not a new upswing. Production and orders improved, but employment, inventories, and export orders remain mixed, with little evidence of a broader restocking, hiring, or capex cycle. Lower input prices ease near-term margin pressure, but weak downstream demand still caps pricing power.

The recovery is still two-speed. Manufacturing competitiveness, trade rerouting, and the global IP/AI cycle continue to support exports and high-tech production. High-tech manufacturing rose 15.1% oya in May and contributed nearly 40% of industrial growth in January–May. But strength remains concentrated in electronics, high-tech manufacturing, and selected upstream sectors; consumer-related, housing-linked, and traditional industries remain weak.

External demand remains the main cushion, but there are risks. June exports may remain strong, supported by AI-related equipment, memory modules, new energy products, and trade rerouting. Yet tariffs, anti-subsidy cases, local-content rules, and carbon-related barriers could increasingly limit external absorption. If exports slow before domestic demand recovers, resilient production would translate into inventories, margin compression, and renewed producer-price weakness.

Domestic demand is the binding constraint. Trade-in subsidies appear to have pulled forward durable-goods purchases, while weak income expectations and confidence cap services upside. The latest activity mix points to an absorption problem: without faster fiscal spending and stronger household demand, resilient output risks feeding inventories and price discounting.

Fiscal execution is the key July watch. General budget spending contracted for a second month in May, infrastructure outlays fell 12.0% oya, and fiscal deposits rose to the second-highest May level in a decade. Slow fiscal deployment remains a drag. Special local government bond issuance has picked up, but the growth impact depends on whether proceeds quickly become project starts and physical work.

If June activity and 2Q GDP disappoint, the July Politburo meeting could bring stronger counter-cyclical considerations and targeted measures. The response would likely remain fiscal-led. Rate cuts may be used as a signal, but without faster fiscal execution and stronger credit demand, the growth impulse would be limited. The near-term outlook hinges on whether external demand and fiscal deployment can absorb resilient production. If trade frictions broaden or fiscal projects lag, output resilience could instead translate into inventories, margin compression, and softer output prices. Policy should now shift from supporting production to converting fiscal resources into real demand.

See page 27 for analyst certification and important disclosures.

Emerging Markets Asia, Economic and Policy Research

Feng Zhu
(852) 2800 1745
feng.zhu@JPM.com

Tingting Ge
(852) 2800-0143
tingting.ge@JPM.com

Jiayi Li
(852) 2800-5229
jiayi.c.li@JPM.com

Tongfang Yuan
(852) 2800-0085
tongfang.yuan@JPM.com
JPM Chase Bank, N.A., Hong Kong Branch

## Table Of Contents

China monthly data outlook.... 1
Production resilient, demand awaits fiscal execution.... 1
Key economic statistics.... 3
China macro indicator heat map.... 4
China activity indicator heat map.... 5
Recent policy measures (June).... 6
Summary of major economic indicators and forecasts.... 7
Real GDP (2Q).... 8
Industrial production (Jun).... 8
Manufacturing PMI (Jun).... 9
Merchandise trade (Jun).... 9
Retail sales (Jun).... 10
Auto production and sales (Jun).... 10
Fixed investment (Jun).... 11
Industrial profits (Jun).... 12
Labor market & consumer confidence (Jun).... 12
Consumer prices (Jun).... 13
Producer prices (Jun).... 13
House prices (June).... 14
Housing activities (June).... 14
Money aggregates (June).... 15
Aggregate financing (June).... 15
Interest rates.... 16
Open market operations.... 16
Fiscal position (June).... 17
Monetary conditions (June).... 17
Currency exchange rate.... 18
FX reserves (June).... 18
Manufacturing and industrial activity tracking.... 19
Service sector activity tracking.... 21
Financial markets.... 23
External conditions and balance of payments.... 24
Labor market conditions.... 25
Recent publication highlights.... 26

Tongfang Yuan (852) 2800-0085
tongfang.yuan@JPM.com

Key economic statistics

<table><tr><td rowspan="3"></td><td colspan="4">2025 Nominal GDP, US$</td><td colspan="3">Real GDP</td><td colspan="3">Consumer prices</td></tr><tr><td rowspan="2">Total billion</td><td rowspan="2" colspan="3">per capita (US$)</td><td colspan="3">%year-on-year</td><td colspan="3">%year-on-year</td></tr><tr><td>2024</td><td>2025</td><td>2026F</td><td>2024</td><td>2025</td><td>2026F</td></tr><tr><td>China</td><td>19550</td><td></td><td>13639</td><td></td><td>4.9</td><td>5.0</td><td>4.7</td><td>0.2</td><td>0.0</td><td>1.1</td></tr><tr><td>Hong Kong SAR</td><td>427</td><td></td><td>55873</td><td></td><td>2.6</td><td>3.5</td><td>3.0</td><td>1.7</td><td>1.4</td><td>2.0</td></tr><tr><td>Taiwan, China</td><td>921</td><td></td><td>39353</td><td></td><td>5.3</td><td>8.8</td><td>9.9</td><td>2.2</td><td>1.7</td><td>1.9</td></tr><tr><td>US</td><td>30762</td><td></td><td>89977</td><td></td><td>2.8</td><td>2.1</td><td>2.1</td><td>3.0</td><td>2.7</td><td>3.5</td></tr><tr><td>Euro Area</td><td>17873</td><td></td><td>51050</td><td></td><td>0.9</td><td>1.5</td><td>0.4</td><td>-20.5</td><td>2.1</td><td>2.7</td></tr><tr><td>Japan</td><td>4433</td><td></td><td>36018</td><td></td><td>5.2</td><td>1.1</td><td>0.7</td><td>2.7</td><td>3.2</td><td>2.1</td></tr><tr><td rowspan="3"></td><td colspan="4">Current account balance</td><td colspan="3">Government balance</td><td colspan="3">Industrial production</td></tr><tr><td colspan="4">% of GDP</td><td colspan="3">% of GDP, end of period</td><td colspan="3">%year-on-year</td></tr><tr><td>2024</td><td>2025F</td><td>2026F</td><td></td><td>2024</td><td>2025</td><td>2026F</td><td>2024</td><td>2025</td><td>2026F</td></tr><tr><td>China</td><td>2.3</td><td>3.8</td><td>3.6</td><td></td><td>-3.0</td><td>-4.0</td><td>-4.0</td><td>5.6</td><td>5.9</td><td>4.5</td></tr><tr><td>Hong Kong SAR</td><td>12.9</td><td>12.8</td><td>10.5</td><td></td><td>-1.8</td><td>0.1</td><td>0.6</td><td>0.8</td><td>2.0</td><td>2.0</td></tr><tr><td>Taiwan, China</td><td>14.1</td><td>15.1</td><td>13.6</td><td></td><td>-0.6</td><td>-1.0</td><td>-1.6</td><td>11.8</td><td>16.0</td><td>9.8</td></tr><tr><td>US</td><td>-4.1</td><td>-3.8</td><td>-2.9</td><td></td><td>-6.3</td><td>-5.8</td><td>-6.3</td><td>-3.6</td><td>0.8</td><td>1.1</td></tr><tr><td>Euro Area</td><td>2.7</td><td>1.7</td><td>2.2</td><td></td><td>-3.1</td><td>-2.7</td><td>-3.1</td><td>-3.0</td><td>1.7</td><td>-0.1</td></tr><tr><td>Japan</td><td>4.6</td><td>4.8</td><td>4.2</td><td></td><td>-6.1</td><td>-6.7</td><td>-6.8</td><td>-3.0</td><td>0.1</td><td>2.5</td></tr><tr><td></td><td>2024</td><td>2025</td><td>2026F</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26F</td></tr><tr><td colspan="11">Real GDP, %-ch over a year ago</td></tr><tr><td>China</td><td>4.9</td><td>5.0</td><td>4.7</td><td>5.4</td><td>5.4</td><td>5.2</td><td>4.8</td><td>4.5</td><td>5.0</td><td>4.7</td></tr><tr><td>Hong Kong SAR</td><td>2.6</td><td>3.5</td><td>3.0</td><td>2.5</td><td>3.2</td><td>3.3</td><td>3.8</td><td>4.0</td><td>5.9</td><td>2.8</td></tr><tr><td>Taiwan, China</td><td>5.3</td><td>8.8</td><td>9.9</td><td>4.1</td><td>5.5</td><td>7.7</td><td>8.4</td><td>13.0</td><td>14.6</td><td>11.3</td></tr><tr><td>US</td><td>2.8</td><td>2.1</td><td>2.1</td><td>2.4</td><td>2.0</td><td>2.1</td><td>2.3</td><td>2.0</td><td>2.7</td><td>2.3</td></tr><tr><td>Euro Area</td><td>0.9</td><td>1.5</td><td>0.4</td><td>1.4</td><td>1.7</td><td>1.6</td><td>1.4</td><td>1.2</td><td>0.3</td><td>0.3</td></tr><tr><td>Japan</td><td>5.2</td><td>1.1</td><td>0.7</td><td>0.7</td><td>1.5</td><td>1.8</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.2</td></tr><tr><td colspan="11">Real GDP, %-ch over 1 quarter, saar</td></tr><tr><td>China (JPM estimate)</td><td>4.9</td><td>5.0</td><td>4.7</td><td>7.1</td><td>4.9</td><td>4.2</td><td>3.7</td><td>5.2</td><td>6.7</td><td>3.3</td></tr><tr><td>Hong Kong SAR</td><td>2.6</td><td>3.5</td><td>3.0</td><td>3.6</td><td>4.5</td><td>3.2</td><td>3.6</td><td>4.5</td><td>12.1</td><td>3.0</td></tr><tr><td>Taiwan, China</td><td>5.3</td><td>8.8</td><td>9.9</td><td>7.2</td><td>3.7</td><td>16.3</td><td>6.7</td><td>28.7</td><td>6.9</td><td>4.5</td></tr><tr><td>US</td><td>2.8</td><td>2.1</td><td>2.1</td><td>1.9</td><td>-0.6</td><td>3.8</td><td>4.4</td><td>0.5</td><td>2.1</td><td>2.2</td></tr><tr><td>Euro Area</td><td>0.9</td><td>1.5</td><td>0.4</td><td>1.5</td><td>2.6</td><td>0.5</td><td>1.0</td><td>0.7</td><td>-0.9</td><td>0.5</td></tr><tr><td>Japan</td><td>5.2</td><td>1.1</td><td>0.7</td><td>1.4</td><td>2.0</td><td>1.1</td><td>-2.3</td><td>0.7</td><td>1.8</td><td>0.8</td></tr><tr><td colspan="11">Consumer prices, %oya, average</td></tr><tr><td>China</td><td>0.2</td><td>0.0</td><td>1.1</td><td>0.2</td><td>-0.1</td><td>0.0</td><td>-0.2</td><td>0.6</td><td>0.8</td><td>1.2</td></tr><tr><td>Hong Kong SAR</td><td>1.7</td><td>1.4</td><td>2.0</td><td>1.4</td><td>1.6</td><td>1.8</td><td>1.1</td><td>1.3</td><td>1.6</td><td>2.0</td></tr><tr><td>Taiwan, China</td><td>2.2</td><td>1.7</td><td>1.9</td><td>2.0</td><td>2.2</td><td>1.6</td><td>1.5</td><td>1.3</td><td>1.2</td><td>2.0</td></tr><tr><td>US</td><td>3.0</td><td>2.7</td><td>3.5</td><td>2.7</td><td>2.7</td><td>2.5</td><td>2.9</td><td>2.7</td><td>2.7</td><td>3.9</td></tr><tr><td>Euro Area</td><td>-20.5</td><td>2.1</td><td>2.7</td><td>2.2</td><td>2.3</td><td>2.0</td><td>2.1</td><td>2.1</td><td>2.0</td><td>3.0</td></tr><tr><td>Japan</td><td>2.7</td><td>3.2</td><td>2.1</td><td>2.9</td><td>3.8</td><td>3.4</td><td>2.9</td><td>2.7</td><td>1.4</td><td>1.5</td></tr><tr><td colspan="11">Official interest rates, % p.a., end-period</td></tr><tr><td>China</td><td>7-day reverse repo</td><td>1.50</td><td>1.40</td><td>1.30</td><td>1.50</td><td>1.50</td><td>1.40</td><td>1.40</td><td>1.40</td><td>1.40</td></tr><tr><td>Hong Kong SAR</td><td>Disc. Window</td><td>4.75</td><td>4.00</td><td>4.00</td><td>4.75</td><td>4.75</td><td>4.50</td><td>4.00</td><td>4.00</td><td>4.00</td></tr><tr><td>Taiwan, China</td><td>Official disc.</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td><td>2.000</td></tr><tr><td>US</td><td>Fed funds</td><td>4.5</td><td>3.8</td><td>3.8</td><td>4.50</td><td>4.50</td><td>4.25</td><td>3.75</td><td>3.75</td><td>3.75</td></tr><tr><td>Euro Area</td><td>Refi rate</td><td>3.0</td><td>2.0</td><td>2.5</td><td>3.00</td><td>2.50</td><td>2.00</td><td>2.00</td><td>2.00</td><td>2.25</td></tr><tr><td>Japan</td><td>O/N call rate</td><td>0.23</td><td>0.73</td><td>1.25</td><td>0.23</td><td>0.48</td><td>0.48</td><td>0.73</td><td>0.73</td><td>1.00</td></tr><tr><td colspan="11">Exchange rates, end-period</td></tr><tr><td>China</td><td>USD/CNY</td><td>7.30</td><td>6.99</td><td>6.70</td><td>7.30</td><td>7.26</td><td>7.16</td><td>7.12</td><td>6.99</td><td>6.79</td></tr><tr><td>Hong Kong SAR</td><td>USD/HKD</td><td>7.77</td><td>7.78</td><td>7.84</td><td>7.77</td><td>7.78</td><td>7.85</td><td>7.78</td><td>7.84</td><td>7.83</td></tr><tr><td>Taiwan, China</td><td>USD/TWD</td><td>32.80</td><td>31.39</td><td>31.90</td><td>32.80</td><td>33.25</td><td>29.23</td><td>30.48</td><td>31.39</td><td>31.50</td></tr><tr><td>Euro Area</td><td>EUR/USD</td><td>1.04</td><td>1.17</td><td>1.13</td><td>1.04</td><td>1.08</td><td>1.18</td><td>1.17</td><td>1.15</td><td>1.17</td></tr><tr><td>Japan</td><td>USD/JPY</td><td>156.9</td><td>156.9</td><td>164.0</td><td>156.9</td><td>149.5</td><td>144.3</td><td>147.9</td><td>156.9</td><td>159.1</td></tr></table>

Source: Private and public agencies and JPM forecasts. Further details available upon request.

China macro indicator heat map

<table><tr><td colspan="2"></td><td>6/24</td><td>7/24</td><td>8/24</td><td>9/24</td><td>10/24</td><td>11/24</td><td>12/24</td><td>1/25</td><td>2/25</td><td>3/25</td><td>4/25</td><td>5/25</td><td>6/25</td><td>7/25</td><td>8/25</td><td>9/25</td><td>10/25</td><td>11/25</td><td>12/25</td><td>1/26</td><td>2/26</td><td>3/26</td><td>4/26</td><td>5/26</td></tr><tr><td>IP</td><td>%oya</td><td>5.3</td><td>5.1</td><td>4.5</td><td>5.4</td><td>5.3</td><td>5.4</td><td>6.2</td><td>5.9</td><td>5.9</td><td>7.7</td><td>6.1</td><td>5.8</td><td>6.8</td><td>5.7</td><td>5.2</td><td>6.5</td><td>4.9</td><td>4.8</td><td>5.2</td><td>6.3</td><td>6.3</td><td>5.7</td><td>4.1</td><td>4.5</td></tr><tr><td>IP</td><td>%m/m sa</td><td>0.2</td><td>0.7</td><td>0.5</td><td>0.5</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.2</td><td>0.4</td><td>0.8</td><td>0.2</td><td>-0.1</td><td>0.9</td><td>-0.2</td><td>0.1</td><td>1.4</td><td>-0.4</td><td>0.6</td><td>1.1</td><td>1.2</td><td>0.4</td><td>0.2</td><td>-1.1</td><td>0.2</td></tr><tr><td>IP</td><td>%3m/3m saar</td><td>3.9</td><td>4.7</td><td>6.0</td><td>6.0</td><td>7.0</td><td>7.9</td><td>8.8</td><td>8.6</td><td>7.5</td><td>6.1</td><td>5.6</td><td>5.1</td><td>4.7</td><td>3.8</td><td>3.7</td><td>3.9</td><td>4.3</td><td>5.3</td><td>5.2</td><td>7.8</td><td>9.5</td><td>10.4</td><td>5.6</td><td>1.0</td></tr><tr><td>Retail sales</td><td>%oya</td><td>2.0</td><td>2.7</td><td>2.1</td><td>3.2</td><td>4.8</td><td>3.0</td><td>3.7</td><td>4.0</td><td>4.0</td><td>5.9</td><td>5.1</td><td>6.4</td><td>4.8</td><td>3.7</td><td>3.4</td><td>3.0</td><td>2.9</td><td>1.3</td><td>0.9</td><td>2.8</td><td>2.8</td><td>1.7</td><td>0.2</td><td>-0.6</td></tr><tr><td>Retail sales</td><td>%m/m sa</td><td>0.2</td><td>0.6</td><td>0.4</td><td>0.4</td><td>0.6</td><td>0.2</td><td>0.6</td><td>0.0</td><td>0.3</td><td>0.7</td><td>0.2</td><td>0.6</td><td>-0.1</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.1</td><td>-0.2</td><td>0.0</td><td>0.3</td><td>0.0</td><td>-0.1</td><td>-0.2</td><td>-0.1</td></tr><tr><td>Retail sales</td><td>%3m/3m saar</td><td>3.3</td><td>3.7</td><td>4.1</td><td>5.3</td><td>5.7</td><td>5.6</td><td>5.4</td><td>4.4</td><td>3.9</td><td>3.4</td><td>4.0</td><td>5.0</td><td>4.6</td><td>3.7</td><td>1.7</td><td>1.1</td><td>0.8</td><td>0.7</td><td>0.2</td><td>-0.1</td><td>0.3</td><td>0.7</td><td>0.0</td><td>-1.0</td></tr><tr><td>FAI</td><td>%oya, ytd</td><td>3.9</td><td>3.6</td><td>3.4</td><td>3.4</td><td>3.4</td><td>3.3</td><td>3.2</td><td>4.1</td><td>4.1</td><td>4.2</td><td>4.0</td><td>3.7</td><td>2.8</td><td>1.6</td><td>0.5</td><td>-0.5</td><td>-1.7</td><td>-2.6</td><td>-3.8</td><td>1.8</td><td>1.8</td><td>1.7</td><td>-1.6</td><td>-4.1</td></tr><tr><td>FAI</td><td>%oya</td><td>3.6</td><td>1.9</td><td>2.2</td><td>3.4</td><td>3.4</td><td>2.4</td><td>2.2</td><td>4.1</td><td>4.1</td><td>4.3</td><td>3.6</td><td>2.9</td><td>0.5</td><td>-5.2</td><td>-6.3</td><td>-6.8</td><td>-11.2</td><td>-11.1</td><td>-16.0</td><td>1.8</td><td>1.8</td><td>1.6</td><td>-8.0</td><td>-10.7</td></tr><tr><td>FAI</td><td>%m/m sa</td><td>0.6</td><td>0.6</td><td>0.3</td><td>0.0</td><td>0.9</td><td>-0.7</td><td>0.8</td><td>0.1</td><td>-0.6</td><td>-0.5</td><td>-1.0</td><td>-0.2</td><td>-1.5</td><td>-2.2</td>

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
