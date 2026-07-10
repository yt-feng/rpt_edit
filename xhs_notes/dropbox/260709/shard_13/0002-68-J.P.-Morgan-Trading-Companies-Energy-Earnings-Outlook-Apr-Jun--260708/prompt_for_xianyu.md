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
# Trading Companies, Energy: Earnings Outlook (Apr-Jun)

Earnings progress unlikely to be viewed as a share-price driver; focus on whether trading companies announce new/additional share buybacks; expect a share buyback from INPEX

## Trading company sector

1Q FY2026 earnings progress: We expect that 1Q FY2026 earnings will be at least 25% of full-year net profit guidance at most trading companies. We believe that higher resource prices and logistics and trade-related profits associated with the Middle East conflict are pushing up profits. Average April-June 2026 resource prices were \$97.0/bbl for Brent crude (\$78.4/bbl in January-March 2026, \$66.7/bbl in April-June 2025); \$13,355/t or \$6.05/lb for LME copper (\$12,824/t or \$5.82/lb in January-March 2026, \$9,508/t or \$4.31/lb in April-June 2025); and \$238.8/t for coking coal (\$226.5/t in January-March 2026, \$184.9/t in April-June 2025), so so the QoQ and YoY rises were particularly large. However, because many resource businesses, mainly energy projects, are reflected in earnings after a three-month lag, it is important to note that the 1Q FY2026 results of trading companies reflect the January-March 2026 results of resource businesses. We expect each company's progress toward full-year guidance to be 23-30%. We think progress will be more than 25% at the six companies excluding Sojitz, which has a seasonally low progress rate in 1Q. In descending order of progress, we forecast 30% for Mitsui & Co., 29% for Marubeni Corporation, 29% for Mitsubishi Corporation, 27% for Itochu Corporation, 27% for Toyota Tsusho, 26% for Sumitomo Corporation, and 22% for Sojitz. We do not expect any trading company to announce a revision of its full-year FY2026 guidance.

Sector investment stance and points to note: Our investment stance on the trading company sector is neutral. We expect strong progress in 1Q FY2026 earnings, but this is largely due to high resource prices, and with resource prices peaking, we think it is unlikely to be seen as a stock price catalyst. We continue to focus on whether sector companies can implement large-scale, high-quality investment projects that lead to expectations for an increase in ROE, and whether they adopt a proactive capital policy with an emphasis on ROE targets. The main points to watch at the time of 1Q FY2026 results are 1) whether Mitsui & Co. and Mitsubishi announce share buybacks, as they did not announce any plans for FY2026 at the start of the fiscal year (we do not expect an announcement by Mitsubishi but think Mitsui & Co. may announce a share buyback of at least ¥200 billion); 2) whether Itochu announces share buybacks as part of its FY2026 plan of ¥300 billion or more (we expect an announcement of around ¥200 million); and 3) whether Marubeni announces a share buyback to follow the ¥45 billion it announced and has implemented since the start of the fiscal year (we think it is possible, but our main scenario is for an announcement when it reports 2Q results).

## Three oil refiners

1Q FY2026 earnings progress: We expect oil companies' 1Q FY2026 results to vary (all excluding inventory impact). For ENEOS Holdings, we expect operating profit to rise 41% YoY to ¥190 billion (32% of full-year guidance) and net profit to grow 168% to ¥120 billion (30%). Capital gains on the sale of shares in JX

See page 10 for analyst certification and important disclosures, including non-US analyst disclosures.

Japan Equity Research
Trading Companies, Energy

Jiro lokibe AC
(81-3) 6736-8668
jiro.iokibe@JPM.com
JPM Securities Japan Co., Ltd.

Advanced Metals (¥86 billion before tax) should boost earnings. For Idemitsu Kosan, we forecast pretax profit of ¥29.6 billion, down 13% YoY (21%) and net profit of ¥17.8 billion, down 56% (20%). We expect quarterly profit to be slightly below one-quarter of full-year guidance. For Cosmo Energy Holdings, we forecast that 1Q FY2026 recurring profit will decline 53% YoY to ¥10 billion (9%) and that net profit will fall 39% to ¥6 billion (15%). We think oil companies' 1Q results will be unavoidably weak due to the suspension of production and shipments from Abu Dhabi oil fields in the Middle East and the rise in the cost of sourcing oil products in the domestic oil business.

