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
CHINA NEW ENERGY VEHICLE WEEKLY CHARTBOOK

# 2026 Week 29 - NEV orders +31% wow/+5% yoy on strong XPeng Mona L03 demand, PV retail yoy decline narrowing

Bottom line: Weekly NEV orders were +31% wow and +5% yoy, mainly driven by XPeng's Mona L03 launch and Li Auto's L6 facelift launch on Jul 16. XPeng booked 59.2k units of non-refundable orders in week 29 after Mona L03 launch, with 70% from BEV version. Industry wise, domestic PV retail volume decline narrowed to -15% yoy during Jul 1-12, vs. -20% yoy in 1H26.

A curated compilation of the most topical charts on weekly passenger vehicle market performance, organized into the following categories: (1) Key NEV brands' weekly orders amount, (2) Key events to watch, (3) NEV/ICE dealer price discount tracker, and (4) Upstream battery pricing dynamics.

## 2026 Week 29 highlights:

Key brand orders: XPeng / Li Auto / Xiaomi showed the strongest growth at +737%/+131%/+32% wow, driven by XPeng's Mona L03 launch and Li Auto's L6 facelift launch on Jul 16.

■ CPCA weekly trend: As of Jul 1-12, PV retail volume was 443k units (-15% yoy/-1% mom), while PV wholesale volume was 379k units (-26% yoy/-17% mom) per CPCA.

Meanwhile, NEV retail volume was 280k units (-8% yoy/-3% mom), and NEV wholesale volume was 262k units (-9% yoy/-15% mom), with NEV penetration at 63.1%/69.1% in Jul 1-12, compared to 62.8%/63.4% in Jun.

■ Key pricing trends: Both NEV and ICE dealer discounts narrowed wow.

■ Upstream battery pricing dynamics: Battery grade lithium carbonate price is unchanged at Rmb153k/ton (+0.0% wow), while prismatic cell (LFP) and prismatic cell (NCM) prices were stable wow.

Tina Hou
+86(21)2401-8694 |
tina.hou@goldmansachs.cn
GS (China) Securities
Company Limited

Jenny Du
+86(21)2401-8978 |
jenny.x.du@goldmansachs.cn
GS (China) Securities
Company Limited

## Weekly order summary

Key brand weekly order trends during 2026 week 29 (7/13-7/19):

■ Key NEV OEMs combined orders were +31% wow and +5% yoy, mainly driven by new and refreshed model launches.

XPeng / Li Auto / Xiaomi showed the strongest growth at +737%/+131%/+32% wow, driven by XPeng's Mona L03 launch and Li Auto's L6 facelift launch on Jul 16.

In terms of YTD orders, Nio / HIMA / XPeng showed relatively defensive growth at +96%/+27%/-2% yoy.

Exhibit 1: NEV brand weekly orders summary

