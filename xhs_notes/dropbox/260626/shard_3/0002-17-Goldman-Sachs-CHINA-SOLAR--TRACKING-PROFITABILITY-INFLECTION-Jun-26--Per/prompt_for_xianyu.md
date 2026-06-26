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
CHINA SOLAR: TRACKING PROFITABILITY INFLECTION

# Jun-26: Persistent upstream pricing softness against worsening inventory expectations

Our China Solar Profitability Tracker follows monthly supply/demand and inventory dynamics by sub-sector, and spot prices/input costs implied cash GP & EBITDA margin trends for companies under our coverage.

## Key highlights in Jun MTD:

Pricing softness persisted across upstream segments in Jun: Throughout the month, pricing declined by an avg. 5% across the solar value chain. Specifically, Film (-12% MTD) and Cell (-11% MTD) led the price weakness due to lower oil price (-8% MoM) and lower silver cost (-13% MTD) amid surging producer-side inventory during the period (+21% MoM), respectively. In terms of profitability, lower pricing has led to 8pp/7pp/4pp/3pp deterioration in Cell/Film/Poly/Glass, while margin slightly improved by 2pp MTD for Module due to easing cost pressure. Looking forward, we think pricing softness will persist considering i) worsening inventory outlook into the weak demand season in Jul-Aug, and ii) lower Module production cost due to softening upstream prices and adoption of cheap metal technology by Tier 1 players staring from 3Q.

Global Module demand declined by 22% mom and 79% yoy to 29GW in May 2026, sending 5M26 down by 46% yoy to 193GW, which is tracking below our FY26E forecast of -12% yoy, mainly due to weaker demand in China (-91% yoy in May and -70% yoy in 5M26).

What to do from here? Across our coverage, we prefer Maxwell (on new application opportunity), Hangzhou First (on solar film price hike and unit profitability expansion potential) and Longi (on ESS potential and more resilient EBITDA driven by upstream price decline with mid-cycle BC upside). We stay cautious on Rod Poly (Neutral/Sell on Daqo ADR/A, and Sell on Tongwei), and Glass (Sell on Flat A/H).

Mengwen Wang
+86(21)2401-8932 |
mengwen.wang@goldmansachs.cn
GS (China) Securities
Company Limited

Jacqueline Du
+852-2978-1783 |
jacqueline.du@gs.com
GS (Asia) L.L.C.

## Profitability improved in Module but deteriorated in upstream segments

Exhibit 1: Pricing softness persisted across upstream segments in Jun Summary of the latest pricing across the solar value chain

