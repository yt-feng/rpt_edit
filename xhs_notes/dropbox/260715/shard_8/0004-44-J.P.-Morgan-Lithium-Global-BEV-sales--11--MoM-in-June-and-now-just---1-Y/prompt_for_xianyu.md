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
# JPM

## Lithium

## Global BEV sales +11% MoM in June and now just - 1%YTD vs 2025; China BEV penetration increased 1ppt to 43%

Key takeaways from the June EV sales data: (1) Global BEV sales (China + EU + US) rose 11% MoM to 1045k units, are up 9% YoY, with YTD sales now down just 1% vs 2025; global BEV penetration increased to 26% in June (vs 24% in May'26). (2) China BEV penetration increased 1ppt to 43% in June, with BEV sales rising 8% MoM to 685k units and total EV (BEV+PHEV) penetration remaining at 63% (the highest since August 2025). (3) US BEV sales declined 16% MoM to 73k units (from 86kt) and are down 26% YTD YoY; BEV penetration declined to 5% (from 6% in May '26). (4) EU-10 BEV sales increased 34% MoM to 287kt and are up 35% YTD YoY; BEV penetration increased to 26% (from 24% in May). The EU remains the strongest growing region on country-level subsidy schemes and affordable mass EVs penetrating the market. Spodumene has traded soft in the past couple of sessions, but we remain constructive on lithium pricing due to our projected medium term S&D deficit supported by continued ESS strength. Our top pick in the lithium space is PLS. For more information on EV/PHEV sales, please see the JPM Asia Battery/Autos research team's latest note here.

Figure 1: China vehicle sales vs. BEV sales  
![](images/4315fc3a499be8a18d3767c4b24a64532f1a3e20c8752d27a8dd2c02b2192852.jpg)  
Source: China Passenger Car Association (CPCA), company data. Note: Our China data now references retail sales vs. wholesale sales previously.

Figure 2: China EV penetration rates  
![](images/34718bf9a794348c96b9f65c136c5735ea8c06c214a16d6faa0da8e87e9a99f5.jpg)  
Battery Electric Vehicles (%) Plug-in Hybrid Electric Vehicles (%) Total EV (BEV+PHEV) penetration (%)  
Source: China Passenger Car Association (CPCA), company data.

## Head of Australia Metals & Mining

Lyndon Fagan AC (61-2) 9003-8648 lyndon.fagan@JPM.com JPM Securities Australia Limited

## Metals & Mining

Jonathon Sharp  
(61 2) 9003-8312  
jonathon.sharp@JPM.com  
JPM Securities Australia Limited

Devwrat Vegad  
(91-22) 6157-3608  
devwrat.vegad@jpmchase.com  
JPM Securities Australia Limited/ JPM India Private Limited

Zane Guo  
(61-3) 9633-4020  
zane.guo@JPM.com  
JPM Securities Australia Limited

