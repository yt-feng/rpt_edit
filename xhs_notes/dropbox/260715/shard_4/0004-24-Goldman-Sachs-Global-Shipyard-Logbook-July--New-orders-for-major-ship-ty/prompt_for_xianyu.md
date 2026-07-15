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
# Global Shipyard Logbook July: New orders for major ship types improved but declined for gas carriers; China's order market share reaches 85%

## Asia Transportation

Identifying imbalance and inflections across passenger and cargo transportation in Asia Explore >

![](images/874705d0612d733a6d7932d51237ccab1619d95ae4dfe7b60107ae7a41bc44b0.jpg)

Global new ship order volume showed some stabilization in Jun-26 (-9% MoM) and was up +1% YoY, while new order value was -39% MoM/-9% YoY. Around 70% of the MoM order value decline was attributable to lower offshore contracting, while the remainder was due to 60-70% MoM contraction of LPG and LNG carriers order volume, which we attribute to a slower new orders negotiation as the war increased uncertainty. Demand for other major ship types improved, with the aggregate of volume/value for containers, tankers and bulkers +22%/+14% MoM, and Chinese shipyards have dominant market share in these three ship types. As a result, together with faster capacity expansion vs. peers (see our trip takeaway), Chinese shipyards strengthened their market share to 85% in Jun-26.

Among our covered shipbuilders, Yangzijiang and Hengli's order momentum both improved in Jun-26. Yangzijiang Shipbuilding won four 1.9k-TEU containerships and 2 LPG orders during Jun-26, new-order win momentum improved vs. Apr-May, but still -24% below the 1Q26 avg; while Hengli's new order-wins volume saw more acceleration at +102% vs. the avg in Apr-May, as it won 16 x 6k containership in Jun-26, which accounts for half of its new orders volume. That said, the data hasn't incorporated up-to twenty 20k-TEU dual-fuel containerships placed by MSC to Hengli, which we estimate could be valued at US\$4bn (see Jul-26 report) and account for more than 10% of Hengli's orderbook, and will be delivered starting from 1H29. We believe this implies further improvement in Hengli's product mix (see Jul-26 report) and also more intense competition for Yangzijiang. We reiterate our view that Hengli will continue to win new orders, benefiting from shorter order cover years. We also remain constructive on Namura (7014.T; Buy) and Mitsui E&S (7003.T; Buy) which stand to benefit from resilient underlying demand for replacement of aging fleets, the structural shift to environmentally friendly vessels, and the revitalization of Japan's shipbuilding industry in the long run. Moreover, with Tokyo Keiki (7721.T; Buy) boasting a 60% global market share for autopilots and gyrocompasses in ships, we believe that this company has the potential to achieve substantial earnings growth as we expect both after-service

Herbert Lu
+852-2978-0726 | herbert.lu@gs.com
GS (Asia) L.L.C.

Simon Cheung, CFA
+852-2978-6102 |
simon.cheung@gs.com
GS (Asia) L.L.C.

Norihiro Miyazaki
+81(3)4587-9842 |
norihiro.miyazaki@gs.com
GS Japan Co., Ltd.

Wing Huang
+852-2978-0415 | ying.huang@gs.com
GS (Asia) L.L.C.

Ryohei Kurita
+81(3)4587-1799 |
ryohei.kurita@gs.com
GS Japan Co., Ltd.

demand and newbuild demand to increase over the next few years, in addition to tailwinds from defense.

By analyzing key data points, we summarize four main findings for Jun:

Value of global new ship contracts (excl. naval ships) slowed down MoM attributable to lower offshore contracting and LPG/LNGC orders - New contract volume/value were down $-9\% / -39\%$ MoM, and was $+1\% / -9\%$ YoY to 5.3mn CGTs/US\$15.3bn. As a result, the end-Jun orderbook slightly increased by $0.3\%$ MoM, which led to a MoM stable orderbook cover year of 3.7x. Clarksons newbuilding price trended higher MoM ( $+0.1\%$ ) to 185, driven by better pricing across all major ship types especially bulkers and tankers, up $+1.3\% / +0.4\%$ MoM respectively.

\- Containership order volumes declined by 13% MoM, of which all new orders were small-to-medium size below 7k TEU; Tanker order momentum improved +5% MoM and nearly doubled (+96%) YoY; and bulker orders were +166%/ flat MoM/YoY - Among the different ship types (Exhibit 6), containership volumes were at 1.2mn CGTs (-13%/-35% MoM/YoY), where all were small-to-mid size vessels (below 7k TEU) attributable to replacement demand. Tanker order volumes were +5%/+96% MoM/YoY. During the month, there were 21 new orders for VLCCs, of which 12/5/2 were placed to CSSC/Hanwha Ocean/Hengli (see Feb-26 report) and scheduled to be delivered starting from 2H28 to 2030. Besides the 2 VLCCs, Hengli also won orders for 2 product tankers and 2 Suezmax tankers in Jun-26, taking c.13% of global tanker orders market share.