<table><tr><td colspan="11">Spot price</td><td colspan="3">Average price</td></tr><tr><td>Price</td><td></td><td>Weekly 6/25/2026</td><td>Monthly Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>MTD Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>Since anti-involution 7/2/2025</td><td>Since anti-monopoly 1/7/2026</td><td>MoM Jun-26</td><td>QoQ 2026Q2</td><td>YTD yoy 2026</td></tr><tr><td>Poly</td><td></td><td></td><td></td><td></td><td></td><td>-6%</td><td>-19%</td><td>-37%</td><td>-4%</td><td>-37%</td><td>-4%</td><td>-30%</td><td>-5%</td></tr><tr><td>N+Granular Poly</td><td>Rmb/kg</td><td>32.5</td><td>33.1</td><td>34.2</td><td>40.8</td><td>-5%</td><td>-20%</td><td>-36%</td><td>-3%</td><td>-36%</td><td>-3%</td><td>-29%</td><td>-4%</td></tr><tr><td>N+Rod Poly</td><td>Rmb/kg</td><td>33.2</td><td>33.8</td><td>35.0</td><td>42.3</td><td>-6%</td><td>-18%</td><td>-38%</td><td>-4%</td><td>-38%</td><td>-4%</td><td>-30%</td><td>-6%</td></tr><tr><td>Poly Future Quotes (Max)</td><td>Rmb/kg</td><td>42.5</td><td>41.5</td><td>41.4</td><td>45.0</td><td>5%</td><td>10%</td><td>-30%</td><td>15%</td><td>-30%</td><td>-1%</td><td>-15%</td><td>-7%</td></tr><tr><td>Poly Future Quotes (Median)</td><td>Rmb/kg</td><td>36.7</td><td>36.6</td><td>38.2</td><td>43.0</td><td>0%</td><td>-4%</td><td>-39%</td><td>5%</td><td>-39%</td><td>-4%</td><td>-21%</td><td>-7%</td></tr><tr><td>Poly Future Quotes (Min)</td><td>Rmb/kg</td><td>35.9</td><td>35.5</td><td>34.7</td><td>40.4</td><td>0%</td><td>0%</td><td>-38%</td><td>6%</td><td>-38%</td><td>4%</td><td>-25%</td><td>-11%</td></tr><tr><td>Non-China produced Poly</td><td>US$/kg</td><td>18.5</td><td>18.5</td><td>18.5</td><td>18.5</td><td>0%</td><td>0%</td><td>3%</td><td>-3%</td><td>3%</td><td>0%</td><td>0%</td><td>-3%</td></tr><tr><td>Spread: Rod-Granular</td><td>Rmb/kg</td><td>0.7</td><td>0.7</td><td>0.8</td><td>1.4</td><td>-0.3</td><td>0.7</td><td>-2.7</td><td>-0.5</td><td>-2.7</td><td>-0.3</td><td>-1.3</td><td>-1.0</td></tr><tr><td>Spread: Max Future - Spot</td><td>Rmb/kg</td><td>9.3</td><td>7.7</td><td>6.5</td><td>2.8</td><td>4.1</td><td>11.1</td><td>2.9</td><td>6.9</td><td>2.1</td><td>1.2</td><td>7.7</td><td>n.a.</td></tr><tr><td>Spread: Median Future - Spot</td><td>Rmb/kg</td><td>3.5</td><td>2.8</td><td>3.2</td><td>0.7</td><td>2.1</td><td>5.7</td><td>-2.4</td><td>3.2</td><td>-2.6</td><td>0.0</td><td>5.2</td><td>n.a.</td></tr><tr><td>Spread: Min Future - Spot</td><td>Rmb/kg</td><td>2.7</td><td>1.7</td><td>-0.3</td><td>-1.8</td><td>2.2</td><td>7.3</td><td>-1.7</td><td>3.4</td><td>-1.4</td><td>2.9</td><td>3.3</td><td>n.a.</td></tr><tr><td>Wafer</td><td></td><td></td><td></td><td></td><td></td><td>-1%</td><td>-8%</td><td>-24%</td><td>1%</td><td>-30%</td><td>-1%</td><td>-20%</td><td>-11%</td></tr><tr><td>N+M10</td><td>Rmb/pc</td><td>0.9</td><td>0.91</td><td>0.93</td><td>1.05</td><td>-3%</td><td>-9%</td><td>-25%</td><td>5%</td><td>-31%</td><td>-2%</td><td>-21%</td><td>-9%</td></tr><tr><td>N+G12L (USS)</td><td>Rmb/pc</td><td>1.2</td><td>1.17</td><td>1.18</td><td>1.33</td><td>0%</td><td>-9%</td><td>-23%</td><td>-2%</td><td>-30%</td><td>0%</td><td>-20%</td><td>-12%</td></tr><tr><td>N+G12R (DS)</td><td>Rmb/pc</td><td>1.0</td><td>0.99</td><td>1.00</td><td>1.13</td><td>-1%</td><td>-7%</td><td>-24%</td><td>-1%</td><td>-30%</td><td>-1%</td><td>-21%</td><td>-11%</td></tr><tr><td>Cell-China</td><td></td><td></td><td></td><td></td><td></td><td>-11%</td><td>-23%</td><td>-13%</td><td>20%</td><td>-22%</td><td>-6%</td><td>-22%</td><td>31%</td></tr><tr><td>Topcon G12L-China (USS)</td><td>Rmb/w</td><td>0.30</td><td>0.31</td><td>0.33</td><td>0.37</td><td>-10%</td><td>-21%</td><td>-12%</td><td>22%</td><td>-21%</td><td>-4%</td><td>-21%</td><td>30%</td></tr><tr><td>Topcon G12R-China (DS)</td><td>Rmb/w</td><td>0.29</td><td>0.30</td><td>0.33</td><td>0.37</td><td>-12%</td><td>-26%</td><td>-15%</td><td>18%</td><td>-24%</td><td>-8%</td><td>-22%</td><td>32%</td></tr><tr><td>Cell-Ex-China</td><td></td><td></td><td></td><td></td><td></td><td>-12%</td><td>-19%</td><td>5%</td><td>n.m.</td><td>n.m.</td><td>-9%</td><td>-13%</td><td>36%</td></tr><tr><td>Topcon M10-Ex-China</td><td>US$/w</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.05</td><td>-12%</td><td>-19%</td><td>5%</td><td>n.m.</td><td>n.m.</td><td>-9%</td><td>-13%</td><td>36%</td></tr><tr><td>Module-China</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>-1%</td><td>6%</td><td>7%</td><td>6%</td><td>0%</td><td>2%</td><td>6%</td></tr><tr><td>Bifacial Topcon-China</td><td>Rmb/w</td><td>0.74</td><td>0.74</td><td>0.75</td><td>0.74</td><td>0%</td><td>-3%</td><td>6%</td><td>9%</td><td>6%</td><td>-1%</td><td>2%</td><td>7%</td></tr><tr><td>NBC-China</td><td>Rmb/w</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.85</td><td>0%</td><td>0%</td><td>13%</td><td>8%</td><td>10%</td><td>0%</td><td>3%</td><td>10%</td></tr><tr><td>Topcon USS-China</td><td>Rmb/w</td><td>0.72</td><td>0.72</td><td>0.71</td><td>0.70</td><td>0%</td><td>3%</td><td>5%</td><td>7%</td><td>5%</td><td>0%</td><td>3%</td><td>3%</td></tr><tr><td>Topcon DS-China</td><td>Rmb/w</td><td>0.76</td><td>0.76</td><td>0.77</td><td>0.76</td><td>-1%</td><td>-4%</td><td>8%</td><td>13%</td><td>8%</td><td>-1%</td><td>2%</td><td>9%</td></tr><tr><td>Spread: NBC-Topcon</td><td>Rmb/w</td><td>0.11</td><td>0.10</td><td>0.09</td><td>0.08</td><td>0.01</td><td>0.04</td><td>0.04</td><td>-0.03</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Module-Export</td><td></td><td></td><td></td><td></td><td></td><td>-1%</td><td>9%</td><td>24%</td><td>n.m.</td><td>n.m.</td><td>-1%</td><td>16%</td><td>14%</td></tr><tr><td>Topcon Export</td><td>US$/w</td><td>0.12</td><td>0.12</td><td>0.12</td><td>0.11</td><td>0%</td><td>11%</td><td>29%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>20%</td><td>18%</td></tr><tr><td>BC C&amp;I EU</td><td>US$/w</td><td>0.14</td><td>0.14</td><td>0.14</td><td>0.13</td><td>-3%</td><td>1%</td><td>21%</td><td>n.m.</td><td>n.m.</td><td>-2%</td><td>11%</td><td>15%</td></tr><tr><td>BS Resi EU</td><td>US$/w</td><td>0.20</td><td>0.20</td><td>0.20</td><td>0.19</td><td>-1%</td><td>14%</td><td>22%</td><td>n.m.</td><td>n.m.</td><td>-1%</td><td>17%</td><td>7%</td></tr><tr><td>Module-US</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>7%</td></tr><tr><td>Imported from Ex-China</td><td>US$/w</td><td>0.27</td><td>0.27</td><td>0.27</td><td>0.27</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>7%</td></tr><tr><td>Local assembled</td><td>US$/w</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>8%</td></tr><tr><td>Module-India</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Local assembled</td><td>US$/w</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Glass</td><td></td><td></td><td></td><td></td><td></td><td>-2%</td><td>-15%</td><td>-27%</td><td>-21%</td><td>-21%</td><td>-6%</td><td>-15%</td><td>-23%</td></tr><tr><td>2.0mm PV glass</td><td>Rmb/sqm</td><td>8.3</td><td>8.1</td><td>8.7</td><td>9.5</td><td>-2%</td><td>-15%</td><td>-27%</td><td>-21%</td><td>-21%</td><td>-6%</td><td>-15%</td><td>-23%</td></tr><tr><td>Film</td><td></td><td></td><td></td><td></td><td></td><td>-12%</td><td>-8%</td><td>15%</td><td>11%</td><td>17%</td><td>-11%</td><td>29%</td><td>10%</td></tr><tr><td>EVA film (Transparent)</td><td>Rmb/sqm</td><td>5.9</td><td>6.1</td><td>7.1</td><td>6.3</td><td>-18%</td><td>-16%</td><td>10%</td><td>3%</td><td>13%</td><td>-15%</td><td>30%</td><td>7%</td></tr><tr><td>EVA film (White)</td><td>Rmb/sqm</td><td>6.4</td><td>6.6</td><td>7.6</td><td>6.8</td><td>-16%</td><td>-15%</td><td>9%</td><td>3%</td><td>12%</td><td>-14%</td><td>28%</td><td>7%</td></tr><tr><td>POE film</td><td>Rmb/sqm</td><td>10.4</td><td>10.5</td><td>10.8</td><td>9.6</td><td>-3%</td><td>7%</td><td>27%</td><td>27%</td><td>27%</td><td>-2%</td><td>29%</td><td>16%</td></tr><tr><td>Spread: POE-EVA</td><td>Rmb/sqm</td><td>4.3</td><td>4.1</td><td>3.5</td><td>3.1</td><td>1.0</td><td>1.8</td><td>1.7</td><td>1.0</td><td>1.6</td><td>0.9</td><td>0.8</td><td>0.9</td></tr><tr><td>EVA resin</td><td>Rmb/ton</td><td>9,200</td><td>9,407</td><td>10,924</td><td>10,407</td><td>-4%</td><td>-27%</td><td>3%</td><td>-6%</td><td>1%</td><td>-12%</td><td>10%</td><td>0%</td></tr><tr><td>POE resin</td><td>Rmb/ton</td><td>15,082</td><td>15,082</td><td>15,272</td><td>12,410</td><td>-1%</td><td>35%</td><td>63%</td><td>43%</td><td>65%</td><td>-1%</td><td>60%</td><td>17%</td></tr><tr><td>Spread: POE-EVA resin</td><td>Rmb/ton</td><td>5,882</td><td>5,675</td><td>4,348</td><td>2,003</td><td>195</td><td>7,279</td><td>5,627</td><td>1,387</td><td>6,225</td><td>1,180</td><td>4,691</td><td>1,894</td></tr></table>

