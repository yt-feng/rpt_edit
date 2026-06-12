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
## Taiwan ODMs

In-line May sales with initial ramp of Amazon T3 servers

Most Taiwan ODMs reported largely in-line revenue in May with sustained server momentum and flattish NB shipment trends. General server demand remains resilient with likely double-digit QoQ shipment growth in 2Q26. For AI servers, we expect double-digit NVL72 rack shipment growth in 2Q26. We also saw resumed component momentum for AWS ASIC in May, implying an uptick in Trianium 3 system shipments in the coming months. For PCs, 2Q26 NB ODM outlook appears to be largely flattish QoQ. We expect a declining trend into 2H26, dragged by price elasticity impact. VGA/MB shipments appear to be down double digit % QoQ/YoY in 2Q26 and likely to see continued weakness into 2H26, due to a lack of new product and end demand weakness. iPhone EMS revenues were resilient in May driven by m/s gains and inventory preparation ahead of the China 618 sales season, but we are cautious on the 2H26 iPhone demand on the potential memory-led price elasticity impact. In the server ODM space, we prefer Wiwynn > Quanta > Hon Hai > Wistron. We stay OW on Delta given the growing AI datacenter power/thermal TAM and potential product price hikes. ASPEED and Lotes are key beneficiaries of general server strength. In the PC space, our top avoids are Micro-Star and ASUSTek.

- AI servers: Continued GB300 ramp, AWS ASIC to pick up in June. We saw continued GB300 shipment ramp in May and forecast double-digit NVL72 shipment growth in 2Q26. We see potential air pockets into 3Q26 due to product transition and anticipate VR200 system ramp in 4Q26. Overall, we estimate 65-70k NVL72 rack shipments this year. For ASIC servers, we saw component pull-in demand (e.g. server slide, power supply, chassis, CCL/PCB) for the Trainium 3 project in May and expect an initial system ramp in June, which bodes well for Wiwiynn.  
- General servers: Robust general server momentum. We saw continued general server shipment growth in May. Server shipments appear to have grown double-digits QoQ in 2Q26, which is in line with our expectations and Lotes's 2Q26 server ODM forecast (+15% QoQ). Supply chain feedback suggests accelerating momentum into 2H26 with better CPU supply. Overall, we forecast traditional server shipments to grow 20% YoY this year (vs. 30-40% demand growth due to supply constraints) and to see sustained momentum into next year due to order backlogs.  
- PCs: Demand weakness and margin pressure in coming quarters: Aggregated NB ODM shipments were up slightly MoM in May. April-May aggregated shipments were largely in line with our estimate of flattish to slightly up QoQ for 2Q26. Initial NB ODM feedback indicates a sub-seasonal 2H26 outlook (1H/2H split at \~55%/45%) and double-digit shipment decline, which echoes our cautious view from price elasticity impact. This, coupled with emerging margin pressure for PC brands in the next few quarters, could drive potential earnings downside and valuation de-rating of PC stocks, in our view.

## Technology - Hardware

## Albert Hung AC

(886-2) 2725-9875

albert.hung@jpmchase.com

JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Anthony Leng

(886-2) 2725-9240

anthony.leng@JPM.com

JPM Securities (Taiwan) Limited

## Gokul Hariharan

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

- VGA/motherboard: Double-digit shipment declines on end demand weakness. Micro-Star's MB/VGA shipments appear to have declined double digits QoQ/YoY in 2Q26 due to end demand weakness. ASUSTek and MSI have seen weaker-than-expected PC component demand, likely due to memory-led negative price elasticity. Looking ahead, we expect continued weakness into 2H26 due to the lack of new products and lackluster end demand. Overall, we forecast double-digit declines for MB/VGA shipments this year. This is negative for Micro-Star and ASUSTek, which have $40 - 50\% / 20\%$ revenue exposure from PC components, respectively.  
- Robust 1H26 iPhone demand, followed by sub-seasonal iPhone EMS build outlook in 2H. Hon Hai/Pegatron iPhone revenues were up double digits/ flattish MoM in May respectively, which were above-seasonal trends, likely driven by some m/s gains and pull-in demand ahead of the China 618 sales season. Our iPhone supply chain analyst, William Yang, expects a 7% YoY decline for 2H26 iPhone EMS build (vs. +9% YoY in 1H26) due to fewer new model launches and potential demand weakness.  
- 800V HVDC datacenter power on track to ramp late 2026/early 2027 with small volumes. We have previously highlighted the earlier-than-expected production introduction of HVDC (800v and +/- 400v) vs. our earlier expectation of a 2H27 launch. Our industry research suggests that key power system integrators are on track to introduce HVDC (800V and ±400V) in 4Q26/1Q27. HVDC is not required for VR200 racks, so we anticipate only 10–20% penetration in the VR200 cycle (still an incremental positive vs. our prior assumptions). Early deployments should skew toward ±400V given data center readiness, but we still expect meaningful power content uplift driven by sidecar power rack adoption.

