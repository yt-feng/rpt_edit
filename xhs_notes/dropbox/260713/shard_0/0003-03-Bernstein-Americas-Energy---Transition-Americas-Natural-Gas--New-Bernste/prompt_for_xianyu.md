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
# Americas Energy & Transition

# Americas Natural Gas: New Bernstein Power Model helps confirm our bullish gas outlook...Haynesville activity doesn't deter us

![](images/10f2f0674c59d2ae1908ca5eb4487c6b575c53d538a6e5fce884d16f92b26c64.jpg)  
Bob Brackett, Ph.D.  
+1 917 344 8422  
bob.brackett@bernsteinsg.com

![](images/fe2f824978300032c7f61b096d804a0db3ae87acca3fe77c79fcf4c55f2e16fb.jpg)

Minnie Xu

+1 917 344 8574

minnie.xu@bernsteinsg.com

![](images/2c2fd520de4ccb8135cef3e134dbcced0adf49cafed82f73b6def25b1fc139c2.jpg)

Raphael Lee

+1 917 344 8355

raphael.lee@bernsteinsg.com

Bernstein has recently launched on Americas Power and Energy Transition (The American Energy Transition: Grid, Gas, and Green - Sector Initiation - Power and Energy Transition) including a proprietary US power model. That new forecast strongly informs our gas demand into power. We update our US gas model accordingly and update most recent data across power, LNG, other demand and supply. We reiterate our long term mid-cycle gas price deck of \$5/mcf.

## We argue gas demand growth is 3 pronged:

\- As LNG capacity continues to expand, LNG liftings will grow in tandem from \~18 bcfd in early 2026 to \~33 bcfd in late 2030 (Exhibit 17).

\- We project aggregate power demand to grow at a 2.6% CAGR through 2030 (Exhibit 2), with gas making up a large percentage of the fuel mix (Exhibit 3).

\- As supply increases (but also remains disciplined), we expect losses from extraction, plant use, and distribution to consume more gas linearly (Exhibit 9).

We continue to highlight supply discipline in the Permian (the largest source of gas growth associated with shale oil drilling) as well as the Appalachia basin (Exhibit 11). Since the start of 2024, Permian and Appalachian rig counts are down 25% and 21%, respectively.

We also observe the tick up in rigs in the Haynesville that suggest increased activity, but we argue that this growth comes from operators with traditionally lower IPs (Exhibit 15).

Haynesville including GEP and EXE (Exhibit 16), with major growth coming from APEX Natural Gas (formerly Paloma Natural Gas), operators with historically lower gas production per well in the cohort we benchmarked in our previous note, Americas Energy & Transition: What the future decades hold for the Haynesville Shale.

Our Permian gas outlook has been updated with increased future takeaway capacity... with more capacity coming online from expansions such as the Transwestern desert pipeline expansion from 1.5 to 2.3 bcfd and the 2.8 bcfd Saguaro connector pipeline (Exhibit 19).

We provide a summary to the updates we made from our previous model (Exhibit 10).