Source: Oilchem, SiliconChina, PVInfolink, SMM, Solarbe

Exhibit 2: Jun spot price implied cash profitability improved in Module but deteriorated in upstream segments
Summary of spot price implied cash GPM and unit GP across the solar value chain

<table><tr><td rowspan="2"></td><td colspan="4">Spot price implied cash GPM</td><td colspan="6">Spot cash GPM change (in ppt)</td><td colspan="3">Average cash GPM change (in ppt)</td></tr><tr><td>Weekly 6/25/2026</td><td>Monthly Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>MTD Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>Since anti-involution 7/2/2025</td><td>Since anti-monopoly 1/7/2026</td><td>mom Jun-26</td><td>qoq 2026Q2</td><td>YTD yoy 2026</td><td></td></tr><tr><td>Poly-Tier 1</td><td>4%</td><td>8%</td><td>7%</td><td>20%</td><td>-4ppt</td><td>-14ppt</td><td>-32ppt</td><td>0ppt</td><td>-34ppt</td><td>0ppt</td><td>-26ppt</td><td>-2ppt</td><td></td></tr><tr><td>Rod Poly</td><td>-8%</td><td>-2%</td><td>-6%</td><td>8%</td><td>-2ppt</td><td>-11ppt</td><td>-36ppt</td><td>0ppt</td><td>-39ppt</td><td>4ppt</td><td>-29ppt</td><td>-4ppt</td><td></td></tr><tr><td>Granular Poly</td><td>15%</td><td>17%</td><td>20%</td><td>31%</td><td>-6ppt</td><td>-18ppt</td><td>-27ppt</td><td>1ppt</td><td>-29ppt</td><td>-4ppt</td><td>-23ppt</td><td>1ppt</td><td></td></tr><tr><td>Wafer-Tier 1</td><td>-3%</td><td>-3%</td><td>-4%</td><td>-3%</td><td>0ppt</td><td>5ppt</td><td>1ppt</td><td>8ppt</td><td>-11ppt</td><td>0ppt</td><td>-2ppt</td><td>-6ppt</td><td></td></tr><tr><td>M10</td><td>-9%</td><td>-9%</td><td>-9%</td><td>-7%</td><td>-1ppt</td><td>4ppt</td><td>-2ppt</td><td>11ppt</td><td>-14ppt</td><td>-1ppt</td><td>-4ppt</td><td>-5ppt</td><td></td></tr><tr><td>G12</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td><td>2ppt</td><td>6ppt</td><td>4ppt</td><td>4ppt</td><td>-7ppt</td><td>1ppt</td><td>-1ppt</td><td>-7ppt</td><td></td></tr><tr><td>Cell-Tier 1</td><td>-6%</td><td>-2%</td><td>2%</td><td>6%</td><td>-8ppt</td><td>-15ppt</td><td>-13ppt</td><td>1ppt</td><td>-7ppt</td><td>-3ppt</td><td>-8ppt</td><td>8ppt</td><td></td></tr><tr><td>Topcon G12R China (USS)</td><td>-7%</td><td>-3%</td><td>1%</td><td>6%</td><td>-9ppt</td><td>-16ppt</td><td>-14ppt</td><td>0ppt</td><td>-8ppt</td><td>-4ppt</td><td>-9ppt</td><td>9ppt</td><td></td></tr><tr><td>Topcon G12L China (DS)</td><td>-6%</td><td>-1%</td><td>2%</td><td>6%</td><td>-8ppt</td><td>-13ppt</td><td>-12ppt</td><td>2ppt</td><td>-6ppt</td><td>-3ppt</td><td>-8ppt</td><td>8ppt</td><td></td></tr><tr><td>Module-Tier 1</td><td>11%</td><td>12%</td><td>10%</td><td>5%</td><td>2ppt</td><td>8ppt</td><td>5ppt</td><td>4ppt</td><td>18ppt</td><td>3ppt</td><td>10ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (pure module)</td><td>12%</td><td>12%</td><td>9%</td><td>2%</td><td>4ppt</td><td>13ppt</td><td>10ppt</td><td>3ppt</td><td>22ppt</td><td>4ppt</td><td>15ppt</td><td>-1ppt</td><td></td></tr><tr><td>Topcon China (poly to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>6%</td><td>1ppt</td><td>7ppt</td><td>2ppt</td><td>4ppt</td><td>14ppt</td><td>3ppt</td><td>7ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (wafer to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>5%</td><td>1ppt</td><td>7ppt</td><td>5ppt</td><td>4ppt</td><td>17ppt</td><td>3ppt</td><td>9ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (cell to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>5%</td><td>1ppt</td><td>6ppt</td><td>4ppt</td><td>3ppt</td><td>19ppt</td><td>2ppt</td><td>10ppt</td><td>3ppt</td><td></td></tr><tr><td>Glass-Tier 1</td><td>-33%</td><td>-37%</td><td>-25%</td><td>-10%</td><td>-3ppt</td><td>-27ppt</td><td>-46ppt</td><td>-24ppt</td><td>-41ppt</td><td>-9ppt</td><td>-28ppt</td><td>-19ppt</td><td></td></tr><tr><td>2.0mm PV glass</td><td>-33%</td><td>-37%</td><td>-25%</td><td>-10%</td><td>-3ppt</td><td>-27ppt</td><td>-46ppt</td><td>-24ppt</td><td>-41ppt</td><td>-9ppt</td><td>-28ppt</td><td>-19ppt</td><td></td></tr><tr><td>Film-Tier 1</td><td>23%</td><td>24%</td><td>26%</td><td>25%</td><td>-7ppt</td><td>-3ppt</td><td>-2ppt</td><td>1ppt</td><td>-1ppt</td><td>-3ppt</td><td>3ppt</td><td>4ppt</td><td></td></tr><tr><td>EVA film</td><td>19%</td><td>20%</td><td>23%</td><td>16%</td><td>-12ppt</td><td>7ppt</td><td>6ppt</td><td>6ppt</td><td>9ppt</td><td>-4ppt</td><td>15ppt</td><td>5ppt</td><td></td></tr><tr><td>POE film</td><td>27%</td><td>27%</td><td>29%</td><td>33%</td><td>-1ppt</td><td>-12ppt</td><td>-11ppt</td><td>-4ppt</td><td>-11ppt</td><td>-1ppt</td><td>-9ppt</td><td>2ppt</td><td></td></tr><tr><td

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the

products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
