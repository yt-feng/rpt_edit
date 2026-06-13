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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
| Jul | 3750 | 3950 | 3950 | 4100 | - |
| Aug | 3650 | 4000 | 4000 | 4100 | - |
| Sep | 3950 | 4350 | 4350 | 4500 | - |
| Oct | 3850 | 4150 | 4450 | 4550 | - |
| Nov | 3650 | 4250 | 4650 | 4450 | - |
| Dec | 4450 | 4650 | 5100 | 4750 | - |
</details>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 7: Battery electric vehicle sales – Global  
![](images/f62c85fb495e174b6854aed5dd0aa9820d617b27f83059eb1844f4e6a52938b4.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 (units) | 2023 (units) | 2024 (units) | 2025 (units) | 2026 (units) |
|---|---|---|---|---|---|
| Jan | 380 | 390 | 550 | 670 | 560 |
| Feb | 340 | 450 | 470 | 660 | 510 |
| Mar | 580 | 680 | 700 | 980 | 960 |
| Apr | 360 | 570 | 620 | 850 | 870 |
| May | 430 | 630 | 750 | 940 | 950 |
| Jun | 630 | 750 | 770 | 970 | - |
| Jul | 510 | 660 | 710 | 880 | - |
| Aug | 550 | 770 | 810 | 1190 | - |
| Sep | 680 | 760 | 930 | 1190 | - |
| Oct | 340 | 730 | 910 | 1070 | - |
| Nov | 670 | 810 | 1030 | 1120 | - |
| Dec | 810 | 890 | 1060 | 1140 | - |
</details>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

## China

Figure 8: Total vehicle sales – China  
![](images/ff033300ded2798ce93a34737d396b237bd9a6e32550528ad7a3a2e27aa4f186.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 (units) | 2023 (units) | 2024 (units) | 2025 (units) | 2026 (units) |
|---|---|---|---|---|---|
| Jan | 2100 | 1250 | 1900 | 1800 | 1550 |
| Feb | 1250 | 1300 | 1350 | 1350 | 1100 |
| Mar | 1700 | 1550 | 1650 | 1850 | 1700 |
| Apr | 1100 | 1600 | 1550 | 1800 | 1350 |
| May | 1400 | 1750 | 1700 | 1900 | 1500 |
| Jun | 1900 | 1850 | 1750 | 1950 | - |
| Jul | 1800 | 1800 | 1750 | 1850 | - |
| Aug | 1850 | 1850 | 1850 | 1900 | - |
| Sep | 1900 | 1950 | 2000 | 2150 | - |
| Oct | 1850 | 2000 | 2150 | 2400 | - |
| Nov | 1750 | 2100 | 2350 | 2350 | - |
| Dec | 2150 | 2400 | 2700 | 2350 | - |
</details>

Source: China Passenger Car Association (CPCA), company data, Motor Intelligence.

Figure 9: Battery electric vehicle sales – China  
![](images/3e4c14813eae9e08e801acc0f1efa94a88d27dafbae691b54f1aee11e84ee8e0.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 (units) | 2023 (units) | 2024 (units) | 2025 (units) | 2026 (units) |
|---|---|---|---|---|---|
| Jan | 280 | 210 | 370 | 430 | 360 |
| Feb | 210 | 230 | 290 | 430 | 290 |
| Mar | 370 | 380 | 430 | 650 | 580 |
| Apr | 210 | 360 | 410 | 570 | 590 |
| May | 280 | 390 | 490 | 610 | 640 |
| Jun | 430 | 440 | 480 | 660 | - |
| Jul | 360 | 420 | 480 | 610 | - |
| Aug | 390 | 480 | 570 | 920 | - |
| Sep | 460 | 490 | 640 | 830 | - |
| Oct | 160 | 490 | 680 | 810 | - |
| Nov | 440 | 550 | 760 | 830 | - |
| Dec | 460 | 610 | 770 | 790 | - |
</details>

Source: China Passenger Car Association (CPCA), company dat

[中间内容因长度限制已省略]

tes may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jun 2026 11:07 AM AEST

Disseminated 12 Jun 2026 11:07 AM AEST
"""
