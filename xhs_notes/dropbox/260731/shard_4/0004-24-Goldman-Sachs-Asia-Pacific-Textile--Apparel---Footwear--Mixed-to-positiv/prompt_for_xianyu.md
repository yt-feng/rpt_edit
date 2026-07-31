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
# Asia Pacific Textile, Apparel & Footwear: Mixed-to-positive read-across from adidas 2Q26 results

adidas (ADSGn.DE, covered by Richard Edwards) reported largely in-line 2Q26 results with 2Q26 cFX sales +14% (company-compiled consensus +13% yoy) led by solid apparel and DTC growth. Full-year topline guidance was raised with FY26 cFX sales now expected to grow 9%-10% from +HSD% previously (1H26 cFX sales +14% yoy, ahead of full-year guidance). We see a mixed-to-positive read-across to our covered OEMs, distributors and local brands.

In 2Q26, adidas China revenue maintained the above-industry growth at cFX +15% yoy. Though slightly moderated from +17% last quarter, this still meaningfully outpaced peers as Nike China declined -17% yoy in the May quarter, Pou Sheng was -3% yoy in 2Q26, and major domestic sportswear brands/retailers' sell-through growth (Anta brand/Fila/Li Ning/Xtep delivered +LSD/+LSD/-LSD/-MSD growth in 2Q26).

1. We view it positive-to-mixed on OEMs: we expect adidas orders to remain a key growth driver for our covered OEMs in 2026-27, underpinned by the strong brand momentum and wallet share gains. We also see growth engines outside of classics footwear product cycle concerns: performance category accelerated to +39% led by +DD% growth in Football, Running, and Motorsport as well as +HSD% in Training, while lifestyle category moderated to +2% (+6% in 1Q26) due to industry discount pressure in lifestyle footwear category. By category, apparel accelerated to +35% cFX yoy, driven by +DD% apparel growth in Football and Originals, and strong increases in Running, Training, Motorsport, and US Sports, implying a better outlook for apparel makers; on the other hand, footwear slowed to +1% cFX yoy mainly on a lag in lifestyle footwear due to competition and discounting which implies pressure among footwear OEMs, but mgmt expects footwear growth to improve into 4Q26/1Q27 as order books improve and channel inventory normalizes. 2Q26 inventory +12% cFX yoy was slightly slower than cFX sales growth, with the overall inventory structure remaining healthy. On oil-price related cost increase, the company noted that oil prices have been off-peak and the cost impact on raw material/freight has been under control given costs have been locked in. On balance, we believe apparel maker Shenzhou should benefit the most from solid adidas momentum especially in apparel/China. Footwear makers face competition, but on the positive side, mgmt's constructive outlook into 4Q26/1Q27 may benefit future orders. Huali would still benefit from solid wallet share gain in adidas supply chain this year, while Yue Yuen may focus on high-end adidas orders.

Michelle Cheng
+852-2978-6631 |
michelle.cheng@gs.com
GS (Asia) L.L.C.

Keira Liu
+852-2978-0473 | keira.liu@gs.com
GS (Asia) L.L.C.

Molly Dai
+852-3966-4000 | molly.dai@gs.com
GS (Asia) L.L.C.

Xinyu Ruan
+852-2978-7347 | xinyu.ruan@gs.com
GS (Asia) L.L.C.

2. Relatively positive for distributors: on the positive side, 1) we are encouraged to see adidas China continued to take share in 2Q26 thanks to successful execution of localization strategy, as seen from the local events / products e.g. the backyard legends activation event in Shanghai, the premium lux collection launched in the China market; 2) the company has been increasing local-for-local sourcing in China which should improve supply chain efficiency, reduce inventory take backs from distributors and alleviate inventory concerns. Despite this, 1) we believe that adidas's solid reported figures may not fully translate into retailers' growth given retailers have been more skewed to offline retail, 2) Nike as the largest competitor for adidas and largest brand for Topsports/Pou Sheng still struggles.

