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
# Korea Auto Parts & Robotics

## Risk/reward looks more attractive after 36%/37% correction from the peak; U/G Mobis/Mando to OW/N

We upgrade Hyundai Mobis (Mobis; N to OW) and HL Mando (Mando; UW to N) as prices now largely reflect core businesses, leaving robot actuators as incremental optionality. In our Mobis SOTP, the core auto parts business (W44tn) plus its stake in the robotics business (W6tn) of Hyundai Motor Group (HMG) broadly explains the current market cap, with incremental upside from actuators (W13tn). For Mando, we still see limited visibility on actuator order wins and therefore assign limited benefit of the doubt, but valuation is effectively supported by the implied value of the core franchise (W2.3tn), roughly in-line with the current market cap. Investor feedback frames both as “robot leverage” plays: actuators may not be structurally attractive, but can remain a narrative catalyst amid robotics momentum. We expect 2Q to be a non-event: commodity headwinds and FX tailwinds would likely offset; Mobis also has a structural A/S profit boost.

\- Risk/reward more attractive after a sharp pullback; actuator upside now more “call option”. In our Mobis SOTP, the core auto parts business (W44tn) plus its stake in HMG’s robotics business (W6tn) broadly explains the current market cap. Incremental upside could come from the actuator business, which we value at W13tn by applying a 20x P/S multiple to 2030E actuator sales of \~W0.8tn. For Mando, we still see limited visibility on actuator order wins and therefore do not assign meaningful “benefit of the doubt” to actuators; however, the stock is effectively supported by the implied value of the core auto parts business (W2.3tn), which already aligns with the current market cap.

\- Key investor feedback from our Asia marketing: Mobis/Mando viewed as “robot leverage” plays. Investors largely agreed with our fundamental view (link to our initiation report) that newly entering the actuator segment may not be highly profitable. That said, the parts suppliers’ actuator initiatives could still act as a narrative catalyst for the stocks. Some investors believe that Mobis and Mando have corrected sufficiently from peak levels and note that the names are difficult shorts, given ongoing robotics momentum and potential ETF-related flows.

\- 2Q likely a non-event; commodity headwinds largely in estimates, with FX a partial offset. We estimate annual OP sensitivity of \~W950bn/\~W150bn for Mobis/Mando from higher commodity inputs (aluminium, copper, plastic, semiconductor), with \~70-80% expected to be passed through to OEMs with a one quarter lag. Offsetting this, both should benefit from FX tailwinds of \~W350bn/\~W25bn on an annualized basis, based on our estimates. Mobis should also enjoy a structural A/S profit boost, supported by structural tailwinds from rising HMG model ASPs in developed markets and a growing portion of the Genesis fleet reaching the five-year mark. Overall, our 2Q OP estimates of W901bn (+W131bn y/y) for Mobis and W104bn (flat y/y) for Mando already reflect these dynamics.

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev End Date</td><td></td></tr><tr><td>Hyundai Mobis</td><td>012330 KS</td><td>29,026</td><td>KRW</td><td>489,000</td><td>OW</td><td>N</td><td>710,000</td><td>Dec-27</td><td>n/c</td><td>n/c</td></tr><tr><td>HL Mando</td><td>204320 KS</td><td>1,493</td><td>KRW</td><td>48,600</td><td>N</td><td>UW</td><td>50,000</td><td>Dec-27</td><td>n/c</td><td>n/c</td></tr></table>

Equity Ratings and Price Targets

Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC

(82-2) 758 5716

sonny.lee@JPM.com

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 07 Jul 26.

Seri Yoon

(82-2) 758 5704

seri.yoon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

See page 15 for analyst certification and important disclosures, including non-US analyst disclosures.

\- Upgrade Mobis (N to OW) and Mando (UW to N) on improved risk/reward. With Mobis/Mando shares down 36%/37% from their recent peaks (vs the KOSPI -10/-12%), we revisit our stance. At current levels, the share prices largely reflect the core auto parts franchises, making robotics and actuators incremental optionality rather than fully priced expectations. Given the market is currently framing the actuator opportunity using a P/S lens (rather than P/E), we believe improved revenue visibility alone could be sufficient to move the stocks. Even after these upgrades, we continue to prefer OEMs (HMC/Kia; both OW) over parts suppliers, given OEMs' increasing discretion across the value chain in both autos and robotics. While HMC and Mobis share prices have moved largely in tandem over the past month (HMC -25% vs. Mobis -19%), we expect HMC's differentiated earnings momentum, supported by a stronger model cycle from 2H26, to begin to materialize and drive outperformance vs. parts suppliers.