Branko Skocic  
(61-3) 9633-4069  
branko.skocic@JPM.com  
JPM Securities Australia Limited

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Figure 3: Battery electric vehicle penetration rates by region  
![](images/fd2c05523d4bc29fb347cec8c19ea4275047c1c51c2b89e9ba2f134bd79ae9f1.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 4: Battery electric vehicle sales – monthly (China + EU + US) '000 units  
![](images/b7565d24340ced17ff922b953ed81c72ed654b56a9fd533559fbdfa66ef86a54.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence. Note: Our China data now references retail sales vs. wholesale sales previously.

Figure 5: Global vehicle sales

<table><tr><td></td><td>Global passenger vehicle sales</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td rowspan="11">China</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>661</td><td>607</td><td>908</td><td>826</td><td>812</td><td>827</td><td>782</td><td>348</td><td>278</td><td>579</td><td>579</td><td>637</td><td>685</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>3,330</td><td>3,937</td><td>4,845</td><td>5,671</td><td>6,483</td><td>7,310</td><td>8,092</td><td>348</td><td>626</td><td>1,205</td><td>1,784</td><td>2,421</td><td>3,106</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>37%</td><td>35%</td><td>39%</td><td>37%</td><td>35%</td><td>31%</td><td>28%</td><td>-19%</td><td>-27%</td><td>-20%</td><td>-13%</td><td>-9%</td><td>-7%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>450</td><td>380</td><td>487</td><td>469</td><td>469</td><td>494</td><td>494</td><td>248</td><td>186</td><td>273</td><td>271</td><td>313</td><td>323</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>921</td><td>839</td><td>557</td><td>946</td><td>1106</td><td>904</td><td>985</td><td>948</td><td>570</td><td>795</td><td>534</td><td>560</td><td>594</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>2032</td><td>1826</td><td>1952</td><td>2241</td><td>2387</td><td>2225</td><td>2261</td><td>1544</td><td>1034</td><td>1647</td><td>1384</td><td>1510</td><td>1602</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>15%</td><td>6%</td><td>2%</td><td>6%</td><td>6%</td><td>-9%</td><td>-14%</td><td>-14%</td><td>-25%</td><td>-15%</td><td>-23%</td><td>-22%</td><td>-21%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>33%</td><td>33%</td><td>47%</td><td>37%</td><td>34%</td><td>37%</td><td>35%</td><td>23%</td><td>27%</td><td>35%</td><td>42%</td><td>42%</td><td>43%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>22%</td><td>21%</td><td>25%</td><td>21%</td><td>20%</td><td>22%</td><td>22%</td><td>16%</td><td>18%</td><td>17%</td><td>20%</td><td>21%</td><td>20%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>55%</td><td>54%</td><td>71%</td><td>58%</td><td>54%</td><td>59%</td><td>56%</td><td>39%</td><td>45%</td><td>52%</td><td>61%</td><td>63%</td><td>63%</td></tr><tr><td>Other Vehicles (%)</td><td>45%</td><td>46%</td><td>29%</td><td>42%</td><td>46%</td><td>41%</td><td>44%</td><td>61%</td><td>55%</td><td>48%</td><td>39%</td><td>37%</td><td>37%</td></tr><tr><td rowspan="11">US</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>101</td><td>130</td><td>149</td><td>147</td><td>72</td><td>69</td><td>87</td><td>66</td><td>71</td><td>84</td><td>78</td><td>86</td><td>73</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>616</td><td>746</td><td>895</td><td>1,042</td><td>1,115</td><td>1,184</td><td>1,271</td><td>66</td><td>136</td><td>220</td><td>298</td><td>385</td><td>458</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>1%</td><td>4%</td><td>7%</td><td>11%</td><td>6%</td><td>1%</td><td>-3%</td><td>-33%</td><td>-30%</td><td>-28%</td><td>-27%</td><td>-25%</td><td>-26%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>21</td><td>24</td><td>30</td><td>25</td><td>12</td><td>13</td><td>14</td><td>10</td><td>11</td><td>13</td><td>15</td><td>19</td><td>18</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>1158</td><td>1252</td><td>1302</td><td>1095</td><td>1200</td><td>1210</td><td>1387</td><td>1039</td><td>1114</td><td>1308</td><td>1287</td><td>1374</td><td>1288</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>1280</td><td>1406</td><td>1480</td><td>1267</td><td>1284</td><td>1292</td><td>1488</td><td>1114</td><td>1196</td><td>1405</td><td>1380</td><td>1480</td><td>1379</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>-4%</td><td>9%</td><td>4%</td><td>7%</td><td>-4%</td><td>-6%</td><td>-2%</td><td>-1%</td><td>-4%</td><td>-11%</td><td>-6%</td><td>0%</td><td>8%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>8%</td><td>9%</td><td>10%</td><td>12%</td><td>6%</td><td>5%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>5%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>10%</td><td>11%</td><td>12%</td><td>14%</td><td>7%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>Other Vehicles (%)</td><td>90%</td><td>89%</td><td>88%</td><td>86%</td><td>93%</td><td>94%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td></tr><tr><td rowspan="11">Europe (EU-10)</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>195</td><td>146</td><td>122</td><td>213</td><td>182</td><td>209</td><td>257</td><td>142</td><td>151</td><td>287</td><td>204</td><td>214</td><td>287</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>953</td><td>1,099</td><td>1,220</td><td>1,434</td><td>1,615</td><td>1,825</td><td>2,081</td><td>142</td><td>293</td><td>581</td><td>784</td><td>999</td><td>1,286</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>22%</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td><td>26%</td><td>29%</td><td>11%</td><td>14%</td><td>27%</td><td>30%</td><td>32%</td><td>35%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>102</td><td>91</td><td>68</td><td>116</td><td>99</td><td>97</td><td>104</td><td>82</td><td>80</td><td>132</td><td>101</td><td>105</td><td>123</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>702</td><td>602</td><td>415</td><td>689</td><td>590</td><td>566</td><td>573</td><td>516</td><td>526</td><td>879</td><td>597</td><td>584</td><td>699</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>999</td><td>839</td><td>605</td><td>1018</td><td>870</td><td>872</td><td>933</td><td>740</td><td>758</td><td>1298</td><td>901</td><td>904</td><td>1110</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>-5%</td><td>2%</td><td>4%</td><td>10%</td><td>5%</td><td>4%</td><td>5%</td><td>-3%</td><td>1%</td><td>11%</td><td>7%</td><td>3%</td><td>11%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>19%</td><td>17%</td><td>20%</td><td>21%</td><td>21%</td><td>24%</td><td>27%</td><td>19%</td><td>20%</td><td>22%</td><td>23%</td><td>24%</td><td>26%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>10%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>10%</td><td>11%</td><td>12%</td><td>11%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>30%</td><td>28%</td><td>31%</td><td>32%</td><td>32%</td><td>35%</td><td>39%</td><td>30%</td><td>31%</td><td>32%</td><td>34%</td><td>35%</td><td>37%</td></tr><tr><td>Other Vehicles (%)</td><td>70%</td><td>72%</td><td>69%</td><td>68%</td><td>68%</td><td>65%</td><td>61%</td><td>70%</td><td>69%</td><td>68%</td><td>66%</td><td>65%</td><td>63%</td></tr><tr><td rowspan="17">Total</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>956</td><td>883</td><td>1178</td><td>1187</td><td>1066</td><td>1105</td><td>1125</td><td>556</td><td>500</td><td>950</td><td>861</td><td>938</td><td>1045</td></tr><tr><td>Battery Electric Vehicles (m units) - YTD</td><td>4,899</td><td>5,782</td><td>6,960</td><td>8,147</td><td>9,213</td><td>10,318</td><td>11,444</td><td>556</td><td>1,056</td><td>2,006</td><td>2,867</td><td>3,805</td><td>4,850</td></tr><tr><td>BEV sales, YTD/YTD</td><td>28%</td><td>28%</td><td>31%</td><td>30%</td><td>29%</td><td>26%</td><td>24%</td><td>-15%</td><td>-19%</td><td>-12%</td><td>-7%</td><td>-3%</td><td>-1%</td></tr><tr><td>BEV growth YoY - China</td><td>34%</td><td>26%</td><td>56%</td><td>28%</td><td>21%</td><td>9%</td><td>3%</td><td>-19%</td><td>-35%</td><td>-10%</td><td>4%</td><td>5%</td><td>4%</td></tr><tr><td>BEV growth YoY - US</td><td>-6%</td><td>18%</td><td>22%</td><td>43%</td><td>-32%</td><td>-42%</td><td>-36%</td><td>-33%</td><td>-28%</td><td>-25%</td><td>-23%</td><td>-18%</td><td>-28%</td></tr><tr><td>BEV growth YoY - EU</td><td>14%</td><td>33%</td><td>25%</td><td>20%</td><td>35%</td><td>42%</td><td>56%</td><td>11%</td><td>18%</td><td>44%</td><td>38%</td><td>39%</td><td>48%</td></tr><tr><td>BEV growth YoY - Total</td><td>24%</td><td>26%</td><td>47%</td><td>28%</td><td>17%</td><td>8%</td><td>6%</td><td>-15%</td><td>-23%</td><td>-1%</td><td>7%</td><td>8%</td><td>9%</td></tr><tr><td>BEV growth MoM - Total</td><td>10%</td><td>-8%</td><td>33%</td><td>1%</td><td>-10%</td><td>4%</td><td>2%</td><td>-51%</td><td>-10%</td><td>90%</td><td>-9%</td><td>9%</td><td>11%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>573</td><td>495</td><td>585</td><td>609</td><td>580</td><td>604</td><td>612</td><td>340</td><td>277</td><td>419</td><td>387</td><td>437</td><td>464</td></tr><tr><td>Growth YoY</td><td>25%</td><td>4%</td><td>14%</td><td>7%</td><td>-6%</td><td>-2%</td><td>-6%</td><td>-15%</td><td>-20%</td><td>-14%</td><td>-16%</td><td>-18%</td><td>-19%</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>2,781</td><td>2,693</td><td>2,274</td><td>2,730</td><td>2,896</td><td>2,680</td><td>2,945</td><td>2,503</td><td>2,210</td><td>2,982</td><td>2,417</td><td>2,518</td><td>2,581</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>4,310</td><td>4,071</td><td>4,037</td><td>4,526</td><td>4,541</td><td>4,389</td><td>4,683</td><td>3,398</td><td>2,987</td><td>4,351</td><td>3,665</td><td>3,893</td><td>4,091</td></tr><tr><td>Total passenger vehicles (Growth YoY)</td><td>4%</td><td>6%</td><td>3%</td><td>7%</td><td>3%</td><td>-6%</td><td>-7%</td><td>-8%</td><td>-12%</td><td>-7%</td><td>-11%</td><td>-9%</td><td>-5%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>22%</td><td>22%</td><td>29%</td><td>26%</td><td>23%</td><td>25%</td><td>24%</td><td>16%</td><td>17%</td><td>22%</td><td>23%</td><td>24%</td><td>26%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>13%</td><td>12%</td><td>14%</td><td>13%</td><td>13%</td><td>14%</td><td>13%</td><td>10%</td><td>9%</td><td>10%</td><td>11%</td><td>11%</td><td>11%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>35%</td><td>34%</td><td>44%</td><td>40%</td><td>36%</td><td>39%</td><td>37%</td><td>26%</td><td>26%</td><td>31%</td><td>34%</td><td>35%</td><td>37%</td></tr><tr><td>Other Vehicles (%)</td><td>65%</td><td>66%</td><td>56%</td><td>60%</td><td>64%</td><td>61%</td><td>63%</td><td>74%</td><td>74%</td><td>69%</td><td>66%</td><td>65%</td><td>63%</td></tr></table>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence. Note: Our China data now references retail sales vs. wholesale sales previously.

Figure 6: Total vehicle sales – Global '000 units

## Global

![](images/9fa30fcdeb436024fe979b6dec029463ac536046055c7201ad1dfd1343dbac01.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 7: Battery electric vehicle sales – Global  
![](images/f8a93ca67f06b67f85f692810d0c90cd92eef0882d91b64ec86ecfc4e3110b22.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

## China

![](images/98e257df12b4fe1b22967b46f2c36dccf7878493f0c4ef79c049d0fa30750300.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 9: Battery electric vehicle sales – China  
![](images/c163ba0c1eff86755d489d96abd69b7a721cc530cf819dbba5e63b086f153333.jpg)  
Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

US  
![](images/4f4e48646aaf279e8da53aefb50486add3875607a7ebadb9de21df75f156d518.jpg)  
Source: Company data, Motor Intelligence.

Figure 11: Battery electric vehicle sales – US  
![](images/ffbe34b8bfca7fedf995bb3ea5093809b8b0ac50ced59a7511e5cb839c45c0bc.jpg)  
Source: Company data, Motor Intelligence.

## EU-10 (France, Germany, UK, Austria, Norway, Sweden, Switzerland, Italy, Spain, Netherlands)

Figure 12: Total vehicle sales – EU  
![](images/a4113851f3b6990d804a2433d55ed141c671c28a6be5658bf2b238b69d07791a.jpg)  
Source: Company data, Motor Intelligence.

Figure 13: Battery electric vehicle sales – EU  
![](images/2e69de3f563cd2493b45b89aac471c657ad34e562481d32fd4c6fb06bc38f5dd.jpg)  
Source: Company data, Motor Intelligence.

Figure 14: Lithium spodumene prices  
![](images/3ded23f75d8bf2982b1357382e368f6565c4fa11e46c74249ea1fd8b439f18cc.jpg)  
Spodumene FOB Australi

[中间内容因长度限制已省略]

involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Completed 13 Jul 2026 02:38 PM AEST
"""
