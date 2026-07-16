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
## Ebara (6361.T): IR Day raises expectations for semiconductor-driven sales growth and wider profit margins in each business; reiterate Buy

Ebara held its IR Day event from 1:30 PM (JST) on July 14, providing an update on strategies for the precision machinery, energy, and building service & industrial segments, which the company positions as its three pillars in its medium-term plan. While company commentary was essentially in line with the medium-term plan announced in February, we think it underlined scope for profitability improvements, as Ebara discussed specific measures aimed at expanding profit margins for the energy and building service & industrial segments. It also confirmed that the business environment for the precision machinery segment is stronger than assumed under the medium-term plan. Below, we summarize the main points of the company's comments.

We continue to see a high likelihood that Ebara will revise up its company-wide orders, sales, and profit guidance, including for precision machinery, at its 2Q results given strong capex appetite at key semiconductor customers. We also see substantial room for the valuation multiple to expand as awareness of the stock broadens among a wider range of investors, and we reiterate our Buy rating.

## Precision machinery: demand remains stronger than company expected

Market environment: Demand looks strong heading into 2026-2027, and there is strong potential for the growth rate to be higher than indicated at the 2025 IR Day (9% CAGR for CMP systems) or in the medium-term plan announced in February (8% CAGR for the WFE market). The company continues to think the CMP market will outperform WFE market growth, and aims for a precision machinery sales growth rate above that of the market. Regarding production capacity for CMP systems, the completion of the K3 building at the Kumamoto plant means the company is well-positioned to fully meet currently visible demand, and investments for future capacity expansion are currently under consideration.

Pricing strategy: Ebara plans to pass rising costs in an inflationary environment onto product prices. Recognizing the difficulty of raising prices for the same product, it aims to raise ASP and improve profitability by increasing the value add of its equipment.

Energy: Orders on a recovery trend entering FY12/26; room for profit

## Shuhei Nakamura

+81(3)4587-9932 | shuhei.nakamura@gs.com GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

## margin expansion through own efforts

Business environment: FY12/26 guidance calls for lower sales and profits in the wake of sluggish product orders in FY12/25. However, in FY12/26 the company has already secured orders for relatively high-margin upstream/midstream sectors in the Middle East, and with multiple projects anticipated up ahead, orders are expanding smoothly toward achieving the FY12/28 sales guidance. Going forward, Ebara aims to expand market share through the transition to using electric motors for powering compressors in the LNG field, automation investments/delivery time reductions at its US manufacturing sites, and optimization of S&S sites (expanding them in areas closer to customer business activities).

Profitability: Ebara aims to boost OPM to 14.5% in FY12/28 from 11.9% in FY12/25, with about half of the increase to come from orders/sales expansion, and the remaining half from profitability improvements driven by internal efforts (not necessarily dependent on sales expansion).

## Building service & industrial: Aiming for margin expansion driven by both sales growth and operational efficiency

Profitability: Looking to transform the business structure, Ebara aims to drive sales growth by expanding sales of products for data centers and the semiconductor market (chillers, cooling pumps). At the same time, it is also proceeding with efficiency improvements in existing businesses, such as optimizing its structure in line with the slump in the Chinese construction market. The company expects the benefits of these efforts to emerge gradually from FY12/26.

Service (S&S) ratio: The S&S ratio was c.23% of segment sales in FY12/25, with the company aiming to expand this to 30% in the medium term. The ratio has recently risen by a few percentage points via wider use of the EBARA Maintenance Cloud and other tools, and given that profit margins on services are about 1.5-2X higher than for products, the company expects margin expansion in the segment.