3. Negative for domestic brands: adidas' continued momentum despite a relatively soft macro backdrop underscores the strength of its product innovation, brand equity, marketing, channel management, and localization capabilities, and could intensify competition. Meanwhile, the overall macro and demand backdrop remains challenging; as a reference, we previously removed sportswear brand from our preferred sector list considering the fluid 2Q26 demand and weaker than expected pricing trends. On the positive side, the market share gain opportunities from Nike's prolonged adjustment and slower reset could offer opportunities for domestic brands, though we need to closely monitor Nike's strategy on potential inventory management from these online channels which could lead to a more promotional environment.

Within the whole apparel/footwear value chain, we like Anta's multiple brand strategies to capture different demand scenarios with an in-line 2Q26 and above-expectation 1H26 run-rate.

By market: cFX revenues for the adidas brand increased +14% yoy, reflecting its continued broad-based momentum. By region, cFX revenues were LATAM +28% yoy, Emerging Markets +12% yoy, Europe +6% yoy, Greater China +15% yoy, Japan/South Korea +18% yoy and North America +17% yoy.

Greater China: mgmt highlighted Greater China's strong momentum (+15% yoy) continued to be supported by the localization strategy. 2Q China Gross margin improved 1.9 pp yoy to 56.0%, and China 2Q EBIT margin came in at 23.0% (+0.3pp yoy).

By category: Apparel sales grew cFX 35% yoy in Q2 (vs. +31% in 1Q26) driven by double-digit increases in Football and Originals, also strong increases in Running, Training, Motorsport, and US Sports. Footwear revenues for the adidas brand grew cFX +1% yoy in Q2 (vs. +4% in 1Q26), and the company noted the strong product offering drove double-digit footwear increases in several performance categories, led by Running and Training, alongside strong growth in many lifestyle footwear franchises. Though footwear moderated from 1Q26, mgmt expects footwear growth to improve into 4Q26/1Q27 as the order book for wholesale improves and channel inventory normalizes.

Inventories increased 13% by Jun-quarter and were up 12% yoy Cfx, slower than cFX sales growth. End-Jun inventory (\~€6.0bn) was slightly higher than end-Mar (\~€5.8bn) mainly due to lower than expected Middle-East sell-through. Overall the inventory structure remained healthy with only 9% from previous seasons.

Exhibit 1: adidas recorded a $15\%$ yoy sales growth in Greater China in 2Q26  
Greater China FX-neutral sales growth, yoy  
![](images/daddd1c168e998d819bc4de751935696e7dbe57a62942d586b74e4cd295edd06.jpg)

Exhibit 2: adidas group global cFX sales grew by $14\%$ yoy in 2Q26 Sales growth comparison for adidas vs. Nike globally  
![](images/b288b47988e3965ef0892e8c460e28390d44b9f2590400640b605d2ce3143869.jpg)  
Source: Company data  
Source: Company data  
Exhibit 3: adidas inventory was up $13\%$ yoy in 2Q26 Total inventory growth yoy

![](images/cdc83c8b4bea49504f667d29ef1445e406094055d1727fe0ec0c7952d78243bd.jpg)  
Source: Company data

Exhibit 4: adidas yoy inventory growth in-line with sales growth in 2Q26. Global brands - gap between yoy sales growth and inventory growth