Table 1: May sales summary

<table><tr><td>NT$ bn</td><td>May&#x27;26 sales</td><td>MoM (%)</td><td>YoY (%)</td><td>JPMe 2Q26</td><td>Apr-May aggregate sales as % of JPMe</td><td>Consensus 2Q26</td><td>Apr-May aggregate sales as % of Consensus</td></tr><tr><td colspan="8">PC brands</td></tr><tr><td>Asus</td><td>62.7</td><td>-19%</td><td>7%</td><td>236.0</td><td>59%</td><td>241.3</td><td>58%</td></tr><tr><td>Acer</td><td>26.2</td><td>-16%</td><td>37%</td><td>N.A.</td><td>N.A.</td><td>78.5</td><td>73%</td></tr><tr><td>MSI</td><td>15.8</td><td>-3%</td><td>-24%</td><td>55.9</td><td>57%</td><td>52.9</td><td>61%</td></tr><tr><td>Gigabyte</td><td>49.1</td><td>-6%</td><td>5%</td><td>N.A.</td><td>N.A.</td><td>131.9</td><td>77%</td></tr><tr><td colspan="8">Notebook ODMs</td></tr><tr><td>Wistron</td><td>290.2</td><td>2%</td><td>39%</td><td>860.5</td><td>67%</td><td>857.0</td><td>67%</td></tr><tr><td>Compal</td><td>70.5</td><td>-2%</td><td>22%</td><td>220.3</td><td>65%</td><td>216.5</td><td>66%</td></tr><tr><td>Inventec</td><td>82.8</td><td>-2%</td><td>35%</td><td>240.0</td><td>70%</td><td>213.7</td><td>78%</td></tr><tr><td>Quanta</td><td>311.5</td><td>-8%</td><td>94%</td><td>992.2</td><td>66%</td><td>950.5</td><td>69%</td></tr><tr><td colspan="8">iPhone EMS</td></tr><tr><td>Hon Hai</td><td>859.4</td><td>3%</td><td>40%</td><td>2,346.2</td><td>72%</td><td>2,366.0</td><td>71%</td></tr><tr><td>Pegatron</td><td>96.0</td><td>10%</td><td>12%</td><td>278.2</td><td>66%</td><td>276.2</td><td>66%</td></tr><tr><td colspan="8">Server</td></tr><tr><td>Wiwynn</td><td>84.1</td><td>2%</td><td>18%</td><td>271.8</td><td>61%</td><td>276.8</td><td>60%</td></tr><tr><td>ASPEED</td><td>1.3</td><td>0%</td><td>69%</td><td>3.8</td><td>67%</td><td>3.7</td><td>70%</td></tr><tr><td colspan="8">Components</td></tr><tr><td>Delta</td><td>59.0</td><td>0%</td><td>44%</td><td>188.7</td><td>62%</td><td>185.5</td><td>63%</td></tr><tr><td>Lotes</td><td>3.0</td><td>-10%</td><td>9%</td><td>10.2</td><td>63%</td><td>10.1</td><td>64%</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

Table 2: NVL72 rack shipment estimates

