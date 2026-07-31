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

# Weichai Power - A/H

Positive read-throughs from BE, Innio, GE Vernova: SOFC, Gas Engines, BTM Demand; stay OW

We summarize in this note the latest read-throughs from Bloom Energy, Innio, and GE Vernova, focusing on SOFC, gas primary engines, gas engines, and BTM (behind-the-meter) power demand. Mark Strouse covers all three names with Overweight ratings, and his recent reviews of results and guidance remain constructive. All three companies reported robust Q2 orders and raised capacity or delivery guidance, with management teams consistently highlighting strong BTM and data center demand, persistent supply constraints, and multi-year order visibility. Despite recent market volatility and investor concerns about BTM overcapacity or potential AI/data center capex cuts, management commentary across the board points to order books that remain full, slot reservations stretching into the 2030s, and no evidence of a material oversupply or demand cliff. Pricing power and margin resilience are recurring themes, with all three companies signaling confidence in their ability to defend profitability even as the competitive landscape evolves.

Stock view: Weichai's latest management update and fireside chat reinforce the AIDC thesis and highlight margin resilience despite sector volatility. The company is tracking in line with its 2026 AIDC shipment guidance of 3,500–4,000 units, with a strong order pipeline and a back-half weighted ramp. Capacity expansion is on track, with AIDC-related engine capacity set to reach 8,000–10,000 units by end-2027, and SOFC ramping from 30MW in 2026 to 200MW in 2027. Following recent share price correction (H/A down c.19%/13% since May vs. MSCI China -5%), Weichai's valuation has turned compelling, trading once again as an industrial cyclical name with a c.4% yield. Notably, on July 21, 2026, Weichai's controlling shareholder, Weichai Group, announced plans to increase its holdings in the company's A-shares by up to Rmb400MM, which we see as a strong signal of confidence in the company's growth outlook and intrinsic value. We view the current reset as an opportunity, supported by resilient delivery, margin discipline, and a multi-year growth runway. Maintain OW on Weichai A/H.

## Bloom Energy's results reinforce the structural upcycle in SOFC and BTM, with robust order momentum and pricing power

\- Bloom Energy management highlighted that SOFC demand is accelerating, with customer visibility building into 2030 and order books expanding rapidly. The company is targeting utility and incremental machinery expansion, supporting the narrative that SOFC is poised for multi-year growth. This is highly relevant for Weichai's SOFC ambitions, as it suggests the global market is still in the early stages of a multi-year upcycle.

Infrastructure, Industrials & Transport

Karen Li, CFA AC
(852) 2800-8589
karen.yy.li@JPM.com

Mufan Shi
(852) 2800-8502
mufan.shi@JPM.com

Jenny Qiu, CFA
(852) 2800 8503
jenny.qiu@JPM.com

Sunny Su
(852) 2800 8551
sunny.su@JPM.com

Beatrice Lam
(852) 2800-8738
beatrice.lam@JPM.com

JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

000338.SZ, 000338 CH

Price: Rmb26.19

28 Jul 2026

Price Target: Rmb49.00

PT End Date: 30 Jun 2027

2338.HK, 2338 HK

Overweight

Price: HK\$30.92

28 Jul 2026

Price Target: HK\$52.00

See page 6 for analyst certification and important disclosures, including non-US analyst disclosures.

PT End Date: 30 Jun 2027

\- Data center orders are more than double of total FY25 orders, highlighting structural tailwinds for BTM power solutions. Management sees the total addressable market expanding, driven by AI/data center power shortages and the shift toward distributed generation.

\- Pricing power is evident, as management noted robust ASPs and margin resilience despite supply chain challenges. The competitive landscape is evolving, but Bloom's technology and delivery capability are seen as differentiators. The company is investing in capacity and expects demand to remain supply-constrained for several years, which is highly relevant for Weichai's SOFC and BTM ambitions.

## Innio's record orders and capacity ramp signal persistent strength in gas engines and BTM, with margin and TAM upside

\- Innio reported record 2Q order activity, especially in data center and BTM segments, with a book-to-bill of 6.3x for data centers and 2.0x for utility solutions. Capacity ramp plans to 5 GW by YE26 and 10 GW by 2030 signal accelerating demand and fully booked slot reservations into the 2030s. This supports the view that gas engine demand is not only strong but also likely to remain supply-constrained for several years.