China's overall market share improved to 85%, the highest since Aug-24; while Korea's market share declined to 9% in Jun-26 (vs. 40% in May-26). Excluding LNGC, China/Korea Jun-26 market shares were at 87%/7% respectively - In terms of CGTs (Exhibit 3), Chinese shipyards' Jun-26 market share incl./excl. LNGCs was 85%/87% (vs.52%/65% in May-26). China continued to dominate tanker and bulker new order volumes with a global share at 78%/89%. Korean shipyards' May-26 market share incl./excl. LNGCs was 9%/7% (vs.40%/25% in May-26), due to lower market share in LNGC/LPG/containerships (Exhibit 3).

Yangzijiang's orderbook cover years was at 3.4x, modestly below the global avg at 3.7x; while Hengli cover years was at 2.8x (after factoring in Phase III capacity), which could decline further if they expand capacity via phase IV - Yangzijiang's orderbook cover years was at 3.4x years in Jun-26, stable vs. May-26. We expect additional capacity at Hongyuan Shipyard by end-26 will support further order wins for YZJ. Hengli cover years was flattish at 3.2x years and was at 2.8x years considering an earlier completion of Phase III capacity (see Apr-26 report), which remains well below the global average. We expect Hengli cover years could be further shortened to below 2x, if the company finalizes Phase IV capacity addition, which is estimated to add another up to $100\%$ capacity to the existing three phases (see Jul-26). Hence, we expect it will continue to win orders, benefiting from shorter cover years.

Note: VLCC crude tanker earnings based on TCE of Inside Persian Gulf to China from 2017 to Feb'26 and based on VLCC-TCE (China) which is the average of TD15, TD22 and Outside Persian Gulf to China TCE since Mar'26"; and VLCC new building price (Long Run historical time series)

Exhibit 1: Global Shipbuilding key monthly data overview  
Global new contract value was -9% YoY was due to lower volume contribution from containerships and non-major shiptypes, partially offset by better volume from tankers while newbuild price was +0.1% MoM; Yangzijiang and Hengli were c.1%/15% of the global new order volumes

