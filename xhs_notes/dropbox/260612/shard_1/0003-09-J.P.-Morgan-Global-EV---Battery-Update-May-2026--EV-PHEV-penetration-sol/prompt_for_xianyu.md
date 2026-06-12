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
# Global EV & Battery Update

May 2026: EV/PHEV penetration solid in EU/China vs US weak; ESS remains the clear bright spot

EV+PHEV penetration trends by region. May EU-5+US+China EV/PHEV momentum remained resilient, with sales at 1.3mn units (-2% y/y, +10% m/m) and penetration at 35% (+3%ppts y/y, +1%ppt m/m). EU-5 continued to drive penetration gains, China's penetration rose despite weak PV sales, while the US remained soft.

- EU-5. May EV/PHEV sales volume grew 39% y/y and penetration reached 32% (+8%pts y/y, +1%pts m/m) with strength across all regions. EU-5 penetration continues to rise: France (+13%pts), followed by Italy (+9%pts), Germany (+8%pts), UK (+7%pts), Spain (+4%pts), supported by country-level subsidy schemes and affordable mass EVs penetrating the market. This week, the EU introduced a €1.5bn Battery Booster Facility to support EV battery production within the European Economic Area, with the first awards expected before the end-2026 (link).  
- US. May EV/PHEV sales volume fell 21% y/y with penetration at 7% (-2%pts y/y, flat m/m), continuing to print y/y declines. By OEM, M/S remained broadly muted m/m: Tesla (#1) followed by GM (#2), HMG (#3), Toyota (#4) and Ford (#5). EV demand stayed weak (-18% y/y, +10% m/m) at \~6% penetration, likely reflecting fewer consumer choices as OEMs cancel new EV launches and pull back marketing.  
- China. CPCA May NEV retail sales volume came in at 0.95mn units (-7% y/y, +12% m/m), with collective penetration at 63% (+10%pts y/y, +1%pts m/m) out of a total of 1.5mn PV sales. While overall PV sales continue to fall, NEV sales held relatively better. Our China auto team is turning more cautious on domestic demand, revising 2026 retail forecasts from -4% to -15% y/y. NEVs are holding up relatively well with penetration exceeding 60%; NEV mix and overseas exposure are becoming more important earnings drivers than headline industry growth (link).

EV index performance. Over the past month, Asian EV supply chain stocks have traded soft, with Korea (-19%) and China (-13%) underperforming while Japan outperformed (+17%). By subsector, cathodes (-19%) lagged the most, followed by anodes (-17%), separators (-9%), cell makers (-4%) and battery foil (-1%), while electrolytes relatively outperformed (+1%).

AIDC ESS momentum is building, with Siemens partnering with NVIDIA and Fluence Energy to develop a reference power-and-controls architecture for AIDCs, while Fluence has signed Master Supply Agreements with two hyperscalers with first orders expected in 3Q. We believe these developments should alleviate market concerns on whether AIDCs need ESS and drive rising expectations for AIDC ESS demand into 2026-27. Adoption appears slow on the surface, but we believe this is due to construction sequencing rather than a lack of demand, as ESS installation occurs in the later stages of AIDC builds and most large-scale projects are still in early construction phases. AIDC ESS battery is a distinct product category from utility-scale ESS, requiring rapid response, high power density and frequent micro-cycling, which favours leading players with strong product quality (link).

## Korean Autos

## Sonny Lee AC

(82-2) 758 5716

sonny.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

## Seri Yoon

(82-2) 758 5704

seri.yoon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

## Asia Autos & EV Battery

## Rebecca Wen

(852) 2800-8505

rebecca.y.wen@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Asia Energy & Chemicals / EV Battery

## Parsley Ong

(65) 6882-8578

parsley.rh.ong@JPM.com

JPM Securities Singapore Private Limited/
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## European Autos

## Jose M Asumendi

(44-20) 7742-5315

jose.m.asumendi@JPM.com

JPM Securities plc

Chinese OEMs' overseas expansion appears structural. Our China auto team raised 2026 overseas sales forecasts for BYD/Geely by \~15%/\~30%, while trimming domestic estimates after visiting Europe. The key takeaway from our European Auto Conference last week is that Chinese OEMs' overseas strategy has evolved beyond a single-powertrain, cheap EV narrative into balanced powertrain portfolios, brand ladders and tech stories. Chinese OEMs' M/S in Europe NEV reached 18%, tripling y/y, driven by retail execution moats and strong feature content bundled as standard, with localization accelerating to mitigate tariff and regulatory risks (link).

Downgrade SQM (SQM US, N, covered by Lucas Ferreira) to Neutral as upside to lithium prices from current spot levels appears limited. The global lithium S/D balance still points to a deficit over the next couple of years, but several near-term headwinds are emerging, including a rebound in Chinese lithium inventories, pushback from battery players on elevated price levels, and a more cautious stance on Chinese EV sales with Chinese NEV sales falling y/y entering 2026. Offsetting this, ESS demand remains strong and some lithium project delays in China are keeping the market tight, but not enough to drive meaningful upside (link).

Stock recommendations and potential future catalysts. Europe continues to print strong EV growth, China's penetration is rising despite soft PV sales, while the US remains soft. ESS remains a clear bright spot with global shipments more than doubling y/y in 4M26, driven by China domestic demand and robust exports to ex-US regions. US-bound shipments are shifting from China to Korean/Japanese battery makers, underscoring the ongoing sourcing shift as OBBBA regulations remain in effect (link). Among ESS players, we favor CATL as the largest global ESS battery maker, and LGES/SDI as key beneficiaries of growing US ESS opportunities.

Stock positioning. In Korea, we like auto OEMs (Hyundai Motor, Kia) on resilient auto earnings driven by increasing HEV mix. Within the Korea battery supply chain, we prefer battery makers (LGES/SDI OW) over materials (LG Chem/L&F OW; EBM N; PFM UW) and lithium producers (POSCO, N), reflecting relative bargaining power and execution capability (LGES, LG Chem covered by Parsley Ong). In China, we like BYD-A/H (covered by Nick Lai) for its strong execution on global expansion along with overseas production ramp-up; and CATL-A/H (covered by Rebecca Wen) given its technology and leadership position in the global EV and ESS battery market.

Table 1: May 2026 PV+EV+PHEV monthly and YTD sales and penetration trends (by region)  
Units in 000s, %, %p

<table><tr><td>Global PV Sales (&#x27;000s)</td><td>May-26</td><td>May-25</td><td>y/y%</td><td>5M26</td><td>5M25</td><td>y/y%</td></tr><tr><td colspan="7">Passenger Vehicles (PV)</td></tr><tr><td>Europe (EU5)</td><td>791</td><td>765</td><td>3.3%</td><td>4,092</td><td>3,883</td><td>5.4%</td></tr><tr><td>Germany</td><td>239</td><td>239</td><td>0.1%</td><td>1,188</td><td>1,147</td><td>3.6%</td></tr><tr><td>France</td><td>128</td><td>124</td><td>3.7%</td><td>668</td><td>673</td><td>-0.6%</td></tr><tr><td>Italy</td><td>150</td><td>139</td><td>7.7%</td><td>792</td><td>722</td><td>9.6%</td></tr><tr><td>Spain</td><td>112</td><td>113</td><td>-0.8%</td><td>519</td><td>491</td><td>5.8%</td></tr><tr><td>United Kingdom</td><td>161</td><td>150</td><td>7.1%</td><td>925</td><td>851</td><td>8.7%</td></tr><tr><td>China</td><td>1,510</td><td>1,938</td><td>-22.1%</td><td>7,119</td><td>8,810</td><td>-19.2%</td></tr><tr><td>US</td><td>1,480</td><td>1,475</td><td>0.3%</td><td>6,575</td><td>6,901</td><td>-4.7%</td></tr><tr><td>Total</td><td>3,780</td><td>4,179</td><td>-9.5%</td><td>17,786</td><td>19,595</td><td>-9.2%</td></tr><tr><td colspan="7"></td></tr><tr><td colspan="7">Battery Electric Vehicles (EV)</td></tr><tr><td>Europe (EU5)</td><td>167</td><td>111</td><td>49.7%</td><td>804</td><td>570</td><td>40.9%</td></tr><tr><td>Germany</td><td>60</td><td>43</td><td>39.3%</td><td>284</td><td>202</td><td>40.9%</td></tr><tr><td>France</td><td>37</td><td>19</td><td>92.7%</td><td>186</td><td>119</td><td>55.4%</td></tr><tr><td>Italy</td><td>13</td><td>7</td><td>85.8%</td><td>65</td><td>37</td><td>75.5%</td></tr><tr><td>Spain</td><td>12</td><td>9</td><td>34.4%</td><td>49</td><td>35</td><td>39.9%</td></tr><tr><td>United Kingdom</td><td>44</td><td>33</td><td>34.2%</td><td>221</td><td>177</td><td>24.3%</td></tr><tr><td>China</td><td>637</td><td>607</td><td>4.9%</td><td>2,421</td><td>2,675</td><td>-9.5%</td></tr><tr><td>US</td><td>86</td><td>106</td><td>-18.3%</td><td>385</td><td>515</td><td>-25.3%</td></tr><tr><td>Total</td><td>890</td><td>824</td><td>8.0%</td><td>3,610</td><td>3,761</td><td>-4.0%</td></tr><tr><td colspan="7"></td></tr><tr><td colspan="7">Plug-in Hybrid Vehicles (PHEV)</td></tr><tr><td>Europe (EU5)</td><td>87</td><td>71</td><td>22.0%</td><td>414</td><td>312</td><td>32.6%</td></tr><tr><td>Germany</td><td>28</td><td>25</td><td>10.9%</td><td>132</td><td>113</td><td>16.0%</td></tr><tr><td>France</td><td>8</td><td>8</td><td>-6.5%</td><td>29</td><td>37</td><td>-21.7%</td></tr><tr><td>Italy</td><td>15</td><td>7</td><td>122.0%</td><td>69</td><td>33</td><td>108.4%</td></tr><tr><td>Spain</td><td>14</td><td>13</td><td>6.6%</td><td>62</td><td>43</td><td>46.9%</td></tr><tr><td>United Kingdom</td><td>22</td><td>18</td><td>23.9%</td><td>121</td><td>86</td><td>41.8%</td></tr><tr><td>China</td><td>313</td><td>414</td><td>-24.4%</td><td>1,291</td><td>1,678</td><td>-23.1%</td></tr><tr><td>US</td><td>19</td><td>28</td><td>-32.5%</td><td>68</td><td>154</td><td>-55.9%</td></tr><tr><td>Total</td><td>418</td><td>513</td><td>-18.4%</td><td>1,773</td><td>2,145</td><td>-17.3%</td></tr></table>

Source: CNEV Post, Motor Intelligence, European Union  
Note: China data are based on preliminary CPCA retail sales data.

Figure 1: Global EV battery installations by company vs KOR battery cell market share  
GWh, %  
![](images/5e683fb46f2c70a2c00134a4c5ad9f6c353967bc48f206c58276254dea263fb7.jpg)

<details>
<summary>bar chart</summary>

| Month   | CATL | LGES | SDI | BYD | Panasonic | SK On |
|---------|------|------|-----|-----|-----------|-------|
| Jan-25  | 30   | 10   | 5   | 10  | 5         | 5     |
| Feb-25  | 30   | 10   | 5   | 10  | 5         | 5     |
| Mar-25  | 35   | 15   | 5   | 10  | 5         | 5     |
| Apr-25  | 30   | 15   | 5   | 10  | 5         | 5     |
| May-25  | 30   | 15   | 5   | 10  | 5         | 5     |
| Jun-25  | 30   | 15   | 5   | 10  | 5         | 5     |
| Jul-25  | 30   | 15   | 5   | 10  | 5         | 5     |
| Aug-25  | 30   | 15   | 5   | 10  | 5         | 5     |
| Sep-25  | 40   | 15   | 5   | 10  | 5         | 5     |
| Oct-25  | 30   | 10   | 5   | 10  | 5         | 5     |
| Nov-25  | 40   | 10   | 5   | 10  | 5         | 5     |
| Dec-25  | 40   | 10   | 5   | 10  | 5         | 5     |
| Jan-26  | 30   | 10   | 5   | 10  | 5         | 5     |
| Feb-26  | 30   | 10   | 5   | 10  | 5         | 5     |
| Mar-26  | 40   | 10   | 5   | 10  | 5         | 5     |
| Apr-26  | 40   | 10   | 5   | 10  | 5         | 5     |
</details>

Source: SNE Research.

<table><tr><td>Global EV/PHEV Penetration (%)</td><td>May-26</td><td>May-25</td><td>y/y%</td><td>5M26</td><td>5M25</td><td>y/y%</td></tr><tr><td colspan="7">EV/PHEV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>32.0%</td><td>23.8%</td><td>8.2%p</td><td>29.8%</td><td>22.7%</td><td>7.0%p</td></tr><tr><td>Germany</td><td>36.7%</td><td>28.5%</td><td>8.2%p</td><td>35.0%</td><td>27.5%</td><td>7.5%p</td></tr><tr><td>France</td><td>35.1%</td><td>22.3%</td><td>12.8%p</td><td>32.2%</td><td>23.3%</td><td>8.8%p</td></tr><tr><td>Italy</td><td>18.9%</td><td>10.0%</td><td>8.9%p</td><td>16.9%</td><td>9.7%</td><td>7.2%p</td></tr><tr><td>Spain</td><td>23.0%</td><td>19.4%</td><td>3.7%p</td><td>21.5%</td><td>15.8%</td><td>5.7%p</td></tr><tr><td>United Kingdom</td><td>41.1%</td><td>33.7%</td><td>7.4%p</td><td>37.0%</td><td>30.9%</td><td>6.1%p</td></tr><tr><td>China</td><td>62.9%</td><td>52.7%</td><td>10.2%p</td><td>52.1%</td><td>49.4%</td><td>2.7%p</td></tr><tr><td>US</td><td>7.1%</td><td>9.1%</td><td>-1.9%p</td><td>6.9%</td><td>9.7%</td><td>-2.8%p</td></tr><tr><td>Total</td><td>34.6%</td><td>32.0%</td><td>2.6%p</td><td>30.3%</td><td>30.1%</td><td>0.1%p</td></tr><tr><td colspan="7">EV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>21.1%</td><td>14.5%</td><td>6.5%p</td><td>19.6%</td><td>14.7%</td><td>5.0%p</td></tr><tr><td>Germany</td><td>25.0%</td><td>18.0%</td><td>7.1%p</td><td>23.9%</td><td>17.6%</td><td>6.3%p</td></tr><tr><td>France</td><td>29.1%</td><td>15.7%</td><td>13.5%p</td><td>27.8%</td><td>17.8%</td><td>10.0%p</td></tr><tr><td>Italy</td><td>8.8%</td><td>5.1%</td><td>3.7%p</td><td>8.2%</td><td>5.1%</td><td>3.1%p</td></tr><tr><td>Spain</td><td>10.8%</td><td>7.9%</td><td>2.8%p</td><td>9.4%</td><td>7.1%</td><td>2.3%p</td></tr><tr><td>United Kingdom</td><td>27.3%</td><td>21.8%</td><td>5.5%p</td><td>23.9%</td><td>20.9%</td><td>3.0%p</td></tr><tr><td>China</td><td>42.2%</td><td>31.3%</td><td>10.9%p</td><td>34.0%</td><td>30.4%</td><td>3.6%p</td></tr><tr><td>US</td><td>5.8%</td><td>7.2%</td><td>-1.3%p</td><td>5.9%</td><td>7.5%</td><td>-1.6%p</td></tr><tr><td>Total</td><td>23.5%</td><td>19.7%</td><td>3.8%p</td><td>20.3%</td><td>19.2%</td><td>1.1%p</td></tr><tr><td colspan="7">PHEV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>11.0%</td><td>9.3%</td><td>1.7%p</td><td>10.1%</td><td>8.0%</td><td>2.1%p</td></tr><tr><td>Germany</td><td>11.7%</td><td>10.5%</td><td>1.1%p</td><td>11.1%</td><td>9.9%</td><td>1.2%p</td></tr><tr><td>France</td><td>6.0%</td><td>6.6%</td><td>-0.6%p</td><td>4.4%</td><td>5.6%</td><td>-1.2%p</td></tr><tr><td>Italy</td><td>10.1%</td><td>4.9%</td><td>5.2%p</td><td>8.7%</td><td>4.6%</td><td>4.1%p</td></tr><tr><td>Spain</td><td>12.3%</td><td>11.4%</td><td>0.8%p</td><td>12.0%</td><td>8.7%</td><td>3.4%p</td></tr><tr><td>United Kingdom</td><td>13.8%</td><td>11.9%</td><td>1.9%p</td><td>13.1%</td><td>10.1%</td><td>3.1%p</td></tr><tr><td>China</td><td>20.7%</td><td>21.4%</td><td>-0.6%p</td><td>18.1%</td><td>19.0%</td><td>-0.9%p</td></tr><tr><td>US</td><td>1.3%</td><td>1.9%</td><td>-0.6%p</td><td>1.0%</td><td>2.2%</td><td>-1.2%p</td></tr><tr><td>Total</td><td>11.1%</td><td>12.3%</td><td>-1.2%p</td><td>10.0%</td><td>10.9%</td><td>-1.0%p</td></tr></table>

Figure 2: Global EV battery installation market share trend by company %  
![](images/6bb9fc7ea02530d2cd154f2b1b7c2669bb5f858af006444117bcb7e16ddfdc01.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | CATL (%) | BYD (%) | LGES (%) | Panasonic (%) | SDI (%) | SK On (%) | Others (%) |
|---|---|---|---|---|---|---|---|
| Jan-25 | 40 | 15 | 10 | 5 | 5 | 5 | 3 |
| Feb-25 | 38 | 16 | 10 | 5 | 5 | 5 | 3 |
| Mar-25 | 37 | 17 | 10 | 5 | 5 | 5 | 3 |
| Apr-25 | 37 | 18 | 10 | 5 | 5 | 5 | 3 |
| May-25 | 37 | 19 | 10 | 5 | 5 | 5 | 3 |
| Jun-25 | 36 | 20 | 10 | 5 | 5 | 5 | 3 |
| Jul-25 | 36 | 21 | 10 | 5 | 5 | 5 | 3 |
| Aug-25 | 34 | 22 | 10 | 5 | 5 | 5 | 3 |
| Sep-25 | 34 | 23 | 10 | 5 | 5 | 5 | 3 |
| Oct-25 | 48 | 14 | 10 | 5 | 5 | 5 | 3 |
| Nov-25 | 40 | 16 | 10 | 5 | 5 | 5 | 3 |
| Dec-25 | 42 | 17 | 10 | 5 | 5 | 5 | 3 |
| Jan-26 | 44 | 18 | 10 | 5 | 5 | 5 | 3 |
| Feb-26 | 42 | 16 | 10 | 5 | 5 | 5 | 3 |
| Mar-26 | 40 | 17 | 10 | 5 | 5 | 5 | 3 |
| Apr-26 | 40 | 17 | 10 | 5 | 5 | 5 | 3 |
The chart displays the percentage market share of different battery manufacturers over time. The x-axis represents time from Jan-25 to Apr-26, and the y-axis represents the percentage share. The legend identifies each manufacturer: CATL (red), BYD (blue), LGES (yellow), Panasonic (gray), SDI (light blue), SK On (dark gray), and Others (black). The data is already in English. There is no variation in the chart title or axis labels beyond the specific values.
</details>

Source: SNE Research.

Figure 3: EU10 + US + China EV/PHEV sales and penetration

[中间内容因长度限制已省略]

mance is not indicative of future results.

Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 11 Jun 2026 05:50 PM HKT

Disseminated 11 Jun 2026 05:50 PM HKT
"""
