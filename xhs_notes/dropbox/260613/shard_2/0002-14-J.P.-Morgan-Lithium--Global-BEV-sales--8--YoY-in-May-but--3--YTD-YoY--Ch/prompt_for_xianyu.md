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
## Lithium

## Global BEV sales +8% YoY in May but -3% YTD YoY; China BEV penetration remains at 42%

Key takeaways from the May EV sales data: (1) Global BEV sales (China + EU + US) rose 9% MoM to 938k units and are up 8% YoY but YTD remain down 3% vs 2025; global BEV penetration stood at 24% in May (vs 23% in Apr'26). (2) China BEV penetration remained elevated at 42% in May, with BEV sales rising 10% MoM to 637k units and total EV (BEV+PHEV) penetration reaching 63%, the highest since August 2025. (3) US BEV sales rebounded 10% MoM to 86k units but are still down 25% YTD YoY; BEV penetration continued to stand at 6%. (4) EU-10 BEV sales increased 5% MoM to 214kt and remain up 32% YTD YoY; BEV penetration increased to 32% (from 24% in April). The EU remains the strongest region on country-level subsidy schemes and affordable mass EVs penetrating the market. With the continued strength in the ESS market and the supply time lag, we see modest upward pressure in spodumene prices from here. Our top pick in the lithium space is PLS. For more information on EV/PHEV sales, please see JPM's Asia Battery/Autos research teams' latest note here.

Figure 1: China vehicle sales vs. BEV sales  
![](images/751f0e57eb10582294ad965c44c5f1e784fc08a326d8bd4dc695100c02a3ee8e.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Total passenger vehicle sales ('000 units) | Battery Electric Vehicles ('000 units) - RHS |
|---|---|---|
| May-25 | 1932 | 687 |
| Jun-25 | 2032 | 744 |
| Jul-25 | 1826 | 687 |
| Aug-25 | 1952 | 884 |
| Sep-25 | 2241 | 844 |
| Oct-25 | 2387 | 844 |
| Nov-25 | 2225 | 844 |
| Dec-25 | 2261 | 800 |
| Jan-26 | 1544 | 360 |
| Feb-26 | 1034 | 300 |
| Mar-26 | 1647 | 580 |
| Apr-26 | 1384 | 580 |
| May-26 | 1510 | 640 |
</details>

Source: China Passenger Car Association (CPCA), company data. Note: Our China data now references retail sales vs. wholesale sales previously.

Figure 2: China EV penetration rates  
![](images/d55802fff1f873d98f15b5d00e817d2aeff24079f72ffbd72b34cf9df0388726.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Battery Electric Vehicles (%) | Plug-in Hybrid Electric Vehicles (%) | Total EV (BEV+PHEV) penetration (%) |
|---|---|---|---|
| May-25 | 31 | 21 | 53 |
| Jul-25 | 33 | 22 | 55 |
| Sep-25 | 37 | 21 | 58 |
| Nov-25 | 34 | 20 | 54 |
| Jan-26 | 23 | 16 | 39 |
| Mar-26 | 35 | 17 | 52 |
| May-26 | 42 | 20 | 61 |
| Jun-26 | 42 | 21 | 63 |
</details>

Source: China Passenger Car Association (CPCA), company data.

## Head of Australia Metals & Mining

Lyndon Fagan AC

(61-2) 9003-8648

lyndon.fagan@JPM.com

JPM Securities Australia Limited

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

Figure 3: Battery electric vehicle penetration rates by region  
![](images/30016de1292c2daef2a3f597d5df11c139c9f996259a934882c5fb045b1c3b17.jpg)

<details>
<summary>bar chart</summary>

| Month | China BEV penetration (%) | EU BEV penetration (%) | US BEV penetration (%) |
|---|---|---|---|
| Dec-25 | 35 | 27 | 6 |
| Jan-26 | 23 | 19 | 6 |
| Feb-26 | 27 | 20 | 6 |
| Mar-26 | 35 | 22 | 6 |
| Apr-26 | 42 | 23 | 6 |
| May-26 | 42 | 24 | 6 |
</details>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 4: Battery electric vehicle sales – monthly (China + EU + US)  
![](images/7ac5905da01982e066981b28a41f7d6520fc285f84ad4b4f9d4a57a95343a6d9.jpg)

<details>
<summary>line chart</summary>

| Date | Value ('000 units) |
|---|---|
| May-25 | 870 |
| Jun-25 | 950 |
| Jul-25 | 870 |
| Aug-25 | 1180 |
| Sep-25 | 1187 |
| Oct-25 | 1050 |
| Nov-25 | 1110 |
| Dec-25 | 1130 |
| Jan-26 | 540 |
| Feb-26 | 490 |
| Mar-26 | 950 |
| Apr-26 | 860 |
| May-26 | 940 |
</details>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.  
Note: Our China data now references retail sales vs. wholesale sales previously.

Figure 5: Global vehicle sales

<table><tr><td></td><td>Global passenger vehicle sales</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td rowspan="11">China</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>607</td><td>661</td><td>607</td><td>908</td><td>826</td><td>812</td><td>827</td><td>782</td><td>348</td><td>278</td><td>579</td><td>579</td><td>637</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>2,669</td><td>3,330</td><td>3,937</td><td>4,845</td><td>5,671</td><td>6,483</td><td>7,310</td><td>8,092</td><td>348</td><td>626</td><td>1,205</td><td>1,784</td><td>2,421</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>38%</td><td>37%</td><td>35%</td><td>39%</td><td>37%</td><td>35%</td><td>31%</td><td>28%</td><td>-19%</td><td>-27%</td><td>-20%</td><td>-13%</td><td>-9%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>414</td><td>450</td><td>380</td><td>487</td><td>469</td><td>469</td><td>494</td><td>494</td><td>248</td><td>186</td><td>273</td><td>271</td><td>313</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>911</td><td>921</td><td>839</td><td>557</td><td>946</td><td>1106</td><td>904</td><td>985</td><td>948</td><td>570</td><td>795</td><td>534</td><td>560</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>1932</td><td>2032</td><td>1826</td><td>1952</td><td>2241</td><td>2387</td><td>2225</td><td>2261</td><td>1544</td><td>1034</td><td>1647</td><td>1384</td><td>1510</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>15%</td><td>15%</td><td>6%</td><td>2%</td><td>6%</td><td>6%</td><td>-9%</td><td>-14%</td><td>-14%</td><td>-25%</td><td>-15%</td><td>-23%</td><td>-22%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>31%</td><td>33%</td><td>33%</td><td>47%</td><td>37%</td><td>34%</td><td>37%</td><td>35%</td><td>23%</td><td>27%</td><td>35%</td><td>42%</td><td>42%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>21%</td><td>22%</td><td>21%</td><td>25%</td><td>21%</td><td>20%</td><td>22%</td><td>22%</td><td>16%</td><td>18%</td><td>17%</td><td>20%</td><td>21%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>53%</td><td>55%</td><td>54%</td><td>71%</td><td>58%</td><td>54%</td><td>59%</td><td>56%</td><td>39%</td><td>45%</td><td>52%</td><td>61%</td><td>63%</td></tr><tr><td>Other Vehicles (%)</td><td>47%</td><td>45%</td><td>46%</td><td>29%</td><td>42%</td><td>46%</td><td>41%</td><td>44%</td><td>61%</td><td>55%</td><td>48%</td><td>39%</td><td>37%</td></tr><tr><td rowspan="11">US</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>106</td><td>101</td><td>130</td><td>149</td><td>147</td><td>72</td><td>69</td><td>87</td><td>66</td><td>71</td><td>84</td><td>78</td><td>86</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>515</td><td>616</td><td>746</td><td>895</td><td>1,042</td><td>1,115</td><td>1,184</td><td>1,271</td><td>66</td><td>136</td><td>220</td><td>298</td><td>385</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>3%</td><td>1%</td><td>4%</td><td>7%</td><td>11%</td><td>6%</td><td>1%</td><td>-3%</td><td>-33%</td><td>-30%</td><td>-28%</td><td>-27%</td><td>-25%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>28</td><td>21</td><td>24</td><td>30</td><td>25</td><td>12</td><td>13</td><td>14</td><td>10</td><td>11</td><td>13</td><td>15</td><td>19</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>1341</td><td>1158</td><td>1252</td><td>1302</td><td>1095</td><td>1200</td><td>1210</td><td>1387</td><td>1039</td><td>1114</td><td>1308</td><td>1287</td><td>1374</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>1475</td><td>1280</td><td>1406</td><td>1480</td><td>1267</td><td>1284</td><td>1292</td><td>1488</td><td>1114</td><td>1196</td><td>1405</td><td>1380</td><td>1480</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>2%</td><td>-4%</td><td>9%</td><td>4%</td><td>7%</td><td>-4%</td><td>-6%</td><td>-2%</td><td>-1%</td><td>-4%</td><td>-11%</td><td>-6%</td><td>0%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>7%</td><td>8%</td><td>9%</td><td>10%</td><td>12%</td><td>6%</td><td>5%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>9%</td><td>10%</td><td>11%</td><td>12%</td><td>14%</td><td>7%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>Other Vehicles (%)</td><td>91%</td><td>90%</td><td>89%</td><td>88%</td><td>86%</td><td>93%</td><td>94%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td><td>93%</td></tr><tr><td rowspan="11">Europe (EU-10)</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>154</td><td>195</td><td>146</td><td>122</td><td>213</td><td>182</td><td>209</td><td>257</td><td>142</td><td>151</td><td>287</td><td>204</td><td>214</td></tr><tr><td>Total BEV sales (&#x27;000 units) - YTD</td><td>758</td><td>953</td><td>1,099</td><td>1,220</td><td>1,434</td><td>1,615</td><td>1,825</td><td>2,081</td><td>142</td><td>293</td><td>581</td><td>784</td><td>999</td></tr><tr><td>Total BEV sales (Growth YTD YoY)</td><td>24%</td><td>22%</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td><td>26%</td><td>29%</td><td>11%</td><td>14%</td><td>27%</td><td>30%</td><td>32%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>89</td><td>102</td><td>91</td><td>68</td><td>116</td><td>99</td><td>97</td><td>104</td><td>82</td><td>80</td><td>132</td><td>101</td><td>105</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>636</td><td>702</td><td>602</td><td>415</td><td>689</td><td>590</td><td>566</td><td>573</td><td>516</td><td>526</td><td>879</td><td>597</td><td>584</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>880</td><td>999</td><td>839</td><td>605</td><td>1018</td><td>870</td><td>872</td><td>933</td><td>740</td><td>758</td><td>1298</td><td>901</td><td>904</td></tr><tr><td>Total vehicle sales (Growth YoY)</td><td>-1%</td><td>-5%</td><td>2%</td><td>4%</td><td>10%</td><td>5%</td><td>4%</td><td>5%</td><td>-3%</td><td>1%</td><td>11%</td><td>7%</td><td>3%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>18%</td><td>19%</td><td>17%</td><td>20%</td><td>21%</td><td>21%</td><td>24%</td><td>27%</td><td>19%</td><td>20%</td><td>22%</td><td>23%</td><td>24%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>10%</td><td>10%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>10%</td><td>11%</td><td>12%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>28%</td><td>30%</td><td>28%</td><td>31%</td><td>32%</td><td>32%</td><td>35%</td><td>39%</td><td>30%</td><td>31%</td><td>32%</td><td>34%</td><td>35%</td></tr><tr><td>Other Vehicles (%)</td><td>72%</td><td>70%</td><td>72%</td><td>69%</td><td>68%</td><td>68%</td><td>65%</td><td>61%</td><td>70%</td><td>69%</td><td>68%</td><td>66%</td><td>65%</td></tr><tr><td rowspan="17">Total</td><td>Battery Electric Vehicles (&#x27;000 units)</td><td>867</td><td>956</td><td>883</td><td>1178</td><td>1187</td><td>1066</td><td>1105</td><td>1125</td><td>556</td><td>500</td><td>950</td><td>861</td><td>938</td></tr><tr><td>Battery Electric Vehicles (m units) - YTD</td><td>3,943</td><td>4,899</td><td>5,782</td><td>6,960</td><td>8,147</td><td>9,213</td><td>10,318</td><td>11,444</td><td>556</td><td>1,056</td><td>2,006</td><td>2,867</td><td>3,805</td></tr><tr><td>BEV sales, YTD/YTD</td><td>29%</td><td>28%</td><td>28%</td><td>31%</td><td>30%</td><td>29%</td><td>26%</td><td>24%</td><td>-15%</td><td>-19%</td><td>-12%</td><td>-7%</td><td>-3%</td></tr><tr><td>BEV growth YoY - China</td><td>23%</td><td>34%</td><td>26%</td><td>56%</td><td>28%</td><td>21%</td><td>9%</td><td>3%</td><td>-19%</td><td>-35%</td><td>-10%</td><td>4%</td><td>5%</td></tr><tr><td>BEV growth YoY - US</td><td>-4%</td><td>-6%</td><td>18%</td><td>22%</td><td>43%</td><td>-32%</td><td>-42%</td><td>-36%</td><td>-33%</td><td>-28%</td><td>-25%</td><td>-23%</td><td>-18%</td></tr><tr><td>BEV growth YoY - EU</td><td>14%</td><td>14%</td><td>33%</td><td>25%</td><td>20%</td><td>35%</td><td>42%</td><td>56%</td><td>11%</td><td>18%</td><td>44%</td><td>38%</td><td>39%</td></tr><tr><td>BEV growth YoY - Total</td><td>17%</td><td>24%</td><td>26%</td><td>47%</td><td>28%</td><td>17%</td><td>8%</td><td>6%</td><td>-15%</td><td>-23%</td><td>-1%</td><td>7%</td><td>8%</td></tr><tr><td>BEV growth MoM - Total</td><td>7%</td><td>10%</td><td>-8%</td><td>33%</td><td>1%</td><td>-10%</td><td>4%</td><td>2%</td><td>-51%</td><td>-10%</td><td>90%</td><td>-9%</td><td>9%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (&#x27;000 units)</td><td>531</td><td>573</td><td>495</td><td>585</td><td>609</td><td>580</td><td>604</td><td>612</td><td>340</td><td>277</td><td>419</td><td>387</td><td>437</td></tr><tr><td>Growth YoY</td><td>33%</td><td>25%</td><td>4%</td><td>14%</td><td>7%</td><td>-6%</td><td>-2%</td><td>-6%</td><td>-15%</td><td>-20%</td><td>-14%</td><td>-16%</td><td>-18%</td></tr><tr><td>Other Vehicles (&#x27;000 units)</td><td>2,889</td><td>2,781</td><td>2,693</td><td>2,274</td><td>2,730</td><td>2,896</td><td>2,680</td><td>2,945</td><td>2,503</td><td>2,210</td><td>2,982</td><td>2,417</td><td>2,518</td></tr><tr><td>Total passenger vehicle sales (&#x27;000 units)</td><td>4,287</td><td>4,310</td><td>4,071</td><td>4,037</td><td>4,526</td><td>4,541</td><td>4,389</td><td>4,683</td><td>3,398</td><td>2,987</td><td>4,351</td><td>3,665</td><td>3,893</td></tr><tr><td>Total passenger vehicles (Growth YoY)</td><td>7%</td><td>4%</td><td>6%</td><td>3%</td><td>7%</td><td>3%</td><td>-6%</td><td>-7%</td><td>-8%</td><td>-12%</td><td>-7%</td><td>-11%</td><td>-9%</td></tr><tr><td>Battery Electric Vehicles (%)</td><td>20%</td><td>22%</td><td>22%</td><td>29%</td><td>26%</td><td>23%</td><td>25%</td><td>24%</td><td>16%</td><td>17%</td><td>22%</td><td>23%</td><td>24%</td></tr><tr><td>Plug-in Hybrid Electric Vehicles (%)</td><td>12%</td><td>13%</td><td>12%</td><td>14%</td><td>13%</td><td>13%</td><td>14%</td><td>13%</td><td>10%</td><td>9%</td><td>10%</td><td>11%</td><td>11%</td></tr><tr><td>Total EV (BEV+PHEV) penetration (%)</td><td>33%</td><td>35%</td><td>34%</td><td>44%</td><td>40%</td><td>36%</td><td>39%</td><td>37%</td><td>26%</td><td>26%</td><td>31%</td><td>34%</td><td>35%</td></tr><tr><td>Other Vehicles (%)</td><td>67%</td><td>65%</td><td>66%</td><td>56%</td><td>60%</td><td>64%</td><td>61%</td><td>63%</td><td>74%</td><td>74%</td><td>69%</td><td>66%</td><td>65%</td></tr></table>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.  
Note: Our China data now references retail sales vs. wholesale sales previously.

## Global

Figure 6: Total vehicle sales – Global  
![](images/8153a7d90c666a19d1d7350d148cdd3a1c26e4fd467787d85fa1ec5093256605.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 (units) | 2023 (units) | 2024 (units) | 2025 (units) | 2026 (units) |
|---|---|---|---|---|---|
| Jan | 3800 | 3100 | 3950 | 3750 | 3400 |
| Feb | 3000 | 3300 | 3350 | 3450 | 3000 |
| Mar | 3800 | 4150 | 4250 | 4700 | 4400 |
| Apr | 3000 | 3750 | 3750 | 4100 | 3700 |
| May | 3300 | 4150 | 4150 | 4350 | 3950 |
| Jun | 4050 | 4350 | 4250 | 4350 | - |
| Jul | 3750 | 3950 | 3950

[中间内容因长度限制已省略]

nce is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jun 2026 11:07 AM AEST

Disseminated 12 Jun 2026 11:07 AM AEST
"""