\- Demand for gas engines is described as structurally strong, with distributed generation and BTM solutions seeing persistent tailwinds. Management expects supply constraints to persist, supporting pricing and margin power for high-quality suppliers. TAM is expanding, driven by electrification, grid constraints, and data center growth.

\- The competitive landscape remains dynamic, but Innio's established technology and service-driven business model are seen as key advantages. Management highlighted favorable margin mix, with FY26 PF EBITDA guidance above Street expectations. Management is confident of maintaining pricing power and expects continued order strength as the market re-rates distributed power solutions.

## GE Vernova's strong orders and capacity expansion highlight the durability of the power upcycle and BTM demand

\- GE Vernova reported strong 2Q orders of \$24.2B, well above expectations, and announced expansion to 20 GW of gas power capacity is complete, targeting 24 GW in FY28 and 30 GW by 2030. Data center orders are at record levels, underscoring structural demand for gas turbines and BTM solutions. This is a clear signal that the power sector is seeing sustained order strength, and that both gas engines and turbines are benefiting from the electrification trend and AI/data center power shortages.

\- The company highlighted positive margin outlook, with FY26 FCF guidance raised to \$11.5–12.5B, up from \$6.5–7.5B previously. Management expects continued order strength and capacity expansion to drive multi-year growth. Pricing power and supply constraints are persistent, with management noting robust ASPs and margin resilience.

\- The competitive landscape is intense, but GE Vernova's scale and diversification are seen as advantages. TAM is expanding, driven by electrification, AI/data center power shortages, and the shift toward distributed generation. Management is confident of maintaining pricing power and expects continued order strength as the market re-rates high-quality suppliers.

Table 1: AIDC power comparison table