<table><tr><td>NVL72 (unit)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>Jan</td><td>Feb</td><td>Mar</td><td>1Q26</td><td>Apr</td><td>May</td><td>Jun</td><td>2Q26</td><td>2025</td><td>2026</td></tr><tr><td>Hon Hai</td><td>400</td><td>1,500</td><td>4,200</td><td>5,800</td><td>2,000</td><td>1,900</td><td>2,626</td><td>6,526</td><td>2,259</td><td>2,446</td><td>2,549</td><td>7,253</td><td>11,900</td><td>31,596</td></tr><tr><td>Quanta</td><td>150</td><td>1,400</td><td>1,600</td><td>3,300</td><td>1,300</td><td>1,300</td><td>1,800</td><td>4,400</td><td>1,750</td><td>1,550</td><td>1,900</td><td>5,200</td><td>6,450</td><td>19,400</td></tr><tr><td>Wistron</td><td>150</td><td>1,800</td><td>1,350</td><td>2,500</td><td>950</td><td>1,550</td><td>1,379</td><td>3,879</td><td>1,350</td><td>1,350</td><td>1,400</td><td>4,100</td><td>5,800</td><td>14,779</td></tr><tr><td>Others</td><td>200</td><td>300</td><td>850</td><td>1,700</td><td></td><td></td><td></td><td>2,195</td><td></td><td></td><td></td><td>2,447</td><td>3,050</td><td></td></tr><tr><td>Total</td><td>900</td><td>5,000</td><td>8,000</td><td>13,300</td><td></td><td></td><td></td><td>17,000</td><td></td><td></td><td></td><td>19,000</td><td>27,200</td><td>70,000</td></tr></table>

Source: JPM estimates, Company data.

Table 3: Taiwan ODM 2Q26 NB guidance

<table><tr><td>Companies</td><td>Ticker</td><td>2Q26 guidance - new</td><td>2Q26 guidance - old</td></tr><tr><td>Wistron</td><td>3231 TT</td><td>5-10% QoQ decline</td><td>5-10% QoQ decline</td></tr><tr><td>Compal</td><td>2324 TT</td><td>Single digit QoQ growth</td><td>Single digit QoQ growth</td></tr><tr><td>Inventec</td><td>2356 TT</td><td>Flattish QoQ</td><td>Flattish QoQ</td></tr><tr><td>Quanta</td><td>2382 TT</td><td>Slight QoQ growth</td><td>Flattish to slight QoQ growth</td></tr><tr><td>Pegatron</td><td>4938 TT</td><td>Below seasonality</td><td>Below seasonality</td></tr></table>

Source: Company data.

Table 4: Quarterly notebook shipments by ODM