We continue to see significant upside in Henry Hub-levered equities (EQT, EXE, DVN).

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td colspan="4">9 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>LNG (Cheniere Energy)</td><td>O</td><td>USD</td><td>261.29</td><td>283.00</td><td>(11.5)%</td><td>USD</td><td>24.19</td><td>16.70</td><td>15.06</td><td>10.8</td><td>15.6</td><td>17.3</td></tr><tr><td>COP (ConocoPhillips)</td><td>O</td><td>USD</td><td>108.02</td><td>121.00</td><td>(7.2)%</td><td>USD</td><td>6.18</td><td>13.89</td><td>10.88</td><td>17.5</td><td>7.8</td><td>9.9</td></tr><tr><td>CVX (Chevron)</td><td>M</td><td>USD</td><td>174.05</td><td>204.00</td><td>(7.6)%</td><td>USD</td><td>8.43</td><td>16.58</td><td>13.26</td><td>20.7</td><td>10.5</td><td>13.1</td></tr><tr><td>EOG (EOG)</td><td>M</td><td>USD</td><td>133.54</td><td>155.00</td><td>(11.2)%</td><td>USD</td><td>9.88</td><td>18.93</td><td>16.25</td><td>13.5</td><td>7.1</td><td>8.2</td></tr><tr><td>KOS (Kosmos Energy)</td><td>M</td><td>USD</td><td>2.18</td><td>2.40</td><td>(24.6)%</td><td>USD</td><td>(1.58)</td><td>1.13</td><td>0.75</td><td>(1.4)</td><td>1.9</td><td>2.9</td></tr><tr><td>KOS.LN (Kosmos Energy)</td><td>M</td><td>GBp</td><td>157.00</td><td>177.00</td><td>(16.3)%</td><td>GBP</td><td>(1.17)</td><td>0.83</td><td>0.56</td><td>(1.3)</td><td>1.9</td><td>2.8</td></tr><tr><td>XOM (ExxonMobil)</td><td>O</td><td>USD</td><td>137.46</td><td>182.00</td><td>(0.7)%</td><td>USD</td><td>7.37</td><td>16.37</td><td>14.49</td><td>18.6</td><td>8.4</td><td>9.5</td></tr><tr><td>APA (APA)</td><td>M</td><td>USD</td><td>33.29</td><td>40.00</td><td>41.5%</td><td>USD</td><td>2.83</td><td>7.20</td><td>6.42</td><td>11.8</td><td>4.6</td><td>5.2</td></tr><tr><td>DVN (Devon Energy)</td><td>O</td><td>USD</td><td>42.02</td><td>59.00</td><td>3.2%</td><td>USD</td><td>4.17</td><td>10.06</td><td>8.43</td><td>10.1</td><td>4.2</td><td>5.0</td></tr><tr><td>FANG (Diamondback)</td><td>O</td><td>USD</td><td>182.00</td><td>241.00</td><td>6.5%</td><td>USD</td><td>4.57</td><td>32.21</td><td>27.22</td><td>39.8</td><td>5.7</td><td>6.7</td></tr><tr><td>EQT (EQT)</td><td>O</td><td>USD</td><td>50.15</td><td>69.00</td><td>(31.6)%</td><td>USD</td><td>3.31</td><td>8.15</td><td>8.58</td><td>7.6</td><td>4.7</td><td>4.6</td></tr><tr><td>CQP (Cheniere Energy Partners)</td><td>M</td><td>USD</td><td>64.88</td><td>58.00</td><td>(5.2)%</td><td>USD</td><td>5.17</td><td>4.69</td><td>3.66</td><td>12.6</td><td>13.8</td><td>17.7</td></tr><tr><td>VG (Venture Global)</td><td>M</td><td>USD</td><td>12.53</td><td>14.00</td><td>(48.6)%</td><td>USD</td><td>0.86</td><td>0.86</td><td>0.86</td><td>8.4</td><td>7.8</td><td>7.6</td></tr><tr><td>EXE (Expand Energy)</td><td>O</td><td>USD</td><td>88.97</td><td>160.00</td><td>(38.7)%</td><td>USD</td><td>7.57</td><td>12.77</td><td>18.37</td><td>11.8</td><td>7.0</td><td>4.8</td></tr><tr><td>SPX</td><td></td><td></td><td>7,575.39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,593.41</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
LNG, EQT, CQP estimate is Reported EPS; LNG, CQP valuation is Reported P/E (x); EQT, VG valuation is EV/EBITDA (x);
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We believe that \$5/mcf is the appropriate mid-cycle price for Henry Hub. As such we continue to see significant upside in Henry Hub-levered equities (EQT, EXE, DVN) which we are rate out perform.

## LONG TERM - SIGNIFICANT GAS DEMAND GROWTH TO 2030

We remind investors of our long term bullish thesis (The Long View: A US gas supercycle is coming...we upgrade gassy E&Ps).

Without invoking industrial, commercial or residential demand growth, we forecast \~24% growth in gas demand by 2030 on the back of LNG exports, power demand and growing the volumes of gas supply required to distribute the new gas demand.

EXHIBIT 1: Three pillars grow gas demand by 24% by 2030

Growing to 2030 gas demand (bcfd)

![](images/a97640cb84e24f0391aaf8c7d74babb10ca7041a0c662dcb770feb9b8d29ba88.jpg)  
Source: EIA; Bloomberg; Baker Hughes; Enverus; Company reports; Bernstein estimates & analysis

As we update our US power model, power demand growth provides significant growth in gas demand used in generation.

EXHIBIT 2: We expect aggregate US power demand to grow at a 2.6% CAGR from 2025-2030...  
Total power demand (TWh)  
![](images/f6ceed7a35d553a9f5b6928e31a81173160d645b281b0727787462dc1223007a.jpg)  
Source: EIA; Bernstein analysis

EXHIBIT 3: ...with gas assuming a large piece of the pie  
![](images/211e020df301c0e632b02d49a38ecadc1dbc11019b405f2360faf14e34168251.jpg)  
Source: EIA, Bernstein analysis

EXHIBIT 4: We expect gas demand for power to grow at a 2.5% CAGR through 2030  
Implied Gas Demand for Power (bcfd)  
![](images/2dc493863d57ac02cf1f2023053f05084dd3b76b3f1b5afb42a1657fe8b28685.jpg)  
Source: EIA; Bernstein analysis