<table><tr><td rowspan="2">Sub-sector</td><td rowspan="2">Company</td><td colspan="18">Gap between Sales yoy growth and Inventory yoy growth</td></tr><tr><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td rowspan="2">Sports retailers</td><td>Dick&#x27;s Sporting Goods</td><td>-48%</td><td>-54%</td><td>-27%</td><td>-16%</td><td>-2%</td><td>8%</td><td>5%</td><td>7%</td><td>1%</td><td>-4%</td><td>-13%</td><td>-17%</td><td>-6%</td><td>-2%</td><td>-15%</td><td>13%</td><td>11%</td><td></td></tr><tr><td>JD Sports</td><td></td><td>-30%</td><td></td><td>-26%</td><td></td><td>-5%</td><td></td><td>-15%</td><td></td><td>-19%</td><td></td><td>-6%</td><td></td><td>4%</td><td></td><td>4%</td><td></td><td></td></tr><tr><td rowspan="5">Retailers</td><td>Target Corp.</td><td>-39%</td><td>-33%</td><td>-11%</td><td>4%</td><td>17%</td><td>12%</td><td>10%</td><td>14%</td><td>4%</td><td>3%</td><td>-2%</td><td>-10%</td><td>-14%</td><td>-3%</td><td>0%</td><td>2%</td><td>12%</td><td></td></tr><tr><td>Walmart Inc.</td><td>-30%</td><td>-17%</td><td>-4%</td><td>7%</td><td>15%</td><td>11%</td><td>6%</td><td>9%</td><td>9%</td><td>7%</td><td>6%</td><td>1%</td><td>-1%</td><td>1%</td><td>3%</td><td>1%</td><td>-2%</td><td></td></tr><tr><td>Academy Sports</td><td>-30%</td><td>-23%</td><td>-19%</td><td>-13%</td><td>-10%</td><td>-6%</td><td>-6%</td><td>10%</td><td>1%</td><td>-7%</td><td>-6%</td><td>-16%</td><td>-16%</td><td>-13%</td><td>-9%</td><td>-12%</td><td>1%</td><td></td></tr><tr><td>B&amp;M</td><td>-56%</td><td></td><td>12%</td><td></td><td>21%</td><td></td><td>5%</td><td></td><td>15%</td><td></td><td>-12%</td><td>0%</td><td>-18%</td><td></td><td>1%</td><td></td><td>8%</td><td></td></tr><tr><td>Pepco Group</td><td>-10%</td><td></td><td>-46%</td><td></td><td>-13%</td><td></td><td>-2%</td><td></td><td>13%</td><td></td><td>-6%</td><td></td><td>-13%</td><td></td><td>1%</td><td></td><td>6%</td><td></td></tr><tr><td rowspan="10">Fashion/Casual</td><td>Gap Inc.</td><td>-47%</td><td>-46%</td><td>-9%</td><td>15%</td><td>22%</td><td>21%</td><td>15%</td><td>18%</td><td>19%</td><td>10%</td><td>4%</td><td>-7%</td><td>-5%</td><td>-9%</td><td>-3%</td><td>-5%</td><td>1%</td><td></td></tr><tr><td>Fast retailing</td><td>3%</td><td>8%</td><td>0%</td><td>-27%</td><td>2%</td><td>14%</td><td>24%</td><td>28%</td><td>10%</td><td>9%</td><td>13%</td><td>5%</td><td>3%</td><td>-3%</td><td>-1%</td><td>8%</td><td>6%</td><td>11%</td></tr><tr><td>Ralph Lauren Corp.</td><td>-10%</td><td>-38%</td><td>-31%</td><td>-32%</td><td>-8%</td><td>0%</td><td>9%</td><td>20%</td><td>18%</td><td>14%</td><td>11%</td><td>16%</td><td>3%</td><td>-4%</td><td>5%</td><td>-3%</td><td>10%</td><td></td></tr><tr><td>PVH Corp.</td><td>6%</td><td>-27%</td><td>-34%</td><td>-31%</td><td>-22%</td><td>-3%</td><td>23%</td><td>21%</td><td>12%</td><td>6%</td><td>-13%</td><td>-11%</td><td>-17%</td><td>-9%</td><td>-2%</td><td>1%</td><td>7%</td><td></td></tr><tr><td>Torrid Holdings Inc.</td><td>-59%</td><td>-61%</td><td>-31%</td><td>-10%</td><td>-8%</td><td>-2%</td><td>9%</td><td>18%</td><td>12%</td><td>17%</td><td>15%</td><td>-11%</td><td>-8%</td><td>-9%</td><td>-4%</td><td>-6%</td><td>-3%</td><td></td></tr><tr><td>Levi Strauss &amp; Co.</td><td>1%</td><td>-14%</td><td>-42%</td><td>-63%</td><td>-27%</td><td>-27%</td><td>-7%</td><td>12%</td><td>6%</td><td>15%</td><td>8%</td><td>16%</td><td>5%</td><td>-2%</td><td>1%</td><td>-4%</td><td>10%</td><td>15%</td></tr><tr><td>Kontoor Brands Inc.</td><td>-19%</td><td>-8%</td><td>-73%</td><td>-57%</td><td>-54%</td><td>-16%</td><td>19%</td><td>8%</td><td>19%</td><td>21%</td><td>26%</td><td>26%</td><td>10%</td><td>-32%</td><td>-38%</td><td>0%</td><td>-6%</td><td></td></tr><tr><td>Hennes &amp; Mauritz</td><td>16%</td><td>1%</td><td>-25%</td><td>-4%</td><td>7%</td><td>12%</td><td>20%</td><td>12%</td><td>6%</td><td>4%</td><td>-7%</td><td>-9%</td><td>-6%</td><td>-6%</td><td>6%</td><td>7%</td><td>5%</td><td></td></tr><tr><td>Inditex</td><td>9%</td><td>-27%</td><td>-16%</td><td>8%</td><td>8%</td><td>21%</td><td>12%</td><td>16%</td><td>10%</td><td>9%</td><td>9%</td><td>-4%</td><td>-5%</td><td>-1%</td><td>0%</td><td>6%</td><td>5%</td><td></td></tr><tr><td>Canada Goose</td><td>12%</td><td>24%</td><td>10%</td><td>-42%</td><td>15%</td><td>-4%</td><td>-40%</td><td>7%</td><td>28%</td><td>11%</td><td>4%</td><td>15%</td><td>21%</td><td>32%</td><td>4%</td><td>14%</td><td>17%</td><td></td></tr><tr><td rowspan="10">Sportswear</td><td>Nike Inc.</td><td>-10%</td><td>-24%</td><td>-41%</td><td>-26%</td><td>-2%</td><td>4%</td><td>12%</td><td>15%</td><td>14%</td><td>9%</td><td>-5%</td><td>-8%</td><td>-7%</td><td>-12%</td><td>3%</td><td>4%</td><td>1%</td><td>-4%</td></tr><tr><td>adidas</td><td>-15%</td><td>-25%</td><td>-61%</td><td>-48%</td><td>-25%</td><td>-6%</td><td>17%</td><td>17%</td><td>25%</td><td>27%</td><td>14%</td><td>14%</td><td>-2%</td><td>-14%</td><td>-18%</td><td>-15%</td><td>-7%</td><td>0%</td></tr><tr><td>Puma</td><td>-9%</td><td>-17%</td><td>-48%</td><td>-26%</td><td>-18%</td><td>-2%</td><td>18%</td><td>15%</td><td>13%</td><td>8%</td><td>3%</td><td>-17%</td><td>-22%</td><td>-18%</td><td>-33%</td><td>-32%</td><td>2%</td><td></td></tr><tr><td>Under Armour</td><td>7%</td><td>-8%</td><td>-27%</td><td>-47%</td><td>-37%</td><td>-41%</td><td>-6%</td><td>3%</td><td>15%</td><td>5%</td><td>-7%</td><td>-5%</td><td>-10%</td><td>-6%</td><td>2%</td><td>-3%</td><td>2%</td><td></td></tr><tr><td>Lululemon</td><td>-42%</td><td>-56%</td><td>-56%</td><td>-20%</td><td>0%</td><td>5%</td><td>23%</td><td>24%</td><td>25%</td><td>21%</td><td>0%</td><td>4%</td><td>-15%</td><td>-14%</td><td>-4%</td><td>-17%</td><td>2%</td><td></td></tr><tr><td>VF Corp.</td><td>-24%</td><td>-89%</td><td>-91%</td><td>-104%</td><td>-65%</td><td>-27%</td><td>8%</td><td>1%</td><td>10%</td><td>16%</td><td>7%</td><td>12%</td><td>-2%</td><td>-9%</td><td>13%</td><td>9%</td><td>17%</td><td>6%</td></tr><tr><td>ON Holding</td><td></td><td></td><td>-30%</td><td></td><td>-108%</td><td>-49%</td><td>-15%</td><td>32%</td><td>42%</td><td>36%</td><td>50%</td><td>18%</td><td>34%</td><td>42%</td><td>16%</td><td>22%</td><td>13%</td><td></td></tr><tr><td>Asics Corp.</td><td>-8%</td><td>-1%</td><td>-31%</td><td>-19%</td><td>10%</td><td>-10%</td><td>14%</td><td>11%</td><td>27%</td><td>32%</td><td>26%</td><td>12%</td><td>12%</td><td>7%</td><td>0%</td><td>-9%</td><td>-6%</td><td></td></tr><tr><td>Amer Sports</td><td>4%</td><td>0%</td><td>-33%</td><td>-37%</td><td>-31%</td><td>-43%</td><td>-1%</td><td>-11%</td><td>7%</td><td>15%</td><td>6%</td><td>13%</td><td>8%</td><td>-5%</td><td>2%</td><td>-4%</td><td>-1%</td><td></td></tr><tr><td>Deckers</td><td>-51%</td><td>-62%</td><td>-24%</td><td>-18%</td><td>2%</td><td>22%</td><td>46%</td><td>41%</td><td>32%</td><td>20%</td><td>13%</td><td>10%</td><td>2%</td><td>4%</td><td>2%</td><td>-3%</td><td>11%</td><td>11%</td></tr></table>