<table><tr><td>Qrtly shipments</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>4,600</td><td>5,100</td><td>5,200</td><td>5,300</td><td>4,900</td><td>5,900</td><td>6,400</td><td>6,900</td><td>6,100</td><td>5,612</td></tr><tr><td>Compal (2324 TT)</td><td>7,500</td><td>8,700</td><td>8,300</td><td>7,800</td><td>7,000</td><td>7,100</td><td>7,100</td><td>6,830</td><td>5,900</td><td>6,195</td></tr><tr><td>Inventec (2356 TT)</td><td>4,500</td><td>4,900</td><td>5,200</td><td>5,400</td><td>5,000</td><td>5,600</td><td>5,400</td><td>5,300</td><td>5,400</td><td>5,400</td></tr><tr><td>Quanta (2382 TT)</td><td>10,500</td><td>11,700</td><td>12,600</td><td>11,100</td><td>10,800</td><td>12,100</td><td>12,700</td><td>10,900</td><td>10,000</td><td>10,428</td></tr><tr><td>Pegatron (4938 TT)</td><td>1,585</td><td>2,040</td><td>2,500</td><td>1,950</td><td>1,885</td><td>2,375</td><td>2,400</td><td>2,410</td><td>1,800</td><td>1,800</td></tr><tr><td>Total (K units)</td><td>28,685</td><td>32,440</td><td>33,800</td><td>31,550</td><td>29,585</td><td>33,075</td><td>34,000</td><td>32,340</td><td>29,200</td><td>29,435</td></tr><tr><td colspan="11"></td></tr><tr><td>QoQ Growth</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>-13%</td><td>11%</td><td>2%</td><td>2%</td><td>-8%</td><td>20%</td><td>8%</td><td>8%</td><td>-12%</td><td>-8%</td></tr><tr><td>Compal (2324 TT)</td><td>-10%</td><td>16%</td><td>-5%</td><td>-6%</td><td>-10%</td><td>1%</td><td>0%</td><td>-4%</td><td>-14%</td><td>5%</td></tr><tr><td>Inventec (2356 TT)</td><td>0%</td><td>9%</td><td>6%</td><td>4%</td><td>-7%</td><td>12%</td><td>-4%</td><td>-2%</td><td>2%</td><td>0%</td></tr><tr><td>Quanta (2382 TT)</td><td>1%</td><td>11%</td><td>8%</td><td>-12%</td><td>-3%</td><td>12%</td><td>5%</td><td>-14%</td><td>-8%</td><td>4%</td></tr><tr><td>Pegatron (4938 TT)</td><td>-4%</td><td>29%</td><td>23%</td><td>-22%</td><td>-3%</td><td>26%</td><td>1%</td><td>0%</td><td>-25%</td><td>0%</td></tr><tr><td>Total (m units)</td><td>-5%</td><td>13%</td><td>4%</td><td>-7%</td><td>-6%</td><td>12%</td><td>3%</td><td>-5%</td><td>-10%</td><td>1%</td></tr><tr><td colspan="11"></td></tr><tr><td>Y/Y Growth</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>18%</td><td>11%</td><td>0%</td><td>0%</td><td>7%</td><td>16%</td><td>23%</td><td>30%</td><td>24%</td><td>-5%</td></tr><tr><td>Compal (2324 TT)</td><td>-1%</td><td>0%</td><td>-11%</td><td>-6%</td><td>-7%</td><td>-18%</td><td>-14%</td><td>-12%</td><td>-16%</td><td>-13%</td></tr><tr><td>Inventec (2356 TT)</td><td>2%</td><td>0%</td><td>6%</td><td>20%</td><td>11%</td><td>14%</td><td>4%</td><td>-2%</td><td>8%</td><td>-4%</td></tr><tr><td>Quanta (2382 TT)</td><td>-3%</td><td>-7%</td><td>-4%</td><td>7%</td><td>3%</td><td>3%</td><td>1%</td><td>-2%</td><td>-7%</td><td>-14%</td></tr><tr><td>Pegatron (4938 TT)</td><td>-7%</td><td>-2%</td><td>0%</td><td>18%</td><td>19%</td><td>16%</td><td>-4%</td><td>24%</td><td>-5%</td><td>-24%</td></tr><tr><td>Total (m units)</td><td>1%</td><td>-1%</td><td>-3%</td><td>5%</td><td>3%</td><td>2%</td><td>1%</td><td>3%</td><td>-1%</td><td>-11%</td></tr></table>

Source: Company data, JPM estimates.

