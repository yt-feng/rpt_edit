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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Global EV & Battery Update

## June 2026: EV/PHEV growth robust in EU, moderating in China, US stays tepid; ESS remains the sweet spot

EV+PHEV penetration trends by region. June EU-5+US+China EV/PHEV momentum remained resilient, with sales at 1.4mn units (+10% y/y, -2% m/m) and penetration at 36% (+2%pts y/y, +2%pts m/m). EU-5 continued to drive penetration gains, China's penetration rose despite soft PV sales, while the US remained muted.

\- EU-5. June EV/PHEV sales volume grew 49% y/y and penetration reached 34% (+8%pts y/y, +2%pts m/m) with strength across all regions. EU-5 penetration continues to rise: France (+12%pts), followed by Germany (+11%pts), Italy (+8%pts), UK (+7%pts), Spain (+2%pts), supported by country-level subsidy schemes and affordable mass EVs penetrating the market. Our EU auto team forecasts Chinese OEMs' market share in Europe will rise to \~20% from \~12% currently, with localization continuing and Spain seen as a key hub for further regional production localization (link).

\- US. June EV/PHEV sales volume fell 26% y/y with penetration at 7% (-3%pts y/y, -1%pts m/m), continuing to print y/y declines. By OEM, M/S remained broadly muted m/m: Tesla (#1) followed by GM (#2), HMG (#3), Toyota (#4) and Rivian (#5). EVs declined more meaningfully m/m than the broader industry, suggesting that stabilizing gas prices triggered by the US-Iran peace talks may be prompting some consumers to shift back towards ICE.

\- China. CPCA June NEV retail sales volume came in at 1mn units (-9% y/y, +6% m/m), with collective penetration at 63% (+10%pts y/y, flat m/m) out of a total of 1.6mn PV sales. While overall PV sales continue to fall, NEV sales held up relatively better. The Chinese government has launched the rural NEV subsidy program, but our China auto team sees it as more of a “mix + replacement” stabilizer than a true demand turnaround, given weak PV demand and subdued consumer confidence. JPM’s 2026 China PV demand forecast remains at -15% y/y, with a gradual recovery expected in 2H26 (link).

EV index performance. Over the past month, Asian EV supply chain stocks have traded soft, with Korea (-12%) and China (-8%) underperforming, while Japan outperformed (+8%). By subsector, cathodes (-13%) lagged the most, followed by battery foil (-11%), anodes (-6%), cell makers (-3%), and separators (-2%), while electrolytes outperformed (+1%).

Implications of the US FERC's policy for ESS. Rising social pushback over data center buildouts and electricity bill impacts has likely catalyzed the US FERC's grid queue reform, which highlights BTM (behind-the-meter) solutions as one potential path. Expert feedback suggests it is increasingly becoming a standard component of data center on-site microgrids, working alongside gas turbines and fuel cells to improve efficiency and resilience (link). More importantly, FERC has issued orders that could compress data center power-approval timelines from years to \~90 days, particularly when paired with ESS via curtailable transmission service, effectively incentivizing ESS attachment. We therefore raise our 2030 US ESS demand forecast by 52% to 303 GWh, with data centers comprising \~45% of total demand by 2030 (link).

Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC
(82-2) 758 5716
sonny.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Seri Yoon
(82-2) 758 5704
seri.yoon@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Asia Autos & EV Battery

(852) 2800-8505
rebecca.y.wen@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Asia Energy & Chemicals / EV Battery

Parsley Ong
(65) 6882-8578
parsley.rh.ong@JPM.com
JPM Securities Singapore Private Limited/
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

European Autos

Jose M Asumendi
(44-20) 7742-5315
jose.m.asumendi@JPM.com
JPM Securities plc

See page 10 for analyst certification and important disclosures, including non-US analyst disclosures.

LGES 2Q OP was a slight miss vs BBGe, with limited OEM compensation and weaker-than-expected AMPC, suggesting ESS production bottlenecks persisted. That said, channel checks indicate LGES has onboarded a second company to help with ESS packs, which should ease most bottlenecks by 3Q26. LGES continues to guide for a 3Q restart of the Ultium plant (offline in 1H26). At the July 30 earnings conf call, we expect updates on US EV battery ramp, OEM compensation, ESS ramp, and order backlog (link).

Ecopro BM announced a W1.2tn rights issue on June 30 via 9.9mn new shares. Proceeds are to be used mainly for a \~20% stake in Indonesia's BNSI nickel smelter (W765bn), with the balance for Hungary funding (W150bn), etc. We view deeper nickel upstream integration as adding incremental risks: 1) reduced flexibility toward LFP opportunities; 2) higher sensitivity to nickel price swings; and 3) policy risk from Indonesian controls (link).

Stock recommendations and potential future catalysts. Europe continues to print strong EV growth and China's NEV penetration is rising despite soft PV sales, while the US remains subdued. Global ESS battery demand decelerated m/m due to capacity constraints but remains robust y/y, with China still the largest demand driver. In the US, ESS battery sourcing is shifting rapidly away from Chinese suppliers towards Korean players: KR/JP shipments surged $>200\%$ y/y, while Chinese suppliers' ESS shipments to the US fell 40% y/y in May. 2Q earnings season begins this month, and we focus on the improving earnings trajectory. Near-term catalysts would be battery makers' smooth ramp-up of ESS capacity that translates into earnings, while longer-term catalysts center on persistent AI data center orders for ESS.

Stock positioning. In Korea, we like auto OEMs (Hyundai Motor, Kia) on resilient auto earnings driven by increasing HEV mix. Within the Korea battery supply chain, we prefer battery makers (LGES/SDI OW) over materials (LG Chem/L&F OW; EBM N; PFM UW) and lithium producers (POSCO, N), reflecting relative bargaining power and execution capability (LGES, LG Chem covered by Parsley Ong). In China, we like BYD-A/H (covered by Nick Lai) for its strong execution on global expansion along with overseas production ramp-up; and CATL-A/H (covered by Rebecca Wen) given its technology and leadership position in the global EV and ESS battery market.

Table 1: June 2026 PV+EV+PHEV monthly and YTD sales and penetration trends (by region)

<table><tr><td>Global PV Sales (&#x27;000s)</td><td>Jun-26</td><td>Jun-25</td><td>y/y%</td><td>6M26</td><td>6M25</td><td>y/y%</td></tr><tr><td colspan="7">Passenger Vehicles (PV)</td></tr><tr><td>Europe (EU5)</td><td>973</td><td>868</td><td>12.1%</td><td>5,066</td><td>4,752</td><td>6.6%</td></tr><tr><td>Germany</td><td>296</td><td>256</td><td>15.7%</td><td>1,484</td><td>1,403</td><td>5.8%</td></tr><tr><td>France</td><td>189</td><td>170</td><td>11.4%</td><td>857</td><td>842</td><td>1.8%</td></tr><tr><td>Italy</td><td>146</td><td>132</td><td>10.8%</td><td>938</td><td>855</td><td>9.8%</td></tr><tr><td>Spain</td><td>128</td><td>119</td><td>7.8%</td><td>648</td><td>610</td><td>6.2%</td></tr><tr><td>United Kingdom</td><td>213</td><td>191</td><td>11.4%</td><td>1,138</td><td>1,042</td><td>9.2%</td></tr><tr><td>China</td><td>1,602</td><td>2,085</td><td>-23.2%</td><td>8,721</td><td>10,895</td><td>-20.0%</td></tr><tr><td>US</td><td>1,379</td><td>1,280</td><td>7.7%</td><td>7,954</td><td>8,181</td><td>-2.8%</td></tr><tr><td>Total</td><td>3,954</td><td>4,233</td><td>-6.6%</td><td>21,740</td><td>23,828</td><td>-8.8%</td></tr><tr><td colspan="7">Battery Electric Vehicles (EV)</td></tr><tr><td>Europe (EU5)</td><td>233</td><td>143</td><td>63.1%</td><td>1,037</td><td>713</td><td>45.4%</td></tr><tr><td>Germany</td><td>84</td><td>47</td><td>78.2%</td><td>368</td><td>249</td><td>47.9%</td></tr><tr><td>France</td><td>56</td><td>29</td><td>91.7%</td><td>242</td><td>149</td><td>62.5%</td></tr><tr><td>Italy</td><td>15</td><td>8</td><td>88.3%</td><td>80</td><td>45</td><td>77.8%</td></tr><tr><td>Spain</td><td>14</td><td>11</td><td>26.5%</td><td>63</td><td>46</td><td>36.6%</td></tr><tr><td>United Kingdom</td><td>64</td><td>47</td><td>35.0%</td><td>285</td><td>225</td><td>26.6%</td></tr><tr><td>China</td><td>685</td><td>661</td><td>3.6%</td><td>3,106</td><td>3,336</td><td>-6.9%</td></tr><tr><td>US</td><td>73</td><td>101</td><td>-27.6%</td><td>458</td><td>616</td><td>-25.7%</td></tr><tr><td>Total</td><td>991</td><td>905</td><td>9.6%</td><td>4,601</td><td>4,665</td><td>-1.4%</td></tr><tr><td colspan="7">Plug-in Hybrid Vehicles (PHEV)</td></tr><tr><td>Europe (EU5)</td><td>102</td><td>82</td><td>25.2%</td><td>516</td><td>394</td><td>31.1%</td></tr><tr><td>Germany</td><td>32</td><td>26</td><td>25.8%</td><td>164</td><td>139</td><td>17.8%</td></tr><tr><td>France</td><td>12</td><td>12</td><td>4.4%</td><td>42</td><td>49</td><td>-15.4%</td></tr><tr><td>Italy</td><td>16</td><td>10</td><td>64.6%</td><td>85</td><td>43</td><td>98.6%</td></tr><tr><td>Spain</td><td>16</td><td>14</td><td>15.0%</td><td>78</td><td>56</td><td>39.2%</td></tr><tr><td>United Kingdom</td><td>27</td><td>21</td><td>24.9%</td><td>148</td><td>107</td><td>38.4%</td></tr><tr><td>China</td><td>323</td><td>450</td><td>-28.2%</td><td>1,614</td><td>2,128</td><td>-24.2%</td></tr><tr><td>US</td><td>18</td><td>21</td><td>-15.9%</td><td>86</td><td>175</td><td>-51.1%</td></tr><tr><td>Total</td><td>443</td><td>553</td><td>-19.8%</td><td>2,216</td><td>2,697</td><td>-17.8%</td></tr></table>

Source: CNEV Post, Motor Intelligence, European Union

<table><tr><td>Global EV/PHEV Penetration (%)</td><td>Jun-26</td><td>Jun-25</td><td>y/y%</td><td>6M26</td><td>6M25</td><td>y/y%</td></tr><tr><td colspan="7">EV/PHEV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>34.5%</td><td>25.9%</td><td>8.6%p</td><td>30.7%</td><td>23.3%</td><td>7.4%p</td></tr><tr><td>Germany</td><td>39.2%</td><td>28.4%</td><td>10.8%p</td><td>35.8%</td><td>27.6%</td><td>8.2%p</td></tr><tr><td>France</td><td>36.1%</td><td>24.1%</td><td>12.0%p</td><td>33.0%</td><td>23.5%</td><td>9.5%p</td></tr><tr><td>Italy</td><td>20.9%</td><td>13.2%</td><td>7.7%p</td><td>17.5%</td><td>10.2%</td><td>7.3%p</td></tr><tr><td>Spain</td><td>23.2%</td><td>20.8%</td><td>2.4%p</td><td>21.8%</td><td>16.8%</td><td>5.0%p</td></tr><tr><td>United Kingdom</td><td>42.5%</td><td>35.9%</td><td>6.6%p</td><td>38.0%</td><td>31.8%</td><td>6.2%p</td></tr><tr><td>China</td><td>62.9%</td><td>53.3%</td><td>9.6%p</td><td>54.1%</td><td>50.1%</td><td>4.0%p</td></tr><tr><td>US</td><td>6.6%</td><td>9.5%</td><td>-2.9%p</td><td>6.8%</td><td>9.7%</td><td>-2.8%p</td></tr><tr><td>Total</td><td>36.3%</td><td>34.4%</td><td>1.8%p</td><td>31.4%</td><td>30.9%</td><td>0.5%p</td></tr><tr><td colspan="7"></td></tr><tr><td colspan="7">EV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>23.9%</td><td>16.4%</td><td>7.5%p</td><td>20.5%</td><td>15.0%</td><td>5.5%p</td></tr><tr><td>Germany</td><td>28.4%</td><td>18.4%</td><td>10.0%p</td><td>24.8%</td><td>17.7%</td><td>7.1%p</td></tr><tr><td>France</td><td>29.6%</td><td>17.2%</td><td>12.4%p</td><td>28.2%</td><td>17.6%</td><td>10.5%p</td></tr><tr><td>Italy</td><td>10.2%</td><td>6.0%</td><td>4.2%p</td><td>8.5%</td><td>5.2%</td><td>3.2%p</td></tr><tr><td>Spain</td><td>11.1%</td><td>9.4%</td><td>1.6%p</td><td>9.8%</td><td>7.6%</td><td>2.2%p</td></tr><tr><td>United Kingdom</td><td>30.0%</td><td>24.8%</td><td>5.2%p</td><td>25.0%</td><td>21.6%</td><td>3.4%p</td></tr><tr><td>China</td><td>42.8%</td><td>31.7%</td><td>11.1%p</td><td>35.6%</td><td>30.6%</td><td>5.0%p</td></tr><tr><td>US</td><td>5.3%</td><td>7.9%</td><td>-2.6%p</td><td>5.8%</td><td>7.5%</td><td>-1.8%p</td></tr><tr><td>Total</td><td>25.1%</td><td>21.4%</td><td>3.7%p</td><td>21.2%</td><td>19.6%</td><td>1.6%p</td></tr><tr><td colspan="7"></td></tr><tr><td colspan="7">PHEV Penetration (%)</td></tr><tr><td>Europe (EU5)</td><td>10.5%</td><td>9.4%</td><td>1.1%p</td><td>10.2%</td><td>8.3%</td><td>1.9%p</td></tr><tr><td>Germany</td><td>10.9%</td><td>10.0%</td><td>0.9%p</td><td>11.0%</td><td>9.9%</td><td>1.1%p</td></tr><tr><td>France</td><td>6.5%</td><td>7.0%</td><td>-0.4%p</td><td>4.8%</td><td>5.8%</td><td>-1.0%p</td></tr><tr><td>Italy</td><td>10.7%</td><td>7.2%</td><td>3.5%p</td><td>9.1%</td><td>5.0%</td><td>4.0%p</td></tr><tr><td>Spain</td><td>12.1%</td><td>11.4%</td><td>0.8%p</td><td>12.0%</td><td>9.2%</td><td>2.9%p</td></tr><tr><td>United Kingdom</td><td>12.5%</td><td>11.2%</td><td>1.4%p</td><td>13.0%</td><td>10.3%</td><td>2.7%p</td></tr><tr><td>China</td><td>20.2%</td><td>21.6%</td><td>-1.4%p</td><td>18.5%</td><td>19.5%</td><td>-1.0%p</td></tr><tr><td>US</td><td>1.3%</td><td>1.6%</td><td>-0.4%p</td><td>1.1%</td><td>2.1%</td><td>-1.1%p</td></tr><tr><td>Total</td><td>11.2%</td><td>13.1%</td><td>-1.9%p</td><td>10.2%</td><td>11.3%</td><td>-1.1%p</td></tr></table>

Note: China data are based on preliminary CPCA retail sales data.  
GWh, %

Figure 1: Global EV battery installations by company vs KOR battery cell market share

![](images/aaa27a1988c78ba4af24baf777bab96354467af0c7a0bab0590e5732d592fb3f.jpg)  
Source: SNE Research.

Figure 2: Global EV battery installation market share trend by company %  
![](images/a64311244639b3a7d64779862870bd22513f0e4411e48149c6743caf836a8fc1.jpg)  
Source: SNE Research.

Figure 3: EU10 + US + China EV/PHEV sales and penetration trend
Units in 000s, %  
![](images/9d2a2cc6f0c6366b256ef8b9be6bec5813eb8ff2c13624df996fd060148adb49.jpg)  
Source: CNEV Post, Motor Intelligence, European Union

Figure 4: EU10 + US + China EV sales and penetration trend
Units in 000s, %  
![](images/786ae79a0073c91ecb04244aa5ea496182955975363ed04ff61e51b279cf6d21.jpg)  
Source: CNEV Post, Motor Intelligence, European Union

Figure 5: EU-5+US+China EV/PHEV sales mix trend
Units mn, %  
![](images/aba014a28f2a87c3210e28124fe5c69772d6112df41a379525ad12be699e1734.jpg)  
Source: CNEV Post, Motor Intelligence, European Union

Figure 6: US EV/PHEV penetration trend %  
![](images/fbc06c6baee4f3d941b12081f27f8e97dbadf3dc3526e6eeba964c77bfa9d7b5.jpg)

Figure 7: EU-5 EV/PHEV penetration trend  
![](images/25b97ab03dece6eee0bbefafd61c957c6da7432074952a39a81cc07685eb75e2.jpg)  
Source: European Union  
Source: Motor Intelligence

Figure 8: China EV/PHEV penetration trend  
![](images/c79be681ce1382b63bb5b58c416318cb7b8f525c3879f72739be24cfe99154db.jpg)  
Source: CNEV Post

Units, %, %p

Table 2: US/Germany: June 2026 EV monthly and YTD sales and market share trends (by OEM)

<table><tr><td>Global EV Sales by OEM (units)</td><td>Jun-26</td><td>Jun-25</td><td>y/y%</td><td>6M26</td><td>6M25</td><td>y/y%</td></tr><tr><td colspan="7">US</td></tr><tr><td>Tesla</td><td>36,642</td><td>45,628</td><td>-20%</td><td>234,670</td><td>274,638</td><td>-15%</td></tr><tr><td>GM</td><td>9,077</td><td>15,337</td><td>-41%</td><td>56,679</td><td>78,195</td><td>-28%</td></tr><tr><td>Toyota</td><td>4,845</td><td>1,986</td><td>144%</td><td>29,656</td><td>13,028</td><td>128%</td></tr><tr><td>HMC</td><td>3,394</td><td>5,117</td><td>-34%</td><td>27,466</td><td>30,859</td><td>-11%</td></tr><tr><td>Ford</td><td>2,322</td><td>4,856</td><td>-52%</td><td>16,606</td><td>38,988</td><td>-57%</td></tr><tr><td>Others</td><td>2,294</td><td>2,071</td><td>11%</td><td>9,398</td><td>16,449</td><td>-43%</td></tr><tr><td>Rivian</td><td>2,290</td><td>3,303</td><td>-31%</td><td>13,801</td><td>15,131</td><td>-9%</td></tr><tr><td>Kia</td><td>2,226</td><td>2,074</td><td>7%</td><td>12,731</td><td>13,674</td><td>-7%</td></tr><tr><td>

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results.

Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