Sector investment stance and points to note: We have been recommending a somewhat cautious investment stance toward the oil wholesalers. We do not expect any changes in shareholder return measures at 1Q FY2026 results, such as revisions to FY2026 earnings guidance and announcements of additional share buybacks. As trends in domestic oil refining margins have become more opaque from an outsider's perspective due to the turmoil in the Middle East, we will focus on 1Q FY2026 results information and explanations given by company management teams at briefings. Points to watch include (1) passing on the costs of imported crude oil alternatives, and (2) resuming exports to Asia. The additional costs related to the procurement of crude oil from outside the Middle East have not been passed on to product prices in 1Q FY2026, and we expect each company to endeavor to do so from this 2Q onward. The Ministry of Economy, Trade and Industry (METI) announced that it will reflect the cost of alternative crude oil procurement when calculating subsidies for petroleum products starting this month. An additional ¥4.9/liter will be added to the July payments made to each oil company. Furthermore, according to industry publications such as RIM Intelligence's, it appears that the major oil wholesalers resumed exporting diesel fuel to Asia in July.

## INPEX (1605)

2Q FY2026 earnings progress: We forecast INPEX's 2Q (April-June 2026) net profit at ¥121 billion, up 24% YoY. We expect strong profit in the mainstay business on the back of rising crude oil prices, with net profit from the Ichthys business rising 16% to ¥75 billion and net profit in the overseas oil & gas, other segment rising 23% to ¥45 billion. This would mean net profit in 1H FY2026 of ¥230.4 billion, or 51% of the ¥450 billion upper limit of full-year guidance (based on a \$83/bbl crude oil price), and 66% of the lower limit of ¥350 billion (based on a \$70/bbl crude oil price). The labor strike at Ichthys LNG in June 2026 ended quickly, so the impact on Ichthys's LNG production and shipments appears to be minor.

Investment opinion and points to note: We rate INPEX Overweight. However, with crude oil prices peaking out, the stock has underperformed TOPIX significantly since April. The points of focus in 2Q results are 1) whether it announces a share buyback (we expect an announcement of around ¥50 billion), and 2) whether it revises FY2026 guidance. Our base scenario is for a narrowing in the guidance range for net profit toward the upper limit of ¥450 billion, but we think there is a certain degree of downside risk due to the decline in crude oil prices. Since the company's policy is for a total return ratio of more than 50%, net profit guidance and share buyback amounts tend to correlate closely.

<table><tr><td rowspan="2">(JPY bn)</td><td colspan="4">FY24</td><td colspan="4">FY25</td><td>FY26E</td><td>vs FY26</td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1QE</td><td>CoE</td></tr><tr><td>ITOCHU</td><td>206.6</td><td>231.8</td><td>238.0</td><td>203.8</td><td>283.9</td><td>216.3</td><td>205.0</td><td>195.0</td><td>253.0</td><td>27%</td></tr><tr><td>Marubeni</td><td>142.6</td><td>95.5</td><td>187.1</td><td>77.8</td><td>154.4</td><td>151.1</td><td>126.8</td><td>111.6</td><td>168.0</td><td>29%</td></tr><tr><td>Mitsui &amp; Co.</td><td>276.1</td><td>135.7</td><td>240.4</td><td>248.2</td><td>191.6</td><td>232.1</td><td>188.2</td><td>222.0</td><td>273.0</td><td>30%</td></tr><tr><td>Sumitomo Corp</td><td>126.3</td><td>127.6</td><td>162.5</td><td>145.4</td><td>170.9</td><td>130.4</td><td>107.2</td><td>191.9</td><td>162.0</td><td>26%</td></tr><tr><td>Mitsubishi Corp</td><td>354.4</td><td>263.7</td><td>209.4</td><td>123.3</td><td>203.1</td><td>152.7</td><td>252.1</td><td>192.5</td><td>319.0</td><td>29%</td></tr><tr><td>Toyota Tsusho</td><td>95.8</td><td>85.7</td><td>96.3</td><td>84.7</td><td>98.3</td><td>88.6</td><td>100.1</td><td>83.5</td><td>107.0</td><td>27%</td></tr><tr><td>Sojitz</td><td>23.0</td><td>21.3</td><td>31.8</td><td>34.5</td><td>21.1</td><td>24.2</td><td>35.1</td><td>23.2</td><td>29.0</td><td>22%</td></tr><tr><td>Total of 7 Companies</td><td>1,224.9</td><td>961.4</td><td>1,165.4</td><td>917.6</td><td>1,123.4</td><td>995.3</td><td>1,014.6</td><td>1,019.7</td><td>1,311.0</td><td>28%</td></tr><tr><td></td><td>4.7%</td><td>3.6%</td><td>10.0%</td><td>-4.7%</td><td>-8.3%</td><td>3.5%</td><td>-12.9%</td><td>11.1%</td><td>16.7%</td><td>-</td></tr><tr><td colspan="11">Idemitsu</td></tr><tr><td>OP + Equity earnings (ex Inventory impact)</td><td>82.1</td><td>31.9</td><td>54.5</td><td>46.1</td><td>33.8</td><td>54.6</td><td>28.4</td><td>127.2</td><td>29.6</td><td>21%</td></tr><tr><td>Net Profit (ex Inventory imopact)</td><td>61.7</td><td>38.2</td><td>43.6</td><td>-18.7</td><td>40.3</td><td>37.1</td><td>28.3</td><td>86.6</td><td>17.8</td><td>20%</td></tr><tr><td colspan="11">ENEOS</td></tr><tr><td>Operating Profit (ex Inventory impact)</td><td>113.1</td><td>95.1</td><td>179.0</td><td>-223.6</td><td>135.1</td><td>138.4</td><td>117.8</td><td>83.0</td><td>190.0</td><td>32%</td></tr><tr><td>Net Profit (ex Inventory imopact)</td><td>55.3</td><td>56.5</td><td>118.3</td><td>36.3</td><td>44.8</td><td>94.7</td><td>74.1</td><td>50.5</td><td>120.0</td><td>30%</td></tr><tr><td colspan="11">Cosmo</td></tr><tr><td>Recurring Profit (ex Inventory impact)</td><td>44.4</td><td>33.2</td><td>39.1</td><td>64.9</td><td>21.1</td><td>51.8</td><td>40.6</td><td>52.3</td><td>10.0</td><td>9%</td></tr><tr><td>Net Profit (ex Inventory imopact)</td><td>18.6</td><td>15.2</td><td>22.9</td><td>22.5</td><td>9.8</td><td>27.6</td><td>18.5</td><td>29.6</td><td>6.0</td><td>15%</td></tr><tr><td rowspan="2">(JPY bn)</td><td colspan="3">FY24</td><td colspan="4">FY25</td><td colspan="2">FY26E</td><td>vs FY26</td></tr><tr><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2QE</td><td>CoE</td></tr><tr><td>INPEX</td><td>90.8</td><td>76.8</td><td>137.9</td><td>126.3</td><td>97.2</td><td>69.9</td><td>100.4</td><td>109.4</td><td>121.0</td><td>51%</td></tr></table>