<table><tr><td></td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2025 Avg</td><td>2026 Avg</td><td>6M25 avg</td><td>6M26 avg</td></tr><tr><td>New contract order volume (mn CGT)</td><td>5.7</td><td>4.6</td><td>3.3</td><td>5.5</td><td>2.3</td><td>5.2</td><td>4.6</td><td>5.1</td><td>7.0</td><td>4.2</td><td>7.5</td><td>10.6</td><td>8.6</td><td>7.9</td><td>6.2</td><td>9.5</td><td>5.8</td><td>5.3</td><td>5.5</td><td>7.2</td><td>4.4</td><td>7.2</td></tr><tr><td>MoM%</td><td>13%</td><td>-19%</td><td>-30%</td><td>68%</td><td>-57%</td><td>123%</td><td>-12%</td><td>11%</td><td>37%</td><td>-41%</td><td>81%</td><td>41%</td><td>-19%</td><td>-8%</td><td>-21%</td><td>52%</td><td>-39%</td><td>-9%</td><td></td><td></td><td colspan="2">6M26 vs. 6M25</td></tr><tr><td>YoY%</td><td>-29%</td><td>-21%</td><td>-41%</td><td>-35%</td><td>-49%</td><td>-64%</td><td>-9%</td><td>-27%</td><td>4%</td><td>-16%</td><td>43%</td><td>109%</td><td>50%</td><td>70%</td><td>92%</td><td>73%</td><td>147%</td><td>1%</td><td></td><td>↑32%</td><td></td><td>↑62%</td></tr><tr><td>New contract value ($m)</td><td>14,580</td><td>15,061</td><td>9,578</td><td>18,018</td><td>8,537</td><td>16,721</td><td>13,731</td><td>12,831</td><td>19,380</td><td>13,977</td><td>23,939</td><td>33,414</td><td>24,803</td><td>22,465</td><td>16,725</td><td>28,335</td><td>25,067</td><td>15,288</td><td>16,647</td><td>22,114</td><td>13,749</td><td>22,114</td></tr><tr><td>MoM%</td><td>-9%</td><td>3%</td><td>-36%</td><td>88%</td><td>-53%</td><td>96%</td><td>-18%</td><td>-7%</td><td>51%</td><td>-28%</td><td>71%</td><td>40%</td><td>-26%</td><td>-9%</td><td>-26%</td><td>69%</td><td>-12%</td><td>-39%</td><td></td><td></td><td colspan="2">6M26 vs. 6M25</td></tr><tr><td>YoY%</td><td>-20%</td><td>-6%</td><td>-33%</td><td>-33%</td><td>-54%</td><td>-57%</td><td>-13%</td><td>-39%</td><td>5%</td><td>0%</td><td>50%</td><td>107%</td><td>70%</td><td>49%</td><td>75%</td><td>57%</td><td>194%</td><td>-9%</td><td></td><td>↑33%</td><td></td><td>↑61%</td></tr><tr><td>Clarksons newbuilding price index</td><td>189</td><td>188</td><td>187</td><td>187</td><td>187</td><td>187</td><td>187</td><td>186</td><td>186</td><td>185</td><td>184</td><td>185</td><td>184</td><td>182</td><td>182</td><td>183</td><td>185</td><td>185</td><td>187</td><td>184</td><td>188</td><td>184</td></tr><tr><td>MoM%</td><td>0.1%</td><td>-0.5%</td><td>-0.5%</td><td>-0.2%</td><td>-0.2%</td><td>0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.4%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>-0.2%</td><td>-1.2%</td><td>0.0%</td><td>0.7%</td><td>0.9%</td><td>0.1%</td><td></td><td></td><td colspan="2">6M26 vs. 6M25</td></tr><tr><td>YoY%</td><td>5%</td><td>4%</td><td>2%</td><td>2%</td><td>0%</td><td>0%</td><td>-1%</td><td>-2%</td><td>-2%</td><td>-3%</td><td>-3%</td><td>-2%</td><td>-3%</td><td>-3%</td><td>-3%</td><td>-2%</td><td>-1%</td><td>-1%</td><td></td><td>↓-2%</td><td></td><td>↓-2%</td></tr><tr><td>Orderbook (mn CGT), period end</td><td>170</td><td>173</td><td>172</td><td>174</td><td>173</td><td>174</td><td>174</td><td>176</td><td>178</td><td>178</td><td>182</td><td>189</td><td>192</td><td>197</td><td>199</td><td>204</td><td>207</td><td>207</td><td></td><td></td><td>172.5</td><td>201.2</td></tr><tr><td>MoM%</td><td>0%</td><td>1%</td><td>0%</td><td>1%</td><td>-1%</td><td>1%</td><td>0%</td><td>1%</td><td>1%</td><td>0%</td><td>2%</td><td>4%</td><td>2%</td><td>3%</td><td>1%</td><td>3%</td><td>1%</td><td>0%</td><td></td><td></td><td></td><td></td></tr><tr><td>Global forward cover years (x)</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.2x</td><td>3.2x</td><td>3.2x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.4x</td><td>3.5x</td><td>3.6x</td><td>3.6x</td><td>3.7x</td><td>3.7x</td><td>3.7x</td><td></td><td></td><td>3.3x</td><td>3.6x</td></tr><tr><td>MoM%</td><td>0%</td><td>1%</td><td>-1%</td><td>1%</td><td>-1%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>-1%</td><td>2%</td><td>3%</td><td>1%</td><td>2%</td><td>1%</td><td>2%</td><td>1%</td><td>0%</td><td></td><td></td><td></td><td></td></tr></table>

Source: Clarksons, Company data, GS Global Investment Research

## Exhibit 2: Dynamic ROI vs orderbook by ship type

Tanker has increased to 36% vs. 25% on Jun 12, 2026 prior to the reopening of the Strait of Hormuz, containerships profitability remains at 31%  
![](images/4ce50bb012c6d569b5de0ad3a07eff12ee9a8a0aa3a63c6455da6625deb79718.jpg)  
Note: Containership data using 9k TEU 6-12m TCE and 8.5-9.5k TEU newbuilding prices Data as of 03-Jul-2026

![](images/24375cbb257a9f2ee73911caed32f0a12724b6033b6dbb8f72bc1dbc45fca560.jpg)  
Note: MR product tanker data using BCTI spot TCE and 47-51k dwt newbuilding prices. Data as of 03-Jul-2026

![](images/d34ecdba6010d5ea4843027852fb434a5cf2ce21767ba86d4d4da48be70244cb.jpg)

![](images/b0fac726cee06b4ef73883514c21037dde8a1f380f78a6788bca7991675a161d.jpg)  
Note: Bulkers data using 170k dwt bulkcarrier 6M TCE and Capesize 180-182k dwt newbuilding prices.
Data as of 03-Jul-2026

![](images/c629a87e1139337487d3002f2a0bab5c97e1f91a4150b05b2f797f25670c03f4.jpg)  
Note: LPG data using 84k CBM LPG 12M TCE and 88-91k cbm LPGC newbuilding prices. Data as of 03-Jul-2026

![](images/dfd2b2b52bf4fd25cb7174cb4867809e8d45a24bf62648139a6621d147df4278.jpg)  
Note: LNG data using 174k CBM 3 year TCE and LNGC 174k cbm newbuilding prices Data as of 03-Jul-2026

