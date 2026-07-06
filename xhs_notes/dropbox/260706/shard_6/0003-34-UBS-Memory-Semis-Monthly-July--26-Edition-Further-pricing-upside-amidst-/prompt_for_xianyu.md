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
# Memory Semis Monthly July '26 Edition: Further pricing upside amidst LTA negotiations

## Upside to 2H26 memory pricing

Based upon our industry checks, we increase base-line DDR contract pricing to +32% QoQ in 3Q26 (was +17%) and +18% QoQ in 4Q26 (was +12%), after +67% QoQ in 2Q26. Depending upon pricing under longer term agreements (LTAs), as well as HBM pricing and mix, the QoQ ASP comparisons will vary though by memory vendor. We continue to forecast the DRAM industry to be undersupplied until at least 2Q28. The gap between bit demand growth in 2027 (+36.2% YoY) and supply (+19.3%) is too wide to close by then. If we assume no inventory digestion downstream in 2027 (i.e., no customers' inventory rebuild in 2H26), then the sufficiency ratio would actually deteriorate to -13.6% from -8.1% in 2026E. Both are unprecedented levels over the last 30 years. As for NAND flash, we now forecast +30% QoQ in 3Q26 (was +17%) and +12% QoQ (unchanged) in 4Q26 after +67% QoQ also in 2Q. We forecast the NAND upcycle to continue til at least 4Q27. Net net, this leaves us forecasting memory industry revenues to reach US\$992bn in 2026 and US\$1,763bn in 2027. The main risk to this unprecedented upcycle remains affordability by customers, notably hyperscalers which will have to continue to tap capital markets to finance this capex.

## LTA negotiations continue

Revised LTA negotiations, which incorporate more fixed terms for volumes and pricing, continue. We see some differences between Micron's SCAs, with price "floor" and "ceiling", and those of the Korean memory makers, which we believe have a portion of volumes fixed (c. 60-70% over a 5-year contract), at fixed pricing, to which a variable component (volume and pricing) is added. We believe Samsung is progressing in completing by 3Q more revised LTA agreements with another handful of large customers. The focus remains on DDR5, for which we would expect a target of 50-70% of volumes being tied up to LTAs. As for SK Hynix, we believe negotiations continue to focus on the larger hyperscale customers for both DDR5 and NAND flash.

## Slightly raising HBM demand forecasts, Meta not an issue

We tweak our HBM industry demand forecast to 33.1bn Gb in 2026 (+90% YoY) and 58.7bn Gb in 2027 (+77% YoY) from 32.9/58.0bn prior. We assume HBM procurement equivalent to 8.5mil Nvidia AI GPU units in 2026E, and 11.0mil in 2027E, consistent with our recent CoWoS estimate revision (link). We revise our estimates for HBM-equivalent Google TPU units to 4.2mil for 2026E and 9.1mil (up) for 2027E, also tweaking up HBM procurement for AMD and AWS for 2027. Meanwhile, recent press reports of Meta possibly selling compute to outside customers (link) negatively impacted memory stocks earlier this week. Still, this is likely monetisation of older assets prior to rolling out further Blackwell/Rubin, as well as MTIA capacity (see also note from Steven Ju: link). As such, we see no impact on HBM procurement.

## Pullback in memory semis stocks likely temporary

Memory stocks are on average down 17% from their June peak, after outperforming Semis, Tech, and GEM YTD. Some of this could be over-crowding. Yet, fundamentals remain strong, with the memory industry set to generate close to US\$1.2tn of FCF in 2027E. We believe this will ultimately lead to a step-up in returns to shareholders. We remain positive on the group, with Samsung Key Call Buy (PT Won550k), and Buy ratings on SK Hynix (PT 3.20m from 3.00m), MU (PT US\$1,625), Kioxia (PT ¥132,000) and Nanya Tech (PT NT\$495).

## Equities

Global Semiconductors

Nicolas Gaudois
Analyst
nicolas.gaudois@ubs.com
+65-6495 5148

Timothy Arcuri
Analyst
timothy.arcuri@ubs.com
+1-415-352 5676

Kenji Yasui
Analyst
kenji.yasui@ubs.com
+81-3-5208 6211

Jimmy Yoon
Analyst
jimmy.yoon@ubs.com
+65-6495 4617

Gianmarco Vella
Associate Analyst
gianmarco.vella@ubs.com
+1-415-352 4555

Atsuhiro Kinoshita
Analyst
atsuhiro.kinoshita@ubs.com
+81-3-5208 6768

Sunny Lin
Analyst
sunny.lin@ubs.com
+886-2-8722 7346

Jimmy Yu
Analyst
S1460517080002
jimmy.yu@ubs.com
+86-21-3866 8880

Randy Abrams
Analyst
randy.abrams@ubs.com
+886-2-8722 7338

Francois-Xavier Bouvignies
Analyst
francois.bouvignies@ubs.com
+44-20-7568 7105

## KEY CHARTS

Figure 1: AI server GPU/accelerator unit forecasts ('000 units)

<table><tr><td></td><td>HBM Gen.</td><td colspan="3">HBM Content (GB)</td><td>2025</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2027E</td></tr><tr><td>NVIDIA</td><td></td><td>2025E</td><td>2026E</td><td>2027E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>L40S</td><td>GDDR6</td><td>48</td><td></td><td></td><td>38.1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>H200</td><td>HBM3E</td><td>141</td><td></td><td></td><td>592.7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>H20 / H20E</td><td>HBM3 / 3E</td><td>96</td><td>96</td><td></td><td>441.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B200 (8Hi)</td><td>HBM3E</td><td>192</td><td>192</td><td></td><td>1,440.9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GB200 (2x GPU - 8Hi)</td><td>HBM3E</td><td>384</td><td>384</td><td></td><td>1,080.4</td><td>102.9</td><td></td><td></td><td></td><td>102.9</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B300 (12Hi)</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td>587.4</td><td>267.0</td><td>300.0</td><td>250.0</td><td>170.0</td><td>987.0</td><td>100.0</td><td></td><td></td><td></td><td>100.0</td></tr><tr><td>GB300 (2x GPU - 12Hi)</td><td>HBM3E</td><td>576</td><td>576</td><td>576</td><td>778.2</td><td>658.0</td><td>670.0</td><td>600.0</td><td>520.0</td><td>2,448.0</td><td>280.0</td><td>180.0</td><td>110.0</td><td>60.0</td><td>630.0</td></tr><tr><td>R200 (12Hi)</td><td>HBM4</td><td>288</td><td>288</td><td>288</td><td></td><td></td><td>20.0</td><td>200.0</td><td>380.0</td><td>600.0</td><td>360.0</td><td>400.0</td><td>300.0</td><td>210.0</td><td>1,270.0</td></tr><tr><td>RV200 (2x GPU - 12Hi)</td><td>HBM4</td><td>576</td><td>576</td><td>576</td><td></td><td></td><td>40.0</td><td>250.0</td><td>480.0</td><td>770.0</td><td>570.0</td><td>700.0</td><td>670.0</td><td>520.0</td><td>2,460.0</td></tr><tr><td>R300 (12Hi)</td><td>HBM4E</td><td></td><td>384</td><td>384</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>130.0</td><td>270.0</td><td>400.0</td></tr><tr><td>RV300 (4x GPU - 12Hi)</td><td>HBM4E</td><td></td><td>768</td><td>768</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>200.0</td><td>500.0</td><td>700.0</td></tr><tr><td>*Other GPU/Accel</td><td>HBM3 / 3E</td><td>288</td><td>384</td><td>576</td><td>106.9</td><td>60.0</td><td>80.0</td><td>80.0</td><td>80.0</td><td>300.0</td><td>70.0</td><td>60.0</td><td>60.0</td><td>50.0</td><td>240.0</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>5,065.6</td><td>1,087.9</td><td>1,110.0</td><td>1,380.0</td><td>1,630.0</td><td>5,207.9</td><td>1,380.0</td><td>1,340.0</td><td>1,470.0</td><td>1,610.0</td><td>5,800.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>3.2%</td><td>-17.2%</td><td>0.0%</td><td>8.2%</td><td>19.4%</td><td>2.8%</td><td>26.9%</td><td>20.7%</td><td>6.5%</td><td>-1.2%</td><td>11.4%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-20.3%</td><td>2.0%</td><td>24.3%</td><td>18.1%</td><td></td><td>-15.3%</td><td>-2.9%</td><td>9.7%</td><td>9.5%</td><td></td></tr><tr><td>Total GPUs</td><td></td><td></td><td></td><td></td><td>6,924.3</td><td>1,848.8</td><td>1,820.0</td><td>2,230.0</td><td>2,630.0</td><td>8,528.8</td><td>2,230.0</td><td>2,220.0</td><td>2,850.0</td><td>3,690.0</td><td>10,990.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>37.9%</td><td>27.2%</td><td>22.9%</td><td>19.6%</td><td>23.7%</td><td>23.2%</td><td>20.6%</td><td>22.0%</td><td>27.8%</td><td>40.3%</td><td>28.9%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-13.0%</td><td>-1.6%</td><td>22.5%</td><td>17.9%</td><td></td><td>-15.2%</td><td>-0.4%</td><td>28.4%</td><td>29.5%</td><td></td></tr><tr><td>AMD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI300</td><td>HBM3</td><td>192</td><td>192</td><td></td><td>71.3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI325X (12Hi)</td><td>HBM3E</td><td>256</td><td>256</td><td></td><td>223.8</td><td>18.0</td><td></td><td></td><td></td><td>18.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI355X (12Hi)</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td>220.7</td><td>170.0</td><td>150.0</td><td>80.0</td><td>70.0</td><td>470.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI308X</td><td>HBM3</td><td>192</td><td>192</td><td>192</td><td>95.8</td><td>29.0</td><td>28.0</td><td>5.0</td><td></td><td>62.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MI450 (12Hi)</td><td>HBM4</td><td></td><td>432</td><td>432</td><td></td><td></td><td></td><td>45.0</td><td>230.0</td><td>275.0</td><td>350.0</td><td>450.0</td><td>470.0</td><td>380.0</td><td>1,650.0</td></tr><tr><td>MI5XX (16Hi)</td><td>HBM4E</td><td></td><td></td><td>1024</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>60.0</td><td>160.0</td><td>220.0</td></tr><tr><td>*Other GPU/Accel</td><td>HBM3</td><td>192</td><td>192</td><td>288</td><td>4.2</td><td>1.4</td><td>1.5</td><td>1.5</td><td>1.5</td><td>5.8</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>8.0</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>615.8</td><td>218.4</td><td>179.5</td><td>131.5</td><td>301.5</td><td>830.8</td><td>352.0</td><td>452.0</td><td>532.0</td><td>542.0</td><td>1,878.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>41.1%</td><td>81.0%</td><td>86.4%</td><td>-26.5%</td><td>37.0%</td><td>34.9%</td><td>61.2%</td><td>151.8%</td><td>304.7%</td><td>79.8%</td><td>126.0%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-0.7%</td><td>-17.8%</td><td>-26.8%</td><td>129.3%</td><td></td><td>16.8%</td><td>28.4%</td><td>17.7%</td><td>1.9%</td><td></td></tr><tr><td>Google</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v5e</td><td>HBM2E</td><td>32</td><td>32</td><td></td><td>134</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v5p</td><td>HBM2E</td><td>96</td><td>96</td><td></td><td>1,916</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v6e</td><td>HBM3E</td><td>32</td><td>32</td><td>32</td><td>426</td><td>205</td><td>224</td><td>141</td><td>70</td><td>640</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TPU v7</td><td>HBM3E</td><td>192</td><td>192</td><td>192</td><td>90</td><td>520</td><td>720</td><td>800</td><td>750</td><td>2,790</td><td>640</td><td>420</td><td>300</td><td>180</td><td>1,540</td></tr><tr><td>TPU v8 (Dual die AX)</td><td>HBM3E</td><td></td><td>288</td><td>288</td><td></td><td></td><td></td><td>25</td><td>225</td><td>250</td><td>740</td><td>940</td><td>980</td><td>840</td><td>3,500</td></tr><tr><td>TPU v8T (Single die X)</td><td>HBM3E</td><td></td><td>216</td><td>216</td><td></td><td></td><td></td><td>70</td><td>380</td><td>450</td><td>850</td><td>1,040</td><td>1,160</td><td>950</td><td>4,000</td></tr><tr><td>*Other TPU/Accel</td><td>HBM3</td><td>96</td><td>144</td><td>144</td><td>77</td><td>7</td><td>9</td><td>10</td><td>10</td><td>37</td><td>15</td><td>15</td><td>15</td><td>15</td><td>60</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>2,642.5</td><td>732.0</td><td>953.4</td><td>1,046.2</td><td>1,435.4</td><td>4,167.0</td><td>2,245.0</td><td>2,415.0</td><td>2,455.0</td><td>1,985.0</td><td>9,100.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>18.6%</td><td>14.3%</td><td>66.1%</td><td>82.4%</td><td>68.0%</td><td>57.7%</td><td>206.7%</td><td>153.3%</td><td>134.7%</td><td>38.3%</td><td>118.4%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-14.3%</td><td>30.2%</td><td>9.7%</td><td>37.2%</td><td></td><td>56.4%</td><td>7.6%</td><td>1.7%</td><td>-19.1%</td><td></td></tr><tr><td>Amazon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Inferentia 2</td><td>HBM2E</td><td>32</td><td>32</td><td></td><td>88</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Trainium 2 / 2.5</td><td>HBM3E</td><td>96</td><td>144</td><td>144</td><td>496</td><td>130</td><td>220</td><td>140</td><td>100</td><td>590</td><td>50</td><td>10</td><td></td><td></td><td>60</td></tr><tr><td>Inferentia 3</td><td>HBM3E</td><td>96</td><td>96</td><td>96</td><td>162</td><td>30</td><td>28</td><td>20</td><td>18</td><td>96</td><td>15</td><td>10</td><td></td><td></td><td>25</td></tr><tr><td>Trainium 3</td><td>HBM3E</td><td>144</td><td>144</td><td>144</td><td></td><td></td><td>320</td><td>620</td><td>840</td><td>1,780</td><td>840</td><td>780</td><td>640</td><td>540</td><td>2,800</td></tr><tr><td>Trainium 4</td><td>HBM4</td><td></td><td>256</td><td>256</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>40</td><td>240</td><td>280</td></tr><tr><td>*Other Accel</td><td>HBM3</td><td>144</td><td>144</td><td>144</td><td>37</td><td>5</td><td>6</td><td>8</td><td>10</td><td>28</td><td>8</td><td>8</td><td>7</td><td>7</td><td>30</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>783.2</td><td>164.8</td><td>573.7</td><td>787.8</td><td>967.6</td><td>2,493.9</td><td>913.0</td><td>808.0</td><td>687.0</td><td>787.0</td><td>3,195.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>-7.7%</td><td>-16.5%</td><td>179.8%</td><td>301.7%</td><td>423.9%</td><td>218.4%</td><td>454.0%</td><td>40.8%</td><td>-12.8%</td><td>-18.7%</td><td>28.1%</td></tr><tr><td>% QoQ</td><td></td><td></td><td></td><td></td><td></td><td>-10.8%</td><td>248.1%</td><td>37.3%</td><td>22.8%</td><td></td><td>-5.6%</td><td>-11.5%</td><td>-15.0%</td><td>14.6%</td><td></td></tr><tr><td>Intel / Habana</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gaudi 3</td><td>HBM2 / 3E</td><td>288</td><td>288</td><td>288</td><td>188</td><td>30</td><td>18</td><td>8</td><td>0</td><td>56</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gaudi 4</td><td>HBM3E</td><td>288</td><td>288</td><td>288</td><td></td><td></td><td></td><td>10</td><td>25</td><td>35</td><td>25</td><td>20</td><td>15</td><td>10</td><td>70</td></tr><tr><td>*Others</td><td>HBM2 / 3E</td><td>192</td><td>192</td><td>192</td><td>25</td><td>6</td><td>4</td><td>4</td><td>5</td><td>18</td><td>4</td><td>4</td><td>4</td><td>4</td><td>16</td></tr><tr><td>Total Units</td><td></td><td></td><td></td><td></td><td>213.2</td><td>36.0</td><td>21.6</td><td>21.6</td><td>30.0</td><td>109.2</td><td>29.0</td><td>24.0</td><td>19.0</td><td>14.0</td><td>86.0</td></tr><tr><td>% YoY</td><td></td><td></td><td></td><td></td><td>-32.1%</td><td>-20.3%</td><td>-60.1%</td><td>-62.7%</td><t

[中间内容因长度限制已省略]

 is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