Figure 1: Earnings estimates for trading companies and energy sector companies

<table><tr><td rowspan="2">FY23</td><td rowspan="2">FY24</td><td rowspan="2">FY25</td><td rowspan="2">FY26EJPME</td><td rowspan="2">FY27EJPME</td><td rowspan="2">FY28EJPME</td><td colspan="2">as of May26</td></tr><tr><td>FY26ECoE</td><td></td></tr><tr><td>801.8</td><td>880.3</td><td>900.3</td><td>950.0</td><td>1,000.0</td><td>1,040.0</td><td>950.0</td><td></td></tr><tr><td>471.4</td><td>503.0</td><td>543.9</td><td>600.0</td><td>620.0</td><td>630.0</td><td>580.0</td><td></td></tr><tr><td>1,063.7</td><td>900.3</td><td>834.0</td><td>1,080.0</td><td>1,180.0</td><td>1,190.0</td><td>920.0</td><td></td></tr><tr><td>386.4</td><td>561.9</td><td>600.3</td><td>650.0</td><td>700.0</td><td>740.0</td><td>630.0</td><td></td></tr><tr><td>964.0</td><td>950.7</td><td>800.5</td><td>1,290.0</td><td>1,220.0</td><td>1,170.0</td><td>1,100.0</td><td></td></tr><tr><td>331.4</td><td>362.5</td><td>370.5</td><td>420.0</td><td>450.0</td><td>480.0</td><td>400.0</td><td></td></tr><tr><td>100.8</td><td>110.6</td><td>103.6</td><td>124.0</td><td>132.0</td><td>140.0</td><td>130.0</td><td></td></tr><tr><td>4,119.5</td><td>4,269.3</td><td>4,153.0</td><td>5,114.0</td><td>5,302.0</td><td>5,390.0</td><td>4,710.0</td><td></td></tr><tr><td>-10.7%</td><td>3.6%</td><td>-2.7%</td><td>23.1%</td><td>3.7%</td><td>1.7%</td><td>10.3%</td><td></td></tr><tr><td colspan="8"></td></tr><tr><td>310.5</td><td>214.7</td><td>244.1</td><td>184.0</td><td>237.0</td><td>244.0</td><td>140.0</td><td></td></tr><tr><td>192.1</td><td>124.8</td><td>192.3</td><td>130.0</td><td>170.0</td><td>170.0</td><td>90.0</td><td></td></tr><tr><td colspan="8"></td></tr><tr><td>393.2</td><td>429.3</td><td>474.4</td><td>560.0</td><td>500.0</td><td>520.0</td><td>590.0</td><td></td></tr><tr><td>237.9</td><td>266.4</td><td>264.2</td><td>340.0</td><td>310.0</td><td>320.0</td><td>400.0</td><td></td></tr><tr><td colspan="8"></td></tr><tr><td>162.2</td><td>181.6</td><td>165.7</td><td>120.0</td><td>170.0</td><td>160.0</td><td>110.0</td><td></td></tr><tr><td>82.5</td><td>79.2</td><td>85.5</td><td>49.0</td><td>92.0</td><td>82.0</td><td>40.0</td><td></td></tr><tr><td colspan="8"></td></tr><tr><td colspan="6"></td><td>Oil $83</td><td>Oil $70</td></tr><tr><td>FY24</td><td>FY25</td><td>FY26EJPME</td><td>FY27EJPME</td><td>FY28EJPME</td><td></td><td>FY26ECoE</td><td>FY26ECoE</td></tr><tr><td>427.3</td><td>393.8</td><td>450.0</td><td>600.0</td><td>480.0</td><td></td><td>450.0</td><td>350.0</td></tr></table>