<table><tr><td rowspan="2"></td><td rowspan="2">BBG Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Last Price LC</td><td rowspan="2">JPM PT LC</td><td rowspan="2">Upside/Downside</td><td rowspan="2">Mkt Cap US$Mn</td><td rowspan="2">YTD Stock perf.</td><td colspan="2">P/E (x)</td><td colspan="2">EPS growth Y/Y</td><td colspan="2">PEG</td><td colspan="2">ROE (%)</td><td colspan="2">P/B (x)</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Weichai Power-H</td><td>2338 HK</td><td>OW</td><td>31.24</td><td>52.00</td><td>66%</td><td>34,543</td><td>66%</td><td>15.0</td><td>13.2</td><td>22%</td><td>14%</td><td>0.7</td><td>0.9</td><td>15.9</td><td>16.6</td><td>2.3</td><td>2.1</td></tr><tr><td>Weichai Power-A</td><td>000338 CH</td><td>OW</td><td>27.10</td><td>49.00</td><td>81%</td><td>34,543</td><td>58%</td><td>15.1</td><td>13.2</td><td>22%</td><td>14%</td><td>0.7</td><td>1.0</td><td>15.9</td><td>16.6</td><td>2.3</td><td>2.1</td></tr><tr><td>Yingliu</td><td>603308 CH</td><td>OW</td><td>42.39</td><td>95.00</td><td>124%</td><td>4,251</td><td>2%</td><td>43.7</td><td>27.7</td><td>92%</td><td>58%</td><td>0.5</td><td>0.5</td><td>11.7</td><td>16.8</td><td>4.9</td><td>4.4</td></tr><tr><td>Techtronic</td><td>669 HK</td><td>OW</td><td>130.00</td><td>179.00</td><td>38%</td><td>30,295</td><td>45%</td><td>20.7</td><td>17.8</td><td>21%</td><td>16%</td><td>1.0</td><td>1.1</td><td>19.9</td><td>20.5</td><td>3.9</td><td>3.5</td></tr><tr><td>HD Hyundai Electric</td><td>267260 KS</td><td>OW</td><td>549000</td><td>1375000</td><td>150%</td><td>13,738</td><td>30%</td><td>19.7</td><td>15.0</td><td>41%</td><td>31%</td><td>0.5</td><td>0.5</td><td>42.7</td><td>42.3</td><td>7.4</td><td>5.6</td></tr><tr><td>Hyosung Heavy Industr</td><td>298040 KS</td><td>OW</td><td>1926000</td><td>4100000</td><td>113%</td><td>12,444</td><td>8%</td><td>22.6</td><td>15.8</td><td>53%</td><td>43%</td><td>0.4</td><td>0.4</td><td>29.2</td><td>31.6</td><td>5.8</td><td>4.4</td></tr><tr><td colspan="18">Gas/diesel engine manufacturers and OEMs</td></tr><tr><td>Caterpillar</td><td>CAT US</td><td>OW</td><td>840.85</td><td>1165.00</td><td>39%</td><td>387,289</td><td>47%</td><td>33.5</td><td>27.6</td><td>34%</td><td>21%</td><td>1.0</td><td>1.3</td><td>97.3</td><td>173.1</td><td>62.6</td><td>39.2</td></tr><tr><td>Cummins</td><td>CMI US</td><td>N</td><td>641.60</td><td>725.00</td><td>13%</td><td>88,534</td><td>26%</td><td>21.9</td><td>19.7</td><td>27%</td><td>11%</td><td>0.8</td><td>1.7</td><td>30.4</td><td>28.5</td><td>6.1</td><td>5.1</td></tr><tr><td>Generac</td><td>GNRC US</td><td>OW</td><td>195.60</td><td>267.00</td><td>37%</td><td>11,515</td><td>43%</td><td>22.1</td><td>20.6</td><td>40%</td><td>7%</td><td>0.6</td><td>2.8</td><td>18.8</td><td>17.8</td><td>3.9</td><td>3.4</td></tr><tr><td>Wartsila</td><td>WRT 1V FH</td><td>N</td><td>29.45</td><td>30.60</td><td>4%</td><td>19,871</td><td>-2%</td><td>27.3</td><td>25.4</td><td>16%</td><td>7%</td><td>1.7</td><td>3.4</td><td>20.7</td><td>21.6</td><td>6.1</td><td>5.4</td></tr><tr><td>China Yuchai Intematic</td><td>CYD US</td><td>NC</td><td>46.43</td><td>NA</td><td>NA</td><td>1,742</td><td>31%</td><td>13.7</td><td>11.6</td><td>40%</td><td>18%</td><td>0.3</td><td>0.6</td><td>8.4</td><td>9.4</td><td>1.2</td><td>1.1</td></tr><tr><td>Weichai Heavy Machine</td><td>000880 CH</td><td>NC</td><td>20.92</td><td>NA</td><td>NA</td><td>1,433</td><td>23%</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Shanghai New Power AI</td><td>600841 CH</td><td>NC</td><td>5.55</td><td>NA</td><td>NA</td><td>950</td><td>-9%</td><td>21.8</td><td>10.8</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>5.0</td><td>10.0</td><td>1.1</td><td>1.1</td></tr><tr><td>Tellhow Sci-Tech</td><td>600590 CH</td><td>NC</td><td>7.73</td><td>NA</td><td>NA</td><td>974</td><td>18%</td><td>18.2</td><td>13.0</td><td>NA</td><td>40%</td><td>NA</td><td>0.3</td><td>10.0</td><td>12.9</td><td>1.9</td><td>1.6</td></tr><tr><td>Shanghai Cooltech</td><td>300153 CH</td><td>NC</td><td>19.43</td><td>NA</td><td>NA</td><td>918</td><td>33%</td><td>41.3</td><td>25.2</td><td>45%</td><td>64%</td><td>NA</td><td>0.4</td><td>15.0</td><td>21.8</td><td>6.2</td><td>5.5</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>25.0</td><td>19.2</td><td>19%</td><td>24%</td><td>0.9</td><td>1.5</td><td>25.7</td><td>36.9</td><td>11.1</td><td>7.8</td></tr><tr><td colspan="18">Turbine Components/OEM</td></tr><tr><td>Howmet</td><td>HWM US</td><td>OW</td><td>286.04</td><td>310.00</td><td>8%</td><td>114,447</td><td>40%</td><td>56.6</td><td>48.3</td><td>37%</td><td>17%</td><td>1.5</td><td>2.8</td><td>34.3</td><td>34.7</td><td>NA</td><td>NA</td></tr><tr><td>GE Vernova</td><td>GEV US</td><td>OW</td><td>943.38</td><td>1330.00</td><td>41%</td><td>251,254</td><td>44%</td><td>27.9</td><td>34.2</td><td>386%</td><td>-19%</td><td>0.1</td><td>-1.8</td><td>60.0</td><td>37.6</td><td>17.2</td><td>12.1</td></tr><tr><td>Siemens Energy</td><td>ENR GY</td><td>OW</td><td>137.90</td><td>235.00</td><td>70%</td><td>135,406</td><td>15%</td><td>28.0</td><td>21.2</td><td>204%</td><td>32%</td><td>0.1</td><td>0.7</td><td>34.4</td><td>33.9</td><td>8.3</td><td>6.3</td></tr><tr><td>Mitsubishi Heavy Indus</td><td>7011 JP</td><td>NC</td><td>3733.00</td><td>NA</td><td>NA</td><td>77,107</td><td>-3%</td><td>43.9</td><td>30.5</td><td>6%</td><td>44%</td><td>7.4</td><td>0.7</td><td>11.6</td><td>12.6</td><td>4.8</td><td>3.7</td></tr><tr><td>Baker Hughes</td><td>BKR US</td><td>OW</td><td>58.46</td><td>74.00</td><td>27%</td><td>58,032</td><td>28%</td><td>24.8</td><td>22.0</td><td>-5%</td><td>13%</td><td>-5.1</td><td>1.7</td><td>11.4</td><td>11.5</td><td>2.6</td><td>2.5</td></tr><tr><td>Doosan Enerbility</td><td>034020 KS</td><td>OW</td><td>57900.00</td><td>130000.00</td><td>125%</td><td>25,655</td><td>24%</td><td>92.2</td><td>55.3</td><td>NA</td><td>67%</td><td>NA</td><td>0.8</td><td>5.0</td><td>7.9</td><td>4.5</td><td>4.2</td></tr><tr><td>Caterpillar</td><td>CAT US</td><td>OW</td><td>840.85</td><td>1165.00</td><td>39%</td><td>387,289</td><td>47%</td><td>33.5</td><td>27.6</td><td>34%</td><td>21%</td><td>1.0</td><td>1.3</td><td>97.3</td><td>173.1</td><td>62.6</td><td>39.2</td></tr><tr><td>Yantai Jereh</td><td>002353 CH</td><td>OW</td><td>136.97</td><td>162.00</td><td>18%</td><td>20,711</td><td>93%</td><td>40.4</td><td>27.4</td><td>14%</td><td>47%</td><td>2.9</td><td>0.6</td><td>14.1</td><td>14.5</td><td>5.2</td><td>4.4</td></tr><tr><td>Dongfang Electric</td><td>1072 HK</td><td>NC</td><td>21.20</td><td>NA</td><td>NA</td><td>12,487</td><td>15%</td><td>13.2</td><td>10.7</td><td>21%</td><td>23%</td><td>0.6</td><td>0.5</td><td>10.5</td><td>11.7</td><td>1.3</td><td>1.2</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>38.0</td><td>28.6</td><td>94%</td><td>28%</td><td>1.0</td><td>0.6</td><td>30.5</td><td>37.8</td><td>13.3</td><td>9.2</td></tr><tr><td colspan="18">SOFC</td></tr><tr><td>Bloom Energy</td><td>BE US</td><td>OW</td><td>166.84</td><td>314.00</td><td>88%</td><td>49,139</td><td>92%</td><td>60.7</td><td>30.0</td><td>588%</td><td>103%</td><td>0.1</td><td>0.3</td><td>64.9</td><td>75.7</td><td>25.4</td><td>14.0</td></tr><tr><td>Ceres Power</td><td>CWR LN</td><td>NC</td><td>316.80</td><td>NA</td><td>NA</td><td>901</td><td>49%</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>-3.8</td><td>0.5</td><td>5.7</td><td>5.2</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>60.7</td><td>30.0</td><td>588%</td><td>103%</td><td>0.1</td><td>0.3</td><td>30.5</td><td>38.1</td><td>15.6</td><td>9.6</td></tr></table>

Source: Bloomberg Finance L.P. Data as of intra-day 29 Jul 2026. JPM estimates. Consensus estimates for not covered (NC) companies, JPM estimates for all others. Note: For Japanese companies, next FY figures taken because FY ends in March. Past results are not an indicator of future performance.

Table 2: Machinery sector comparison table

<table><tr><td rowspan="2"></td><td rowspan="2">BBG Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Last Price LC</td><td rowspan="2">JPM PT LC</td><td rowspan="2">Upside/Downside</td><td rowspan="2">Mkt Cap US$Mn</td><td rowspan="2">YTD Stock perf.</td><td colspan="2">P/E (x)</td><td colspan="2">EV/EBITDA</td><td colspan="2">Dividend yield</td><td colspan="2">ROE (%)</td><td colspan="2">P/B (x)</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Weichai Power-H

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