Figure 1: Aggregated top 3 MB vendors' quarterly shipments and qoq trend  
![](images/eab412d12435ce2b0c4dc5c942d531ff215ec0cbdb13fdc45e01467f9b6e752b.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Aggregated Top 3 motherboard vendor shipment (K unit) | qoq % (%) |
|---|---|---|
| 1Q19 | 8,500 | 1 |
| 2Q19 | 9,000 | 0 |
| 3Q19 | 14,500 | 20 |
| 4Q19 | 8,000 | -6 |
| 1Q20 | 12,500 | 3 |
| 2Q20 | 13,500 | 16 |
| 3Q20 | 12,800 | 16 |
| 4Q20 | 12,500 | -3 |
| 1Q21 | 12,800 | -2 |
| 2Q21 | 12,500 | -9 |
| 3Q21 | 12,800 | -1 |
| 4Q21 | 12,500 | 10 |
| 1Q22 | 11,500 | -10 |
| 2Q22 | 9,500 | -16 |
| 3Q22 | 10,500 | 11 |
| 4Q22 | 9,500 | 4 |
| 1Q23 | 11,500 | -5 |
| 2Q23 | 10,500 | 7 |
| 3Q23 | 11,500 | 0 |
| 4Q23 | 11,500 | -3 |
| 1Q24 | 11,500 | -2 |
| 2Q24 | 11,500 | 5 |
| 3Q24 | 11,500 | 1 |
| 4Q24 | 11,500 | 1 |
| 1Q25 | 12,500 | 14 |
| 2Q25 | 13,500 | 6 |
| 3Q25 | 12,800 | -5 |
| 4Q25 | 12,500 | -8 |
| 1Q26 | 11,500 | -11 |
</details>

Source: Company data, JPM estimates.

Figure 3: Aggregated top 3 MB vendors' quarterly shipments and yoy trend  
![](images/4c51cceee1a5be83e473f058885a0ba475201011ecc8e5f2ff53f4549efe8b1d.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Quarter | Aggregated Top 3 motherboard vendor shipment (K unit) | yoy (%) |
|---|---|---|
| 1Q19 | 9000 | -9 |
| 2Q19 | 9500 | 6 |
| 3Q19 | 10500 | 11 |
| 4Q19 | 11000 | 13 |
| 1Q20 | 12000 | 16 |
| 2Q20 | 13000 | 34 |
| 3Q20 | 12500 | 30 |
| 4Q20 | 13500 | 35 |
| 1Q21 | 12800 | 27 |
| 2Q21 | 12000 | 0 |
| 3Q21 | 13000 | -15 |
| 4Q21 | 12500 | -4 |
| 1Q22 | 11500 | -12 |
| 2Q22 | 9500 | -19 |
| 3Q22 | 10500 | -9 |
| 4Q22 | 11000 | -14 |
| 1Q23 | 11500 | -9 |
| 2Q23 | 10800 | 10 |
| 3Q23 | 11500 | 6 |
| 4Q23 | 11800 | 2 |
| 1Q24 | 11500 | 4 |
| 2Q24 | 11800 | 1 |
| 3Q24 | 12000 | -1 |
| 4Q24 | 12500 | 0 |
| 1Q25 | 13500 | 5 |
| 2Q25 | 14500 | 22 |
| 3Q25 | 13800 | 23 |
| 4Q25 | 13500 | 17 |
| 1Q26 | 11500 | -6 |
| 2Q26 | 11000 | -17 |
</details>

Source: Company data. JPM estimates.

Figure 2: Aggregated top 3 VGA card vendors' quarterly shipments and qoq trend  
![](images/e2fec9a126de00befc3a7c95085a89c9b30f82b5f7ecfd654679442ff152a0db.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Aggregated Top 3 VGA card vendor shipment (K unit) | qoq (%) |
|---|---|---|
| 1Q19 | 3500 | -5 |
| 2Q19 | 3000 | -12 |
| 3Q19 | 4000 | 30 |
| 4Q19 | 4000 | -1 |
| 1Q20 | 4500 | 9 |
| 2Q20 | 5000 | 14 |
| 3Q20 | 5000 | 4 |
| 4Q20 | 5000 | -2 |
| 1Q21 | 5000 | 1 |
| 2Q21 | 5000 | 1 |
| 3Q21 | 5000 | -11 |
| 4Q21 | 5000 | 6 |
| 1Q22 | 5000 | -13 |
| 2Q22 | 4500 | -1 |
| 3Q22 | 4000 | 2 |
| 4Q22 | 4000 | -17 |
| 1Q23 | 3500 | 22 |
| 2Q23 | 3500 | -3 |
| 3Q23 | 4500 | -2 |
| 4Q23 | 4500 | -4 |
| 1Q24 | 4500 | 8 |
| 2Q24 | 4500 | -3 |
| 3Q24 | 4500 | 0 |
| 4Q24 | 4500 | -3 |
| 1Q25 | 5500 | 22 |
| 2Q25 | 5500 | -6 |
| 3Q25 | 5500 | -2 |
| 4Q25 | 5500 | -8 |
| 1Q26 | 4500 | -9 |
</details>

Source: Company data, JPM estimates.

Figure 4: Aggregated top

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 10:51 PM HKT

Disseminated 10 Jun 2026 10:51 PM HKT
"""