Note: CoE refers to the companies' estimates. JPMe refers to JPM estimates. Net profit for trading companies and INPEX. Source: Company data, JPM.

Figure 2: Net profit by segment for ITOCHU

<table><tr><td rowspan="2">(¥bn)</td><td colspan="4">FY24</td><td colspan="4">FY25</td><td>FY26E</td><td>vsFY26</td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1QE</td><td>CoE</td></tr><tr><td>Textile</td><td>5.3</td><td>7.4</td><td>57.8</td><td>3.4</td><td>8.9</td><td>15.3</td><td>11.9</td><td>7.2</td><td>10.0</td><td>19%</td></tr><tr><td>Machinery</td><td>34.0</td><td>29.3</td><td>40.5</td><td>32.7</td><td>32.0</td><td>44.9</td><td>39.3</td><td>39.4</td><td>45.0</td><td>25%</td></tr><tr><td>Metals &amp; Minerals</td><td>52.5</td><td>47.9</td><td>32.7</td><td>45.2</td><td>33.6</td><td>30.0</td><td>39.9</td><td>40.1</td><td>45.0</td><td>26%</td></tr><tr><td>Energy &amp; Chemicals</td><td>17.8</td><td>15.2</td><td>17.6</td><td>28.0</td><td>19.5</td><td>18.2</td><td>17.3</td><td>14.3</td><td>25.0</td><td>33%</td></tr><tr><td>Food</td><td>19.0</td><td>21.2</td><td>19.8</td><td>25.1</td><td>28.8</td><td>25.1</td><td>28.5</td><td>9.6</td><td>35.0</td><td>30%</td></tr><tr><td>General Products &amp; Realty</td><td>18.8</td><td>12.4</td><td>11.5</td><td>27.0</td><td>11.2</td><td>7.8</td><td>7.0</td><td>34.8</td><td>13.0</td><td>21%</td></tr><tr><td>ICT &amp; Financial Business</td><td>16.0</td><td>21.9</td><td>20.2</td><td>25.2</td><td>16.1</td><td>23.9</td><td>20.8</td><td>32.2</td><td>20.0</td><td>21%</td></tr><tr><td>The 8th</td><td>10.9</td><td>43.3</td><td>9.7</td><td>1.2</td><td>15.4</td><td>17.0</td><td>12.9</td><td>-0.3</td><td>10.0</td><td>33%</td></tr><tr><td>Others</td><td>32.2</td><td>33.4</td><td>28.3</td><td>15.9</td><td>118.4</td><td>34.2</td><td>27.4</td><td>17.7</td><td>50.0</td><td>31%</td></tr><tr><td>Total Net Profit</td><td>206.6</td><td>231.8</td><td>238.0</td><td>203.8</td><td>283.9</td><td>216.3</td><td>205.0</td><td>195.0</td><td>253.0</td><td>27%</td></tr><tr><td></td><td>yoy</td><td>-3%</td><td>16%</td><td>20%</td><td>7%</td><td>37%</td><td>-7%</td><td>-14%</td><td>-4%</td><td>-11%</td></tr><tr><td>One-off gains/losses</td><td>4.5</td><td>38.0</td><td>52.5</td><td>15.0</td><td>103.0</td><td>18.5</td><td>10.5</td><td>-13.0</td><td>40.0</td><td>-</td></tr></table>

Note: CoE refers to the company's estimates. JPME refers to JPM estimates.

<table><tr><td rowspan="2">FY23</td><td rowspan="2">FY24</td><td rowspan="2">FY25</td><td rowspan="2">FY26EJPME</td><td rowspan="2">FY27EJPME</td><td rowspan="2">FY28EJPME</td><td>May 26</td></tr><tr><td>FY26ECoE</td></tr><tr><td>27.0</td><td>73.8</td><td>43.3</td><td>52.0</td><td>56.0</td><td>61.0</td><td>52.0</td></tr><tr><td>131.6</td><td>136.5</td><td>155.6</td><td>185.0</td><td>192.0</td><td>199.0</td><td>180.0</td></tr>

[中间内容因长度限制已省略]

 forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not

Completed 08 Jul 2026 10:10 AM JST
"""