<table><tr><td></td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jul-26 MTD</td><td>2026 YTD</td></tr><tr><td colspan="9">Monthly order (units)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>123535</td><td>96547</td><td>252181</td><td>223899</td><td>197343</td><td>295514</td><td>196500</td><td>1360805</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td>85343</td><td>125606</td><td>114161</td><td>110516</td><td>63600</td><td>492740</td></tr><tr><td>HIMA</td><td>26347</td><td>19574</td><td>45610</td><td>122320</td><td>143479</td><td>67232</td><td>21960</td><td>444205</td></tr><tr><td>Leapmotor</td><td></td><td></td><td>50257</td><td>82036</td><td>67357</td><td>59173</td><td>45200</td><td>300080</td></tr><tr><td>Tesla</td><td>30271</td><td>32614</td><td>60929</td><td>61914</td><td>57371</td><td>54214</td><td>28370</td><td>322570</td></tr><tr><td>Nio</td><td>15817</td><td>13400</td><td>38190</td><td>44025</td><td>86183</td><td>76636</td><td>32400</td><td>303565</td></tr><tr><td>Li Auto</td><td>18243</td><td>14614</td><td>26851</td><td>36401</td><td>43150</td><td>29609</td><td>23600</td><td>190840</td></tr><tr><td>Xiaomi</td><td>5529</td><td>10171</td><td>60587</td><td>33513</td><td>33980</td><td>27263</td><td>18400</td><td>187900</td></tr><tr><td>XPeng</td><td>16957</td><td>14597</td><td>41607</td><td>39394</td><td>54514</td><td>36059</td><td>73020</td><td>274220</td></tr><tr><td>SUM</td><td>236699</td><td>201519</td><td>661556</td><td>769108</td><td>797539</td><td>756215</td><td>503050</td><td>3876925</td></tr><tr><td colspan="9">YoY (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-57%</td><td>-64%</td><td>-31%</td><td>-29%</td><td>-41%</td><td>-14%</td><td>-17%</td><td>-37%</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HIMA</td><td>-25%</td><td>-22%</td><td>-21%</td><td>14%</td><td>154%</td><td>58%</td><td>-20%</td><td>27%</td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tesla</td><td>-37%</td><td>-37%</td><td>2%</td><td>55%</td><td>55%</td><td>4%</td><td>-38%</td><td>-3%</td></tr><tr><td>Nio</td><td>-9%</td><td>-2%</td><td>97%</td><td>24%</td><td>190%</td><td>248%</td><td>83%</td><td>96%</td></tr><tr><td>Li Auto</td><td>-47%</td><td>-46%</td><td>-20%</td><td>-9%</td><td>-19%</td><td>-21%</td><td>-16%</td><td>-24%</td></tr><tr><td>Xiaomi</td><td>-86%</td><td>-79%</td><td>-27%</td><td>-5%</td><td>51%</td><td>-91%</td><td>-81%</td><td>-70%</td></tr><tr><td>XPeng</td><td>-18%</td><td>-41%</td><td>-26%</td><td>7%</td><td>18%</td><td>-21%</td><td>40%</td><td>-2%</td></tr><tr><td>SUM</td><td>-51%</td><td>-56%</td><td>-22%</td><td>-8%</td><td>6%</td><td>-31%</td><td>-22%</td><td>-25%</td></tr><tr><td colspan="9">MoM (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-56%</td><td>-22%</td><td>161%</td><td>-11%</td><td>-12%</td><td>50%</td><td></td><td></td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td>47%</td><td>-9%</td><td>-3%</td><td></td><td></td></tr><tr><td>HIMA</td><td>-52%</td><td>-26%</td><td>133%</td><td>168%</td><td>17%</td><td>-53%</td><td></td><td></td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td>63%</td><td>-18%</td><td>-12%</td><td></td><td></td></tr><tr><td>Tesla</td><td>-39%</td><td>8%</td><td>87%</td><td>2%</td><td>-7%</td><td>-6%</td><td></td><td></td></tr><tr><td>Nio</td><td>-49%</td><td>-15%</td><td>185%</td><td>15%</td><td>96%</td><td>-11%</td><td></td><td></td></tr><tr><td>Li Auto</td><td>-28%</td><td>-20%</td><td>84%</td><td>36%</td><td>19%</td><td>-31%</td><td></td><td></td></tr><tr><td>Xiaomi</td><td>-63%</td><td>84%</td><td>495%</td><td>-45%</td><td>1%</td><td>-20%</td><td></td><td></td></tr><tr><td>XPeng</td><td>-48%</td><td>-14%</td><td>185%</td><td>-5%</td><td>38%</td><td>-34%</td><td></td><td></td></tr><tr><td>SUM</td><td>-51%</td><td>-15%</td><td>161%</td><td>16%</td><td>4%</td><td>-5%</td><td></td><td></td></tr></table>

Source: ThinkerCar, Data compiled by GS Global Investment Research

<table><tr><td>2025</td><td>2025</td><td>2025</td><td>2025</td><td>2026</td><td>2026</td><td>2026</td><td>2026</td></tr><tr><td>W266/23-6/29</td><td>W276/30-7/6</td><td>W287/7-7/13</td><td>W297/14-7/20</td><td>W266/22-6/28</td><td>W276/29-7/5</td><td>W287/6-7/12</td><td>W297/13-7/19</td></tr><tr><td colspan="8">Weekly order (units)</td></tr><tr><td>82000</td><td>78000</td><td>75000</td><td>85000</td><td>70600</td><td>86500</td><td>62100</td><td>47900</td></tr><tr><td></td><td></td><td></td><td></td><td>28250</td><td>22700</td><td>20000</td><td>20900</td></tr><tr><td>10000</td><td>9900</td><td>9500</td><td>8000</td><td>10820</td><td>8110</td><td>6800</td><td>7050</td></tr><tr><td></td><td></td><td></td><td></td><td>15000</td><td>13800</td><td>15200</td><td>16200</td></tr><tr><td>11600</td><td>17000</td><td>14000</td><td>15000</td><td>11200</td><td>10900</td><td>9270</td><td>8200</td></tr><tr><td>5000</td><td>5500</td><td>5700</td><td>6500</td><td>11600</td><td>10800</td><td>12200</td><td>9400</td></tr><tr><td>7600</td><td>9500</td><td>9000</td><td>9500</td><td>9900</td><td>5700</td><td>5400</td><td>12500</td></tr><tr><td>283000</td><td>78500</td><td>9800</td><td>9000</td><td>6100</td><td>5400</td><td>5600</td><td>7400</td></tr><tr><td>9400</td><td>28600</td><td>11500</td><td>12000</td><td>7300</td><td>6750</td><td>7070</td><td>59200</td></tr><tr><td>408600</td><td>227000</td><td>134500</td><td>145000</td><td>170770</td><td>170660</td><td>143640</td><td>188750</td></tr><tr><td colspan="8">YoY (%)</td></tr><tr><td></td><td></td><td></td><td></td><td>-14%</td><td>11%</td><td>-17%</td><td>-44%</td></tr><tr><td></td><td></td><td></td><td></td><td>8%</td><td>-18%</td><td>-28%</td><td>-12%</td></tr><tr><td></td><td></td><td></td><td></td><td>-3%</td><td>-36%</td><td>-34%</td><td>-45%</td></tr><tr><td></td><td></td><td></td><td></td><td>132%</td><td>96%</td><td>114%</td><td>45%</td></tr><tr><td></td><td></td><td></td><td></td><td>30%</td><td>-40%</td><td>-40%</td><td>32%</td></tr><tr><td></td><td></td><td></td><td></td><td>-98%</td><td>-93%</td><td>-43%</td><td>-18%</td></tr><tr><td></td><td></td><td></td><td></td><td>-22%</td><td>-76%</td><td>-39%</td><td>393%</td></tr><tr><td></td><td></td><td></td><td></td><td>-69%</td><td>-41%</td><td>-19%</td><td>5%</td></tr><tr><td colspan="8">WoW (%)</td></tr><tr><td>2%</td><td>-5%</td><td>-4%</td><td>13%</td><td>-34%</td><td>23%</td><td>-28%</td><td>-23%</td></tr><tr><td></td><td></td><td></td><td></td><td>17%</td><td>-20%</td><td>-12%</td><td>4%</td></tr><tr><td>11%</td><td>-1%</td><td>-4%</td><td>-16%</td><td>-7%</td><td>-25%</td><td>-16%</td><td>4%</td></tr><tr><td></td><td></td><td></td><td></td><td>6%</td><td>-8%</td><td>10%</td><td>7%</td></tr><tr><td>-3%</td><td>47%</td><td>-18%</td><td>7%</td><td>-11%</td><td>-3%</td><td>-15%</td><td>-12%</td></tr><tr><td>2%</td><td>10%</td><td>4%</td><td>14%</td><td>-20%</td><td>-7%</td><td>13%</td><td>-23%</td></tr><tr><td>-16%</td><td>23%</td><td>-5%</td><td>6%</td><td>67%</td><td>-42%</td><td>-5%</td><td>131%</td></tr><tr><td>6975%</td><td>-72%</td><td>-88%</td><td>-8%</td><td>-15%</td><td>-11%</td><td>4%</td><td>32%</td></tr><tr><td>7%</td><td>204%</td><td>-60%</td><td>4%</td><td>-19%</td><td>-8%</td><td>5%</td><td>737%</td></tr><tr><td>220%</td><td>-44%</td><td>-41%</td><td>8%</td><td>-17%</td><td>0%</td><td>-16%</td><td>31%</td></tr></table>

## Key events to watch

## 2026 Week 30, Jul 20-26

■ Jul 21: Weekly order for new-launched models.

■ Jul 23: Lynk to launch Lynk 07 GT.

## 2026 Week 31, Jul 27-Aug 2

■ Jul 28: Zeekr to launch five-seater 9X.

■ Jul 30: Xiaomi to host SkyNomad tech event.

■ Aug 1: NEV OEM monthly volume release.

## 2026 Week 32, Aug 3-9

■ Aug 8: Avatr to launch Avatr 07 L.

## 2026 Week 33-35, Aug 10-30

■ Aug 10-11: CPCA will release PV/NEV industry and by model wholesale/retail data.

## Retail end-pricing

■ NEV: average dealer discount vs. MSRP was 6.94% as of Jul 18, vs. 7.29%/8.13% as of Jul 11, 2026/Jul 28, 2025; BYD average dealer discount vs. MSRP was 3.95% as of Jul 18, vs. 4.10%/5.45% as of Jul 11, 2026/Jul 28, 2025.

ICE: average dealer discount vs. MSRP was 19.55% as of Jul 18, vs. 20.11%/21.37% as of Jul 11, 2026/Jul 28, 2025.

Exhibit 2: NEV dealer discount trend  
![](images/15fe966723668a5f1996f7bd006f6d14efdc68c22cca010689ca90da938ed3b4.jpg)  
By brand dealer discount is based on best-selling models.

![](images/d57873667b2a9231b205d9b74413dd77fd3ea3e4d7b27793e1ed5bcf713601f8.jpg)

![](images/741713e6ee564702d128777496b77e5cf85bf68b97eca106a6b5bc3a282363e9.jpg)

Source: Autohome, Data compiled by GS Global Investment Research  
Exhibit 3: ICE dealer discount trend  
![](images/9e78925b635652020eb0ec228b41b509611055ac9dc39060be0b28631d770ffb.jpg)  
By brand dealer discount is based on best-selling models.

![](images/9b9016a1a32c5806e7cd6b97c58430bb7d00dfecfb86e36d74f9a7d9150a2b5c.jpg)

ICE dealer discount - domestic brand  
![](images/efdb36dfa70f0c49185e89071be0e949d3664e71cead05eed87a21518fc97165.jpg)

## Upstream battery pricing dynamics

Battery grade lithium carbonate price is unchanged at Rmb153k/ton (+0.0% wow), while prismatic cell (LFP) and prismatic cell (NCM) prices were stable wow.

Exhibit 4: Battery and battery raw materials prices

<table><tr><td>Material</td><td>Unit</td><td>5/6/2026</td><td>5/11/2026</td><td>5/18/2026</td><td>5/25/2026</td><td>6/1/2026</td><td>6/8/2026</td><td>6/13/2026</td><td>6/22/2026</td><td>6/29/2026</td><td>7/6/2026</td><td>7/13/2026</td><td>7/20/2026</td><td>WoW</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>Cathode</td><td>Unit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Lithium Carbonate (battery grade)</td><td>Rmb k / ton</td><td>177.0</td><td>190.0</td><td>191.0</td><td>181.0</td><td>179.5</td><td>168.5</td><td>174.5</td><td>167.5</td><td>151.5</td><td>165.0</td><td>153.0</td><td>153.0</td><td>0.0%</td><td>112%</td><td>74%</td><td>-4%</td><td>1%</td></tr><tr><td>Battery</td><td>Unit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prismatic cell (LFP)</td><td>Rmb / Wh</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.0%</td><td>14%</td><td>14%</td><td>4%</td><td>0%</td></tr><tr><td>Prismatic cell (NCM)</td><td>Rmb / Wh</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.0%</td><td>13%</td><td>10%</td><td>0%</td><td>0%</td></tr></table>

Source: ICC Sino, Data compiled by GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Tina Hou and Jenny Du, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Tina Hou GS (China) Securities Company Limited, Jenny Du GS (China) Securities Company Limited.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-sha

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