Source: Company data, Data compiled by GS Global Investment Research

## Exhibit 5: adidas FX-neutral growth by geography

<table><tr><td></td><td>Europe</td><td>North America</td><td>Latin America</td><td>Greater China</td><td>EMEA</td><td>Other Asian markets</td><td>Japan</td><td>Japan/ South Korea</td><td>MEAA</td><td>APAC (China excluded)</td><td>Emerging Markets</td><td>Russia/ CIS</td><td>Total Company</td></tr><tr><td>2010</td><td>7%</td><td>12%</td><td>14%</td><td>-2%</td><td>16%</td><td>6%</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>9%</td></tr><tr><td>2011</td><td>10%</td><td>15%</td><td>10%</td><td>23%</td><td>22%</td><td>5%</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>13%</td></tr><tr><td>2012</td><td>3%</td><td>2%</td><td>8%</td><td>15%</td><td>15%</td><td>7%</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>6%</td></tr><tr><td>2013</td><td>-6%</td><td>2%</td><td>19%</td><td>7%</td><td>4%</td><td>5%</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>3%</td></tr><tr><td>2014</td><td>8%</td><td>-6%</td><td>19%</td><td>10%</td><td>19%</td><td>2%</td><td>-</td><td></td><td>-</td><td>-</td><td>-</td><td>-</td><td>6%</td></tr><tr><td>2015</td><td>17%</td><td>5%</td><td>12%</td><td>18%</td><td>-</td><td>-</td><td>0%</td><td></td><td>14%</td><td>-</td><td>-</td><td>-11%</td><td>10%</td></tr><tr><td>2016</td><td>20%</td><td>24%</td><td>16%</td><td>28%</td><td>-</td><td>-</td><td>16%</td><td></td><td>16%</td><td>-</td><td>-</td><td>3%</td><td>18%</td></tr><tr><td>2017</td><td>13%</td><td>27%</td><td>12%</td><td>29%</td><td>-</td><td>-</td><td>10%</td><td></td><td>10%</td><td>-</td><td>-</td><td>-13%</td><td>16%</td></tr><tr><td>201

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