Exhibit 3: Monthly orderbook cover years and market share

<table><tr><td></td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2025 Avg</td><td>2026 Avg</td><td>6M25 avg</td><td>6M26 avg</td></tr><tr><td colspan="23">Orderbook cover years (Period end)</td></tr><tr><td>Global</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.2x</td><td>3.2x</td><td>3.2x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.3x</td><td>3.4x</td><td>3.5x</td><td>3.6x</td><td>3.6x</td><td>3.7x</td><td>3.7x</td><td>3.7x</td><td>3.3x</td><td>3.6x</td><td>3.3x</td><td>3.6x</td></tr><tr><td>China</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.6x</td><td>3.7x</td><td>3.8x</td><td>3.9x</td><td>4.0x</td><td>4.1x</td><td>4.1x</td><td>4.1x</td><td>3.5x</td><td>4.0x</td><td>3.5x</td><td>4.0x</td></tr><tr><td>Korea</td><td>3.0x</td><td>3.0x</td><td>2.9x</td><td>3.0x</td><td>2.9x</td><td>2.9x</td><td>2.9x</td><td>2.8x</td><td>2.9x</td><td>2.8x</td><td>2.9x</td><td>3.0x</td><td>3.0x</td><td>3.0x</td><td>3.1x</td><td>3.1x</td><td>3.2x</td><td>3.2x</td><td>2.9x</td><td>3.1x</td><td>3.0x</td><td>3.1x</td></tr><tr><td>Japan</td><td>2.9x</td><td>2.8x</td><td>2.8x</td><td>2.8x</td><td>2.7x</td><td>2.8x</td><td>2.7x</td><td>2.7x</td><td>2.7x</td><td>2.6x</td><td>2.5x</td><td>2.6x</td><td>2.5x</td><td>2.5x</td><td>2.4x</td><td>2.3x</td><td>2.3x</td><td>2.2x</td><td>2.7x</td><td>2.3x</td><td>2.8x</td><td>2.3x</td></tr><tr><td colspan="23">Chinese shipbuilding companies orderbook cover years (Period end)</td></tr><tr><td>Yangzijiang Shipbuilding</td><td>3.7x</td><td>3.7x</td><td>3.6x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.6x</td><td>3.6x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.4x</td><td>3.5x</td><td>3.5x</td><td>3.5x</td><td>3.4x</td><td>3.4x</td><td>3.6x</td><td>3.4x</td><td>3.6x</td><td>3.4x</td></tr><tr><td>Hengli SB</td><td>1.5x</td><td>1.5x</td><td>1.5x</td><td>1.6x</td><td>1.6x</td><td>1.6x</td><td>1.8x</td><td>1.8x</td><td>1.8x</td><td>1.9x</td><td>2.2x</td><td>2.5x</td><td>2.6x</td><td>3.1x</td><td>3.2x</td><td>3.2x</td><td>3.2x</td><td>3.2x</td><td>1.8x</td><td>3.1x</td><td>1.6x</td><td>3.1x</td></tr><tr><td>New Times SB</td><td>3.9x</td><td>3.9x</td><td>3.8x</td><td>3.8x</td><td>3.7x</td><td>3.8x</td><td>3.7x</td><td>3.7x</td><td>3.6x</td><td>3.7x</td><td>3.7x</td><td>3.7x</td><td>3.7x</td><td>4.1x</td><td>4.0x</td><td>4.1x</td><td>4.1x</td><td>4.0x</td><td>3.8x</td><td>4.0x</td><td>3.8x</td><td>4.0x</td></tr><tr><td colspan="23">New contract volume market share by country (by CGT)</td></tr><tr><td>China</td><td>34%</td><td>68%</td><td>49%</td><td>61%</td><td>55%</td><td>62%</td><td>73%</td><td>71%</td><td>56%</td><td>74%</td><td>61%</td><td>70%</td><td>72%</td><td>80%</td><td>67%</td><td>72%</td><td>52%</td><td>85%</td><td>62%</td><td>72%</td><td>55%</td><td>72%</td></tr><tr><td>Korea</td><td>17%</td><td>9%</td><td>29%</td><td>24%</td><td>11%</td><td>22%</td><td>9%</td><td>13%</td><td>23%</td><td>12%</td><td>29%</td><td>16%</td><td>17%</td><td>11%</td><td>25%</td><td>14%</td><td>40%</td><td>9%</td><td>18%</td><td>18%</td><td>19%</td><td>18%</td></tr><tr><td>Japan</td><td>19%</td><td>4%</td><td>8%</td><td>5%</td><td>7%</td><td>14%</td><td>4%</td><td>2%</td><td>6%</td><td>4%</td><td>0%</td

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or

finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