Table 1: Global auto parts: valuation comparison

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt. cap (US$bn)</td><td colspan="2">P/E (x)</td><td colspan="2">P/B (x)</td><td colspan="2">ROE</td><td colspan="2">OPM</td><td colspan="2">NP growth</td></tr><tr><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td></tr><tr><td>Mobis</td><td>012330 KS</td><td>30.3</td><td>10</td><td>9</td><td>0.8</td><td>0.8</td><td>8%</td><td>9%</td><td>6%</td><td>6%</td><td>16%</td><td>12%</td></tr><tr><td>Mando</td><td>204320 KS</td><td>1.5</td><td>12</td><td>10</td><td>0.8</td><td>0.8</td><td>7%</td><td>8%</td><td>4%</td><td>5%</td><td>95%</td><td>21%</td></tr><tr><td>Autoever</td><td>307950 KS</td><td>8.8</td><td>61</td><td>47</td><td>6.5</td><td>5.8</td><td>11%</td><td>13%</td><td>6%</td><td>7%</td><td>18%</td><td>29%</td></tr><tr><td>Valeo</td><td>FR FP</td><td>3.8</td><td>10</td><td>7</td><td>0.9</td><td>0.8</td><td>9%</td><td>12%</td><td>4%</td><td>5%</td><td>62%</td><td>38%</td></tr><tr><td>Forvia</td><td>FAU GR</td><td>2.1</td><td>n/a</td><td>7</td><td>0.7</td><td>0.6</td><td>-1%</td><td>8%</td><td>6%</td><td>6%</td><td>97%</td><td>583%</td></tr><tr><td>Continental</td><td>CON GY</td><td>17.0</td><td>12</td><td>10</td><td>3.2</td><td>2.7</td><td>29%</td><td>29%</td><td>11%</td><td>13%</td><td>857%</td><td>18%</td></tr><tr><td>Denso</td><td>6902 JP</td><td>35.7</td><td>13</td><td>12</td><td>1.1</td><td>0.9</td><td>8%</td><td>8%</td><td>7%</td><td>7%</td><td>6%</td><td>-6%</td></tr><tr><td>Aisin</td><td>7259 JP</td><td>10.6</td><td>12</td><td>10</td><td>0.9</td><td>0.8</td><td>7%</td><td>8%</td><td>4%</td><td>5%</td><td>60%</td><td>-7%</td></tr><tr><td>Magna</td><td>MGA US</td><td>17.7</td><td>10</td><td>9</td><td>1.5</td><td>1.4</td><td>15%</td><td>15%</td><td>6%</td><td>6%</td><td>11%</td><td>7%</td></tr><tr><td>Aptiv</td><td>APTV US</td><td>12.6</td><td>10</td><td>9</td><td>1.3</td><td>1.2</td><td>14%</td><td>14%</td><td>14%</td><td>15%</td><td>-25%</td><td>8%</td></tr><tr><td>Autoliv</td><td>ALV US</td><td>9.0</td><td>11</td><td>10</td><td>3.3</td><td>2.9</td><td>29%</td><td>32%</td><td>11%</td><td>11%</td><td>1%</td><td>12%</td></tr><tr><td>Lear</td><td>LEA US</td><td>6.7</td><td>9</td><td>8</td><td>1.3</td><td>1.1</td><td>14%</td><td>15%</td><td>5%</td><td>5%</td><td>8%</td><td>11%</td></tr><tr><td>BorgWarner</td><td>BWA US</td><td>13.5</td><td>13</td><td>11</td><td>2.3</td><td>2.0</td><td>17%</td><td>18%</td><td>11%</td><td>11%</td><td>1%</td><td>9%</td></tr></table>

Note: Price as of 6 July 2026.  
Source: Bloomberg Finance L.P.