<table><tr><td colspan="16">Ebara (6361.T)</td></tr><tr><td>(JPY mn)</td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td>CoE</td><td>CoE</td><td>CoE</td><td></td><td></td><td></td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td>CoE</td></tr><tr><td>Consolidated income statement</td><td>12/2025</td><td>12/2026</td><td>12/2027</td><td>12/2028</td><td>12/2026</td><td>12/2028</td><td>12/2035</td><td>12/2025 1Q</td><td>12/2025 2Q</td><td>12/2025 3Q</td><td>12/2025 4Q</td><td>12/2026 1Q</td><td>12/2026 2Q</td><td>12/2026 3Q</td><td>12/2026 4Q</td></tr><tr><td>Sales</td><td>958,285</td><td>1,043,100</td><td>1,193,200</td><td>1,330,800</td><td>1,020,000</td><td>1,200,000</td><td>2,000,000</td><td>212,650</td><td>236,118</td><td>214,787</td><td>294,730</td><td>246,311</td><td>235,700</td><td>274,200</td><td>286,889</td></tr><tr><td>Operating profits</td><td>113,802</td><td>137,600</td><td>188,000</td><td>232,900</td><td>125,000</td><td>174,000</td><td>400,000</td><td>22,601</td><td>27,461</td><td>19,479</td><td>44,261</td><td>26,749</td><td>25,000</td><td>42,700</td><td>43,151</td></tr><tr><td>Net income</td><td>76,633</td><td>112,000</td><td>134,400</td><td>167,300</td><td>99,500</td><td></td><td></td><td>15,789</td><td>15,552</td><td>13,342</td><td>31,950</td><td>18,322</td><td>16,800</td><td>29,500</td><td>47,378</td></tr><tr><td>EBITDA</td><td>148,606</td><td>179,600</td><td>233,800</td><td>282,700</td><td>167,000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profits</td><td>32.6%</td><td>33.7%</td><td>35.0%</td><td>36.0%</td><td></td><td></td><td></td><td>32.2%</td><td>32.4%</td><td>31.3%</td><td>33.9%</td><td>31.6%</td><td></td><td></td><td></td></tr><tr><td>EBITDA</td><td>15.5%</td><td>17.2%</td><td>19.6%</td><td>21.2%</td><td>16.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profits</td><td>11.9%</td><td>13.2%</td><td>15.8%</td><td>17.5%</td><td>12.3%</td><td>14.5%</td><td>20.0%</td><td>10.6%</td><td>11.6%</td><td>9.1%</td><td>15.0%</td><td>10.9%</td><td>10.6%</td><td>15.6%</td><td>15.0%</td></tr><tr><td>Net income</td><td>8.0%</td><td>10.7%</td><td>11.3%</td><td>12.6%</td><td>9.8%</td><td></td><td></td><td>7.4%</td><td>6.6%</td><td>6.2%</td><td>10.8%</td><td>7.4%</td><td>7.1%</td><td>10.8%</td><td>16.5%</td></tr><tr><td>R&amp;D</td><td>23,200</td><td>26,000</td><td>27,500</td><td>29,000</td><td>25,000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D&amp;A</td><td>34,804</td><td>42,000</td><td>45,800</td><td>49,800</td><td>42,000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Capex</td><td>100,735</td><td>99,000</td><td>75,000</td><td>80,000</td><td>99,000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EPS (JPY)</td><td>166.3</td><td>246.4</td><td>299.6</td><td>381.5</td><td>217.9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DPS (JPY)</td><td>59.0</td><td>86.0</td><td>105.0</td><td>134.0</td><td>66.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BPS (JPY)</td><td>1,114.5</td><td>1,257.8</td><td>1,402.4</td><td>1,567.8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Orders by business segment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Precision Machinery</td><td>303,447</td><td>488,100</td><td>603,600</td><td>665,400</td><td>405,000</td><td></td><td></td><td>73,980</td><td>67,322</td><td>59,760</td><td>102,385</td><td>151,225</td><td>80,000</td><td>125,000</td><td>131,875</td></tr><tr><td>Energy</td><td>194,777</td><td>193,300</td><td>215,800</td><td>221,000</td><td>210,000</td><td></td><td></td><td>42,346</td><td>44,567</td><td>64,042</td><td>43,822</td><td>55,752</td><td>50,000</td><td>45,000</td><td>42,548</td></tr><tr><td>Building Service &amp; Industrial</td><td>249,285</td><td>250,200</td><td>262,400</td><td>275,100</td><td>265,000</td><td></td><td></td><td>59,799</td><td>65,734</td><td>62,771</td><td>60,981</td><td>70,375</td><td>59,200</td><td>61,200</td><td>59,425</td></tr><tr><td>Infrastructure</td><td>62,973</td><td>63,000</td><td>65,000</td><td>67,000</td><td>60,000</td><td></td><td></td><td>20,073</td><td>11,108</td><td>14,458</td><td>17,334</td><td>14,783</td><td>15,000</td><td>15,000</td><td>18,217</td></tr><tr><td>Environmental Solutions</td><td>135,392</td><td>125,000</td><td>125,000</td><td>125,000</td><td>130,000</td><td></td><td></td><td>3,382</td><td>62,457</td><td>27,527</td><td>42,026</td><td>32,494</td><td>75,000</td><td>5,000</td><td>12,506</td></tr><tr><td>Other</td><td>3,808</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>275</td><td>275</td><td>283</td><td>2,975</td><td>320</td><td>0</td><td>0</td><td>(320)</td></tr><tr><td>Total</td><td>949,683</td><td>1,119,600</td><td>1,271,800</td><td>1,353,500</td><td>1,070,000</td><td></td><td></td><td>199,857</td><td>251,462</td><td>228,843</td><td>269,521</td><td>324,951</td><td>279,200</td><td>251,200</td><td>264,251</td></tr><tr><td>Sales by business segment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Precision Machinery</td><td>342,268</td><td>439,000</td><td>557,000</td><td>665,400</td><td>400,000</td><td></td><td></td><td>62,406</td><td>88,150</td><td>72,761</td><td>118,951</td><td>82,949</td><td>97,000</td><td>125,000</td><td>134,051</td></tr><tr><td>Energy</td><td>218,894</td><td>197,000</td><td>211,500</td><td>222,000</td><td>205,000</td><td></td><td></td><td>48,677</td><td>60,998</td><td>50,484</td><td>58,735</td><td>46,575</td><td>48,000</td><td>54,000</td><td>47,525</td></tr><tr><td>Building Service &amp; Industrial</td><td>243,448</td><td>251,800</td><td>264,100</td><td>276,900</td><td>260,000</td><td></td><td></td><td>56,684</td><td>57,830</td><td>59,811</td><td>69,123</td><td>63,075</td><td>59,200</td><td>61,200</td><td>66,725</td></tr><tr><td>Infrastructure</td><td>57,192</td><td>60,900</td><td>63,000</td><td>64,600</td><td>60,000</td><td></td><td></td><td>21,552</td><td>11,121</td><td>9,109</td><td>15,410</td><td>23,271</td><td>11,500</td><td>10,000</td><td>16,029</td></tr><tr><td>Environmental Solutions</td><td>97,981</td><td>97,100</td><td>100,500</td><td>104,900</td><td>95,000</td><td></td><td></td><td>23,501</td><td>18,623</td><td>22,801</td><td>33,056</td><td>30,138</td><td>20,000</td><td>24,000</td><td>22,862</td></tr><tr><td>Other</td><td>2,568</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>624</td><td>627</td><td>680</td><td>637</td><td>300</td><td>0</td><td>0</td><td>(300)</td></tr><tr><td>Elimination/corporate</td><td>(4,109)</td><td>(2,700)</td><td>(2,900)</td><td>(3,000)</td><td>0</td><td></td><td></td><td>(792)</td><td>(1,235)</td><td>(859)</td><td>(1,223)</td><td>246,311</td><td>235,700</td><td>274,200</td><td>286,892</td></tr><tr><td>Total</td><td>958,285</td><td>1,043,100</td><td>1,193,200</td><td>1,330,800</td><td>1,020,000</td><td>1,200,000</td><td>2,000,000</td><td>212,650</td><td>236,118</td><td>214,787</td><td>294,735</td><td>246,311</td><td>235,700</td><td>274,200</td><td>286,889</td></tr><tr><td>Op. profit by business segment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Precision Machinery</td><td>57,773</td><td>89,900</td><td>133,900</td><td>173,300</td><td>73,500</td><td></td><td></td><td>8,257</td><td>15,194</td><td>9,421</td><td>24,901</td><td>13,531</td><td>17,000</td><td>31,200</td><td>28,169</td></tr><tr><td>Energy</td><td>25,943</td><td>17,300</td><td>21,800</td><td>25,000</td><td>21,000</td><td></td><td></td><td>1,979</td><td>9,195</td><td>5,898</td><td>8,871</td><td>(1,666)</td><td>4,600</td><td>7,600</td><td>6,766</td></tr><tr><td>Building Service &amp; Industrial</td><td>15,251</td><td>18,400</td><td>20,100</td><td>22,000</td><td>19,000</td><td></td><td></td><td>4,332</td><td>2,533</td><td>3,734</td><td>4,652</td><td>4,408</td><td>3,900</td><td>4,500</td><td>5,592</td></tr><tr><td>Infrastructure</td><td>4,680</td><td>5,700</td><td>6,000</td><td>6,100</td><td>5,500</td><td></td><td></td><td>5,598</td><td>10</td><td>(1,941)</td><td>1,013</td><td>6,126</td><td>0</td><td>(1,500)</td><td>1,074</td></tr><tr><td>Environmental Solutions</td><td>13,003</td><td>9,800</td><td>10,200</td><td>11,000</td><td>9,500</td><td></td><td></td><td>3,038</td><td>1,390</td><td>2,848</td><td>5,727</td><td>6,174</td><td>300</td><td>1,600</td><td>1,726</td></tr><tr><td>Other</td><td>(2,294)</td><td>(3,500)</td><td>(4,000)</td><td>(4,500)</td><td>(3,500)</td><td></td><td></td><td>(655)</td><td>(695)</td><td>(343)</td><td>(601)</td><td>(1,675)</td><td>(800)</td><td>(700)</td><td>(325)</td></tr><tr><td>Elimination/corporate</td><td>(556)</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>51</td><td>(166)</td><td>(139)</td><td>(302)</td><td>(149)</td><td>0</td><td>0</td><td>149</td></tr><tr><td>Total</td><td>113,802</td><td>137,600</td><td>188,000</td><td>232,900</td><td>125,000</td><td>174,000</td><td>400,000</td><td>22,601</td><td>27,461</td><td>19,479</td><td>44,261</td><td>26,749</td><td>25,000</td><td>24,700</td><td>43,151</td></tr><tr><td>OPM by business segment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Precision Machinery</td><td>16.9%</td><td>20.5%</td><td>24.0%</td><td>26.0%</td><td>18.4%</td><td></td><td></td><td>13.2%</td><td>17.2%</td><td>12.9%</td><td>20.9%</td><td>16.3%</td><td>17.5%</td><td>25.0%</td><td>21.0%</td></tr><tr><td>Energy</td><td>11.9%</td><td>8.8%</td><td>10.3%</td><td>11.3%</td><td>10.2%</td><td></td><td></td><td>4.1%</td><td>15.1%</td><td>11.7%</td><td>15.1%</td><td>-3.6%</td><td>9.6%</td><td>14.1%</td><td>14.2%</td></tr><tr><td>Building Service &amp; Industrial</td><td>6.3%</td><td>7.3%</td><td>7.6%</td><td>7.9%</td><td>7.3%</td><td></td><td></td><td>7.6%</td><td>4.4%</td><td>6.2%</td><td>6.7%</td><td>7.0%</td><td>6.6%</td><td>7.4%</td><td>8.4%</td></tr><tr><td>Infrastructure</td><td>8.2%</td><td>9.4%</td><td>9.5%</td><td>9.4%</td><td>9.2%</td><td></td><td></td><td>26.0%</td><td>0.1%</td><td>-21.3%</td><td>6.6%</td><td>26.3%</td><td>0.0%</td><td>-15.0%</td><td>6.7%</td></tr><tr><td>Environmental Solutions</td><td>13.3%</td><td>10.1%</td><td>10.1%</td><td>10.5%</td><td>10.0%</td><td></td><td></td><td>12.9%</td><td>7.5%</td><td>12.5%</td><td>17.3%</td><td>20.5%</td><td>1.5%</td><td>6.7%</td><td>7.5%</td></tr><tr><td>Total</td><td>11.9%</td><td>13.2%</td><td>15.8%</td><td>17.5%</td><td>12.3%</td><td>14.5%</td><td>20.0%</td><td>10.6%</td><td>11.6%</td><

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