Obviously, one of our pillars for gas bullishness is the growing use of gas for power demand (both AI and other end uses). Such demand growth did not arrive in 2025 mostly due to coal switching (AE&T: What coal stole explains the majority of the summer gas price move...but winter is coming). We explicitly include such switching but argue additional coal switching is limited (Coal/gas switching matters... for gas bulls it's a modest impact, and higher gas means higher rail rates). As data center build out progresses, we expect power demand for gas to grow \~2 bcfd in 2026 rising towards \~6 bcfd by 2030 from 2025. We note that power demand for gas this year is entering the strong demand season well above last year and even above the previous record year of 2024.

EXHIBIT 5: Power demand for gas flattish year on year  
Power demand for gas (bcfd) flat year on year  
![](images/1a39659b399b2f70b0b7b25926ce9b6076c105cd16d2471ec0e066717fd940b3.jpg)  
Source: EIA; Bernstein analysis  
Growth in LNG liftings remains a key part to our thesis.

EXHIBIT 6: We project that as LNG capacity continues to expand, LNG lifting to grow with it

US LNG Capacity  
![](images/e118d8efe0ec6a4b038e2e2a67a2ddf675bf16f1d9f484489a534baf1b5a7084.jpg)  
Source: EIA, Bernstein analysis and estimates

■ Residential ■ Commercial

While recom demand should be seasonal and flattish.

EXHIBIT 7: We conservatively project flat residential and commercial gas demand  
Rescom Gas Demand (bcfd)  
![](images/6ce69dee3cf20df2007e6286b3126c0413a3626db47c2199e4ac4d44ac6652df.jpg)  
Source: EIA, Bernstein analysis and estimates

To achieve more than 150 bcfd by 2030 requires heavy lifting by the constrained Permian (41% growth), constrained Appalachia (13% growth), Haynesville (65% growth) and even so the balance isn't met - we believe \$5/mcf is required to convince the upstream to deliver the required molecules.

EXHIBIT 8: Achieving 154 BCFD of demand in 2030 will require 'heavy lifting' from all basins...and more

Balancing 2030 gas demand (bcfd)

![](images/3883b967d9a070827323a7bf56b8e9915bf2beee08370c3b81da84c15d01a146.jpg)  
Missing gas includes missing gross withdrawals as well as other items, including balancing items Source: EIA; Bloomberg; Baker Hughes; Enverus; Company reports; Bernstein estimates & analysis

Our summary of the US gas landscape to 2030 is shown below.  
EXHIBIT 9: US Gas Overview

<table><tr><td>Demand (Bcfd)</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Industrial</td><td>22.95</td><td>23.38</td><td>23.44</td><td>23.44</td><td>23.64</td><td>23.53</td><td>23.53</td><td>23.53</td><td>23.53</td><td>23.53</td></tr><tr><td>Commercial</td><td>9.06</td><td>9.65</td><td>9.16</td><td>9.07</td><td>9.93</td><td>9.66</td><td>8.42</td><td>8.42</td><td>8.42</td><td>8.42</td></tr><tr><td>Residential</td><td>13.03</td><td>13.67</td><td>12.46</td><td>12.00</td><td>13.35</td><td>12.85</td><td>11.69</td><td>11.69</td><td>11.69</td><td>11.69</td></tr><tr><td>Power</td><td>30.7</td><td>33.1</td><td>35.4</td><td>36.8</td><td>35.7</td><td>37.7</td><td>39.0</td><td>39.8</td><td>40.9</td><td>41.6</td></tr><tr><td>Vehicle Fuel</td><td>0.15</td><td>0.18</td><td>0.16</td><td>0.17</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td></tr><tr><td>Net Mexico Pipeline Exports</td><td>5.8</td><td>5.6</td><td>6.1</td><td>6.4</td><td>6.6</td><td>7.1</td><td>7.6</td><td>7.6</td><td>7.6</td><td>7.6</td></tr><tr><td>LNG Exports</td><td>9.7</td><td>10.6</td><td>11.9</td><td>11.9</td><td>15.1</td><td>18.5</td><td>22.3</td><td>26.5</td><td>30.6</td><td>32.4</td></tr><tr><td>Lease and Plant Use</td><td>5.1</td><td>5.1</td><td>5.3</td><td>5.3</td><td>5.6</td><td>5.8</td><td>6.2</td><td>6.5</td><td>6.7</td><td>6.9</td></tr><tr><td>Extraction Loss to NGLs</td><td>7.7</td><td>8.4</td><td>9.3</td><td>10.0</td><td>10.8</td><td>12.3</td><td>14.3</td><td>15.7</td><td>17.0</td><td>18.2</td></tr><tr><td>Pipeline and Distribution</td><td>3.1</td><td>3.4</td><td>3.4</td><td>3.5</td><td>3.6</td><td>3.6</td><td>3.8</td><td>4.0</td><td>4.2</td><td>4.3</td></tr><tr><td>Coal Switching/Demand Destruction</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>-0.4</td><td>-0.7</td><td>-1.0</td><td>-0.8</td><td>-0.8</td></tr><tr><td>Total (Bcfd)</td><td>107.3</td><td>113.2</td><td>116.6</td><td>118.6</td><td>124.4</td><td>130.9</td><td>136.4</td><td>143.0</td><td>150.0</td><td>154.0</td></tr></table>

<table><tr><td>Supply (Bcfd)</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>US Marketed Production*</td><td>101.3</td><td>106.7</td><td>111.4</td><td>112.1</td><td>117.4</td><td>122.5</td><td>130.1</td><td>136.9</td><td>142.0</td><td>145.3</td></tr><tr><td>Balancing &amp; Supplemental</td><td>-0.3</td><td>-1.0</td><td>0.5</td><td>-0.3</td><td>-0.2</td><td>0.1</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td></tr><tr><td>Net Canada Pipeline Imports</td><td>5.1</td><td>5.7</td><td>5.2</td><td>5.9</td><td>5.8</td><td>5.6</td><td>5.8</td><td>5.7</td><td>5.7</td><td>5.7</td></tr><tr><td>Total (Bcfd)</td><td>106.1</td><td>111.4</td><td>117.1</td><td>117.6</td><td>123.0</td><td>128.3</td><td>136.1</td><td>142.9</td><td>148.0</td><td>151.3</td></tr></table>

<table><tr><td>US Gross Withdrawals (Bcfd) **</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Gas from Permian Shale Oil</td><td>17.8</td><td>20.6</td><td>23.2</td><td>25.8</td><td>28.0</td><td>28.7</td><td>32.1</td><td>35.0</td><td>37.4</td><td>39.6</td></tr><tr><td>Gas from Other Shale Oil</td><td>19.5</td><td>21.2</td><td>22.8</td><td>23.3</td><td>24.0</td><td>24.2</td><td>24.4</td><td>24.7</td><td>25.0</td><td>25.2</td></tr><tr><td>Bakken</td><td>3.0</td><td>3.2</td><td>3.4</td><td>3.5</td><td>3.6</td><td>3.5</td><td>3.6</td><td>3.6</td><td>3.6</td><td>3.6</td></tr><tr><td>Eagle Ford</td><td>5.7</td><td>6.6</td><td>7.7</td><td>8.0</td><td>8.6</td><td>8.4</td><td>8.6</td><td>8.9</td><td>9.2</td><td>9.4</td></tr><tr><td>Rockies</td><td>3.9</td><td>4.0</td><td>4.1</td><td>4.6</td><td>4.7</td><td>4.9</td><td>4.9</td><td>4.9</td><td>4.9</td><td>4.9</td></tr><tr><td>Midcon</td><td>7.0</td><td>7.4</td><td>7.6</td><td>7.2</td><td>7.1</td><td>7.4</td><td>7.4</td><td>7.4</td><td>7.4</td><td>7.4</td></tr><tr><td>Appalachia</td><td>33.8</td><td>34.4</td><td>35.0</td><td>35.3</td><td>36.3</td><td>37.0</td><td>37.8</td><td>40.0</td><td>41.0</td><td>41.1</td></tr><tr><td>Haynesville</td><td>12.7</td><td>14.8</td><td>15.9</td><td>14.2</td><td>14.6</td><td>16.1</td><td>17.7</td><td>17.9</td><td>17.9</td><td>17.9</td></tr><tr><td>Other Basins</td><td>20.7</td><td>19.0</td><td>17.8</td><td>17.0</td><td>18.2</td><td>19.3</td><td>19.0</td><td>18.6</td><td>18.2</td><td>17.8</td></tr><tr><td>call on more Haynesville</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.5</td><td>2.0</td><td>3.7</td><td>5.3</td><td>6.2</td></tr><tr><td>Missing Gas</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td><td>1.0</td></tr><tr><td>Total</td><td>104.6</td><td>109.9</td><td>114.8</td><td>115.6</td><td>121.0</td><td>126.0</td><td>133.6</td><td>140.5</td><td>145.5</td><td>148.9</td></tr></table>

<table><tr><td>Storage (BCF)</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Total Storage</td><td>2,719</td><td>2,456</td><td>2,891</td><td>3,125</td><td>2,918</td><td>2,672</td><td>2,589</td><td>2,346

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
