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
# China Electrical Equipment

Pinggao Winning the Most Orders from State Grid 2nd Batch of Equipment Purchase for Building UHV Lines in 2026

## CITI'S TAKE

State Grid (link) announced the bidding results of its 2nd batch of equipment procurement for construction of ultra-high voltage ('UHV') lines total Rmb9.4bn today. These bidding results are important since the amount of Rmb9.4bn was more than double of Rmb4bn in the 1st batch in 2026 and equal to 42.6% of total Rmb22.1bn in the five batches of 2025. The biggest winners this time were (i) Pinggao (600312 CH, BUY) winning Rmb2.092bn or 22.3% of the new orders; (ii) China XD Electric (601179 CH, not covered) winning Rmb1.899bn or 20.2%; (iii) TBEA (600089 CH, BUY) winning Rmb473m or 5.0%; (iv) Sieyuan Electric (002028 CH, BUY) winning Rmb196m or 2,1%; and (iv) NARI (600406 CH, BUY) winning Rmb144m or 1.5%. In PRC power grid equipment sector, our top picks are Sieyuan for fast export growth (>80% yoy), Pinggao for getting the most PRC UHV orders and TBEA for inexpensive valuations.

Total 79 entities winning contracts this time – In term of products in this batch total Rmb9.4bn, these comprised (i) Rmb5.4bn or 57.4% for 1,000kV gas insulated switch-gears ('GIS'), (ii) Rmb1.184m or 12.6% for raw materials; and (iii) Rmb655m or 7.0% for 1,000kV reactors. 79 companies won contracts this round, equal to an average Rmb119m per company. The three biggest winners were (i) Henan Pinggao Electric Co Ltd winning Rmb1.94bn or 20.6% total orders; (ii) Xian Xidian Switchgear Electric Co Ltd (unlisted) owned by China XD Electric winning Rmb1.45bn or 15.4% total orders and (iii) Shandong Electric Hitachi High-Voltage Switch-gear Co Ltd (not listed) winning Rmb1.41bn or 15.0% total orders.

Fast growing PRC power grid capex so far this year – PRC power grid capex surged 40% yoy to Rmb167.5bn in 1Q26; the capex comprises three categories; namely, civil works, equipment procurement and others (such as project design works). NARI explained that the biggest part of PRC power grid capex increment in 1Q26 came from civil works as PRC government was keen on having PRC FAI resuming positive numbers. The goal was achieved and PRC FAI improved from -3.9% yoy in 2025 to +1.7% yoy in 1Q26. Spending in civil works could boost the FAI faster than from other aspects as the former is often incurred at earlier stages. NARI expects the fast growth trend to persist in 2Q26E.

Pinggao expecting more UHV line equipment tendering in 2026E — Pinggao's new orders were +12% yoy to Rmb13.9bn in 2025. It expects more equipment tendering for construction of UHV lines in 2026E, comprising 3 AC projects (namely Dalate-Mengxi, Panzhihua-Xichang, and Zhejiang Ring Network) approved in 2025 and pending equipment tendering ahead as well as possibly at least another 2 AC projects to be approved in 2026E, up from only 3 in 2025. Tendering value of the first batch of State Grid's power grid equipment announced on 31 March 2026 were Rmb9,834m,

Pierre Lau, CFA $^{AC}$

+852-2501-2716

pierre.lau@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

comprising Rmb647m won by Pinggao which ranked No. 2 among all companies participating in the biddings. Pinggao guided that the tendering prices might be higher from the second batch ahead to reflect increased copper prices.

Pinggao's rising delivery of high voltage switchgears in 2026E — Pinggao's gas insulated switchgears (GIS) delivery should rise to 15 knots (+36% yoy) of 1,100kV units (7 knots for Aba, 4 for Yantai-Weihai, 2 knots for Caozhou project, and 2 knots for power plants) and >100 knots (+7.5% yoy) of 750kV units in 2026E, up from 11 and 93, respectively, in 2025. Its orders on hand were Rmb12.6bn by end 2025, comprising Rmb11.3bn for high-voltage projects, Rmb1.2bn for distribution equipment, and Rmb100m for international projects, with the latter figure adjusted after the cancellation of previous high-risk contracts. The orders on hand comprised high-voltage GIS of 34 knots for 1100kV (including Yantai-Weihai, Datong, Aba, Caozhou, Zhumadian, and Liantang projects) and 150 knots for 750kv ones. Its 750kv knots had 45% market share from total 293 bidding in the market in 2025, up 77% yoy.