Table 2: Robotics: valuation comparison

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt. cap (US$bn)</td><td colspan="2">P/E (x)</td><td colspan="2">P/B (x)</td><td colspan="2">P/S (x)</td><td colspan="2">OPM</td><td colspan="2">Rev growth</td></tr><tr><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td></tr><tr><td>Mobis</td><td>012330 KS</td><td>30.3</td><td>10</td><td>9</td><td>0.8</td><td>0.8</td><td>0.7</td><td>0.6</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td></tr><tr><td>Mando</td><td>204320 KS</td><td>1.5</td><td>12</td><td>10</td><td>0.8</td><td>0.8</td><td>0.2</td><td>0.2</td><td>4%</td><td>5%</td><td>3%</td><td>6%</td></tr><tr><td>Autoever</td><td>307950 KS</td><td>8.8</td><td>61</td><td>47</td><td>6.5</td><td>5.8</td><td>2.7</td><td>2.4</td><td>6%</td><td>7%</td><td>13%</td><td>15%</td></tr><tr><td>Leader Harmonic Drive</td><td>688017 CH</td><td>12.3</td><td>454</td><td>317</td><td>23.1</td><td>21.9</td><td>97.7</td><td>67.1</td><td>21%</td><td>22%</td><td>55%</td><td>46%</td></tr><tr><td>Orbbec</td><td>688322 CH</td><td>7.7</td><td>172</td><td>100</td><td>15.2</td><td>13.3</td><td>33.6</td><td>22.5</td><td>19%</td><td>22%</td><td>65%</td><td>49%</td></tr><tr><td>Zhaowei Machinery &amp; Electronic</td><td>003021 CH</td><td>3.6</td><td>77</td><td>60</td><td>n/a</td><td>4.3</td><td>10.6</td><td>8.4</td><td>15%</td><td>15%</td><td>16%</td><td>26%</td></tr><tr><td>Fortior Technology</td><td>688279 CH</td><td>3.5</td><td>76</td><td>54</td><td>5.0</td><td>4.7</td><td>22.8</td><td>17.0</td><td>34%</td><td>37%</td><td>32%</td><td>34%</td></tr><tr><td>Haozhi Industrial</td><td>300503 CH</td><td>5.0</td><td>97</td><td>72</td><td>19.1</td><td>15.9</td><td>14.0</td><td>10.9</td><td>16%</td><td>18%</td><td>45%</td><td>28%</td></tr><tr><td>Harmonic Drive Systems</td><td>6324 JP</td><td>5.3</td><td>466</td><td>136</td><td>9.7</td><td>9.1</td><td>13.1</td><td>10.9</td><td>4%</td><td>11%</td><td>6%</td><td>20%</td></tr><tr><td>Six robot parts suppliers average</td><td></td><td>6.2</td><td>224</td><td>123</td><td>14.4</td><td>11.5</td><td>32.0</td><td>22.8</td><td>18%</td><td>21%</td><td>37%</td><td>34%</td></tr><tr><td>Sanhua Intelligent Controls</td><td>002050 CH</td><td>27.1</td><td>41</td><td>36</td><td>5.4</td><td>4.9</td><td>5.2</td><td>4.5</td><td>16%</td><td>16%</td><td>7%</td><td>15%</td></tr><tr><td>Hengli Hydraulic</td><td>601100 CH</td><td>23.2</td><td>45</td><td>37</td><td>7.8</td><td>6.8</td><td>11.7</td><td>9.9</td><td>28%</td><td>29%</td><td>24%</td><td>18%</td></tr><tr><td>Shuanghuan Driveline</td><td>002472 CH</td><td>5.8</td><td>26</td><td>22</td><td>3.4</td><td>3.0</td><td>3.6</td><td>3.2</td><td>16%</td><td>17%</td><td>12%</td><td>15%</td></tr></table>

Note: Price as of 6 July 2026.
Source: Bloomberg Finance L.P.

Table 3: JPMe vs. Consensus  
Wbn, %

<table><tr><td colspan="7">Mobis</td><td colspan="3"></td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>66,211</td><td>65,123</td><td>2%</td><td>68,389</td><td>69,380</td><td>-1%</td><td>70,465</td><td>73,729</td><td>-4%</td></tr><tr><td>OP</td><td>3,493</td><td>3,717</td><td>-6%</td><td>3,968</td><td>4,185</td><td>-5%</td><td>4,367</td><td>4,599</td><td>-5%</td></tr><tr><td colspan="7">Mando</td><td colspan="3"></td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>9,893</td><td>9,726</td><td>2%</td><td>10,382</td><td>10,206</td><td>2%</td><td>10,812</td><td>10,906</td><td>-1%</td></tr><tr><td>OP</td><td>389</td><td>411</td><td>-5%</td><td>436</td><td>468</td><td>-7%</td><td>470</td><td>527</td><td>-11%</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates

Table 4: Mobis: 2Q preview  
Wbn, %

<table><tr><td rowspan="2"></td><td colspan="3">2Q26</td><td rowspan="2">2Q25</td><td rowspan="2">% y/y</td><td rowspan="2">1Q26</td><td rowspan="2">% q/q</td></tr><tr><td>JPMe</td><td>BBG</td><td>Diff.</td></tr><tr><td>Revenue</td><td>17,490</td><td>17,087</td><td>2%</td><td>15,936</td><td>10%</td><td>15,561</td><td>12%</td></tr><tr><td>OP</td><td>901</td><td>922</td><td>-2%</td><td>870</td><td>4%</td><td>803</td><td>12%</td></tr><tr><td>OP margin</td><td>5.2%</td><td>5.4%</td><td></td><td>5.5%</td><td></td><td>5.2%</td><td></td></tr><tr><td>NP</td><td>1,136</td><td>1,093</td><td>4%</td><td>934</td><td>22%</td><td>883</td><td>29%</td></tr><tr><td>NP margin</td><td>6.5%</td><td>6.4%</td><td></td><td>5.9%</td><td></td><td>5.7%</td><td></td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates

## Table 5: Mando: 2Q preview

Wbn, %

<table><tr><td rowspan="2"></td><td colspan="3">2Q26</td><td rowspan="2">2Q25</td><td rowspan="2">% y/y</td><td rowspan="2">1Q26</td><td rowspan="2">% q/q</td></tr><tr><td>JPMe</td><td>BBG</td><td>Diff.</td></tr><tr><td>Revenue</td><td>2,536</td><td>2,492</td><td>2%</td><td>2,401</td><td>6%</td><td>2,312</td><td>10%</td></tr><tr><td>OP</td><td>104</td><td>104</td><td>0%</td><td>104</td><td>0%</td><td>94</td><td>11%</td></tr><tr><td>OP margin</td><td>4.1%</td><td>4.2%</td><td></td><td>4.3%</td><td></td><td>4.0%</td><td></td></tr><tr><td>NP</td><td>48</td><td>49</td><td>-4%</td><td>10</td><td>381%</td><td>53</td><td>-10%</td></tr><tr><td>NP margin</td><td>1.9%</td><td>2.0%</td><td></td><td>0.4%</td><td></td><td>2.3%</td><td></td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates

## ▲Overweight

Previous: Neutral
012330.KS, 012330 KS
Price (07 Jul 26):W489,000
Price Target (Dec-27):W710,000

Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC
(82-2) 758 5716
sonny.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Quarterly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (W)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>11,086</td><td>9,715A</td><td>12,722</td></tr><tr><td>Q2</td><td>10,158</td><td>12,523</td><td>14,296</td></tr><tr><td>Q3</td><td>10,125</td><td>12,934</td><td>14,824</td></tr><tr><td>Q4</td><td>8,408</td><td>10,683</td><td>13,084</td></tr><tr><td>FY</td><td>40,290</td><td>45,856</td><td>54,926</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>6</td><td>6</td><td>8</td><td>8</td><td>36</td></tr><tr><td>Growth</td><td>48</td><td>32</td><td>50</td><td>53</td><td>41</td></tr><tr><td>Momentum</td><td>44</td><td>53</td><td>37</td><td>33</td><td>71</td></tr><tr><td>Quality</td><td>31</td><td>16</td><td>33</td><td>38</td><td>31</td></tr><tr><td>Low Vol</td><td>32</td><td>14</td><td>16</td><td>17</td><td>63</td></tr><tr><td>ESGQ</td><td>22</td><td>99</td><td>100</td><td>13</td><td>9</td></tr></table>

## Hyundai Mobis

## Actuator upside now more “call option”; upgrade to Overweight

The share price of Hyundai Mobis (Mobis) has corrected 36% from its recent peak and the risk/reward now looks more attractive after a sharp pullback. We upgrade Mobis to Overweight from Neutral as the share price now largely reflects the core business, leaving robot actuators as incremental optionality rather than fully priced expectations.

\- Key investor feedback from our Asia marketing suggests Mobis is viewed as a "robot leverage" play: while investors largely agree that newly entering the actuator segment may not be highly profitable, the initiative could still act as a narrative catalyst, and some note the stock i

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 07 Jul 2026 09:03 PM HKT

Disseminated 07 Jul 2026 09:03 PM HKT
"""