Figure 1. Equipment procurement of State Grid in 2025-26 so far for construction of ultra-high voltage transmission lines  
![](images/cb312106b6a221397c8080dfef9527825033cfc595c3b25ce045b806f7efd460.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | Value (Rmbbn) | Cumulative value (Rmbbn) | # of Bid packages |
| :--- | :--- | :--- | :--- |
| 202501 | 2.0 | 2.0 | 55 |
| 202502 | 0.5 | 2.5 | 42 |
| 202503 | 1.3 | 3.8 | 72 |
| 202504 | 16.5 | 20.3 | 114 |
| 202505 | 1.7 | 22.1 | 115 |
| 202601 | 4.0 | 4.0 | 136 |
| 202601-n | 5.0 | 9.0 | 12 |
| 202602 | 9.4 | 18.4 | 119 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, sgcc.com.cn

Figure 2. Listed companies winning the most orders in the 2nd batch of equipment procurement for UHV line construction by State Grid

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Rank</td><td>Value (Rmbbn)</td><td>% of total value</td><td># Bid packages</td><td>Biggest package</td><td>Winning bidder</td></tr><tr><td>Pingao</td><td>600312.SH</td><td>BUY</td><td>1</td><td>2.09</td><td>22.2%</td><td>9</td><td>0.90</td><td>5</td></tr><tr><td>XD Electric</td><td>601179.SH</td><td>Not covered</td><td>2</td><td>1.90</td><td>20.2%</td><td>10</td><td>0.62</td><td>6</td></tr><tr><td>TBEA</td><td>600089.SH</td><td>BUY</td><td>3</td><td>0.47</td><td>5.0%</td><td>6</td><td>0.14</td><td>3</td></tr><tr><td>HSINO</td><td>601096.SH</td><td>Not covered</td><td>4</td><td>0.20</td><td>2.2%</td><td>5</td><td>0.10</td><td>2</td></tr><tr><td>Sieyuan</td><td>002028.SZ</td><td>BUY</td><td>5</td><td>0.20</td><td>2.1%</td><td>6</td><td>0.06</td><td>4</td></tr><tr><td>SGIT</td><td>600131.SH</td><td>Not covered</td><td>6</td><td>0.15</td><td>1.6%</td><td>6</td><td>0.0</td><td>2</td></tr><tr><td>NARI</td><td>600406.SH</td><td>BUY</td><td>7</td><td>0.14</td><td>1.5%</td><td>4</td><td>0.1</td><td>3</td></tr><tr><td>FenGFan</td><td>601700.SH</td><td>Not covered</td><td>8</td><td>0.14</td><td>1.4%</td><td>4</td><td>0.06</td><td>1</td></tr><tr><td>Shaanxi Constrution</td><td>600248.SH</td><td>Not covered</td><td>9</td><td>0.11</td><td>1.1%</td><td>1</td><td>0.11</td><td>1</td></tr><tr><td>CEEC</td><td>601868.SH</td><td>Not covered</td><td>10</td><td>0.10</td><td>1.1%</td><td>2</td><td>0.05</td><td>1</td></tr><tr><td>Others</td><td></td><td></td><td></td><td>3.92</td><td>41.6%</td><td>66</td><td>n/a</td><td>51</td></tr><tr><td>Total</td><td></td><td></td><td></td><td>9.42</td><td>100.0%</td><td>119</td><td>0.90</td><td>79</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, sgcc.com.cn

Figure 3. Valuation comp table of global, Asian and Chinese power grid equipment makers

<table><tr><td rowspan="2"></td><td rowspan="2">Stock code</td><td rowspan="2">Citi rating</td><td rowspan="2">Price 8-Jun-26</td><td rowspan="2">Target price</td><td rowspan="2">Potential upside</td><td colspan="2">PER</td><td colspan="2">PB</td><td colspan="2">ROE</td><td colspan="2">Yield</td><td colspan="2">Net D/E</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="16">PRC private companies:</td></tr><tr><td>Sieyuan</td><td>002028.SZ</td><td>Buy</td><td>177.6</td><td>270.0</td><td>52.0%</td><td>29.6</td><td>21.3</td><td>7.2</td><td>5.6</td><td>26.9%</td><td>29.6%</td><td>0.6%</td><td>0.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Huaming Electric</td><td>002270.SZ</td><td>Buy</td><td>19.6</td><td>32.5</td><td>66.0%</td><td>22.2</td><td>19.7</td><td>5.1</td><td>4.7</td><td>23.9%</td><td>25.1%</td><td>3.2%</td><td>3.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>Wasion Holdings</td><td>3393.HK</td><td>Buy</td><td>20.8</td><td>34.0</td><td>63.6%</td><td>13.6</td><td>10.9</td><td>2.7</td><td>2.3</td><td>20.3%</td><td>22.8%</td><td>2.9%</td><td>3.7%</td><td>net cash</td><td>net cash</td></tr><tr><td>Sanxing Medical Electric</td><td>601567.SS</td><td>n/a</td><td>14.8</td><td>n/a</td><td>n/a</td><td>9.2</td><td>7.3</td><td>1.5</td><td>1.4</td><td>16.9%</td><td>19.3%</td><td>5.5%</td><td>6.8%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>17.5</td><td>13.9</td><td>3.6</td><td>3.1</td><td>19.9%</td><td>22.0%</td><td>3.4%</td><td>4.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">PRC SOEs:</td></tr><tr><td>Pinggao</td><td>600312.SS</td><td>Buy</td><td>18.5</td><td>24.0</td><td>29.9%</td><td>19.8</td><td>17.1</td><td>2.1</td><td>1.9</td><td>10.8%</td><td>11.6%</td><td>2.1%</td><td>2.6%</td><td>net cash</td><td>net cash</td></tr><tr><td>NARI</td><td>600406.SS</td><td>Buy</td><td>22.9</td><td>31.0</td><td>35.6%</td><td>19.9</td><td>18.4</td><td>3.3</td><td>3.0</td><td>16.9%</td><td>17.2%</td><td>3.0%</td><td>3.3%</td><td>net cash</td><td>net cash</td></tr><tr><td>XJ Electric</td><td>000400.SZ</td><td>Buy</td><td>22.1</td><td>33.0</td><td>49.5%</td><td>17.4</td><td>16.3</td><td>1.7</td><td>1.6</td><td>10.2%</td><td>10.1%</td><td>2.3%</td><td>2.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>TBEA</td><td>600089.SS</td><td>Buy</td><td>23.9</td><td>36.0</td><td>50.4%</td><td>13.3</td><td>11.7</td><td>1.6</td><td>1.5</td><td>12.7%</td><td>13.2%</td><td>2.4%</td><td>2.7%</td><td>24.3%</td><td>25.1%</td></tr><tr><td>XD Electric</td><td>601179.SS</td><td>n/a</td><td>14.0</td><td>n/a</td><td>n/a</td><td>46.1</td><td>38.1</td><td>3.0</td><td>2.8</td><td>6.5%</td><td>7.4%</td><td>0.9%</td><td>1.1%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Jinpan Smart Technology</td><td>688676.SS</td><td>n/a</td><td>83.6</td><td>n/a</td><td>n/a</td><td>42.9</td><td>31.2</td><td>6.3</td><td>5.5</td><td>15.2%</td><td>17.9%</td><td>0.9%</td><td>1.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>26.6</td><td>22.1</td><td>3.0</td><td>2.7</td><td>12.1%</td><td>12.9%</td><td>1.9%</td><td>2.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">Asia (ex-China) companies:</td></tr><tr><td>Hyundai Electric</td><td>267260.KS</td><td>Buy</td><td>889,000.0</td><td>1,440,000.0</td><td>62.0%</td><td>31.5</td><td>24.5</td><td>11.5</td><td>8.5</td><td>42.0%</td><td>39.8%</td><td>0.8%</td><td>1.0%</td><td>net cash</td><td>net cash</td></tr><tr><td>LS Electric</td><td>010120.KS</td><td>Buy</td><td>208,000.0</td><td>320,000.0</td><td>53.8%</td><td>66.0</td><td>45.7</td><td>13.1</td><td>11.0</td><td>21.3%</td><td>26.2%</td><td>0.5%</td><td>0.7%</td><td>33.4%</td><td>34.5%</td></tr><tr><td>Hyosung Heavy</td><td>298040.KS</td><td>Buy</td><td>3,196,000.0</td><td>4,500,000.0</td><td>40.8%</td><td>35.2</td><td>25.4</td><td>10.0</td><td>7.6</td><td>32.0%</td><td>34.1%</td><td>0.6%</td><td>0.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Chung Hsin Electric</td><td>1513.TW</td><td>Buy</td><td>169.5</td><td>180.0</td><td>6.2%</td><td>18.6</td><td>16.5</td><td>3.8</td><td>3.6</td><td>21.0%</td><td>22.4%</td><td>4.0%</td><td>4.5%</td><td>-9.5%</td><td>-30.0%</td></tr><tr><td>Fortune Electric</td><td>1519.TW</td><td>Buy</td><td>815.0</td><td>1,150.0</td><td>41.1%</td><td>42.0</td><td>32.3</td><td>21.4</td><td>18.9</td><td>53.6%</td><td>62.0%</td><td>1.9%</td><td>2.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>Shihlin Electric &amp; Engineering</td><td>1503.TW</td><td>n/a</td><td>230.0</td><td>n/a</td><td>n/a</td><td>25.3</td><td>16.8</td><td>3.1</td><td>N/A</td><td>12.9%</td><td>16.7%</td><td>N/A</td><td>N/A</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>38.7</td><td>28.9</td><td>12.0</td><td>9.9</td><td>34.0%</td><td>36.9%</td><td>1.6%</td><td>1.9%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">Global companies:</td></tr><tr><td>ABB</td><td>ABBN.S</td><td>Neutral</td><td>81.9</td><td>78.0</td><td>-4.7%</td><td>31.7</td><td>29.3</td><td>9.4</td><td>8.1</td><td>43.7%</td><td>28.7%</td><td>1.2%</td><td>1.2%</td><td>net cash</td><td>net cash</td></tr><tr><td>Siemens Energy</td><td>ENR1n.DE</td><td>Neutral</td><td>157.5</td><td>185.0</td><td>17.5%</td><td>35.3</td><td>24.1</td><td>13.1</td><td>11.4</td><td>34.6%</td><td>49.4%</td><td>1.3%</td><td>1.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Alstom</td><td>ALSO.PA</td><td>Buy</td><td>16.7</td><td>28.0</td><td>67.9%</td><td>11.8</td><td>9.6</td><td>0.7</td><td>0.7</td><td>3.1%</td><td>5.4%</td><td>N/A</td><td>1.5%</td><td>11.4%</td><td>11.8%</td></tr><tr><td>Schneider Electric</td><td>SCHN.PA</td><td>Buy</td><td>266.8</td><td>340.0</td><td>27.4%</td><td>25.7</td><td>22.5</td><td>5.6</td><td>5.0</td><td>20.8%</td><td>21.7%</td><td>1.6%</td><td>1.7%</td><td>41.8%</td><td>28.8%</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>26.1</td><td>21.4</td><td>7.2</td><td>6.3</td><td>25.5%</td><td>26.3%</td><td>1.4%</td><td>1.6%</td><td>26.6%</td><td>20.3%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, IEBS

## Companies Mentioned:

ABB (ABBN.S; SFr83.1; 2; 05 Jun 26; 17:30) | Alstom (ALSO.PA; €17.15; 1; 05 Jun 26; 17:30) | Changshu Fengfan Power Equipment Co Ltd (601700.SS; Rmb4.95; Not Rated; 08 Jun 26; 15:00) | China Energy Engineering Corp Ltd (601868.SS; Rmb2.8; Not Rated; 08 Jun 26; 15:00) | China XD Electric (601179.SS; Rmb14.01; Not Rated; 08 Jun 26; 15:00) | Chung Hsin Electric (1513.TW; NT\$169.5; 1; 08 Jun 26; 13:30) | Fortune Electric (1519.TW; NT\$815.0; 1; 08 Jun 26; 13:30) | Hainan Jinpan Smart Technology Co Ltd (688676.SS; Rmb83.6; Not Rated; 08 Jun 26; 15:00) | HD Hyundai Electric (267260.KS; W889000.0; 1; 08 Jun 26; 15:45) | Henan Pinggao Electric Co (600312.SS; Rmb18.48; 1; 08 Jun 26; 15:00) | Hsino Tower Group Co Ltd (601096.SS; Rmb4.69; Not Rated; 08 Jun 26; 15:00) | Huaming Power Equipment (002270.SZ; Rmb19.58; 1; 08 Jun 26; 15:00) | Hyosung Heavy Industries (298040.KS; W3196000.0; 1; 08 Jun 26; 15:45) | LS Electric (010120.KS; W208000.0; 1; 08 Jun 26; 15:45) | NARI Technology Co (600406.SS; Rmb22.86; 1; 08 Jun 26; 15:00) | Schneider Electric (SCHN.PA; €269.05; 1; 05 Jun 26; 17:30) | Shaanxi Construction Engineering Group Corp Ltd (600248.SS; Rmb3.07; Not Rated; 08 Jun 26; 15:00) | Shihlin Electric & Engineering Corp (1503.TW; NT\$230.0; Not Rated; 08 Jun 26; 13:30) | Siemens Energy AG (ENRIn.DE; €158.02; 2;

05 Jun 26; 17:30) | Sieyuan Electric (002028.SZ; Rmb177.59; 1; 08 Jun 26; 15:00) | State Grid Information & Communication Co Ltd (600131.SS; Rmb15.4; Not Rated; 08 Jun 26; 15:00) | TBEA Co (600089.SS; Rmb23.94; 1; 08 Jun 26; 15:00) | Wasion Holdings (3393.HK; HK\$20.78; 1; 08 Jun 26; 16:10) | XJ Electric (000400.SZ; Rmb22.07; 1; 08 Jun 26; 15:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifyin

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
