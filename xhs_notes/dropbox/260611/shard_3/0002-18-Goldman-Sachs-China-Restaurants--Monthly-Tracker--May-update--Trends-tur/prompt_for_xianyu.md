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
# China Restaurants: Monthly Tracker: May update: Trends turn softer but divergence across brands; FMD high base effect kicking in

May SSSG performance was sequentially softer from Apr, with moderate demand during the Labor Day holiday and softness in consumption sentiment/weather headwinds. By brand, Haidilao's table turn turned to slightly negative growth yoy (vs. yoy stable growth during Labor Day), implying low-mid 80% recovery compared to the 2019 level (slightly higher than Apr yet remains below the 1Q level); Tai Er recorded SSSG of low DD%, slightly lower than Apr with weather headwinds during Labor Day (SSSG up MSD%-HSD%), but post holiday SSSG has picked up. For freshly made drinks (FMD), high base impact has started to kick in, and brands have generally seen SSSG pressure in May on a yoy basis. We continue to see performance divergence across brands, e.g. Nayuki per store sales decline further expanded to 24% yoy (vs. -11% in Apr), while leading brands were more resilient with support from category expansion/new products. On the bright side, multiple brands commented that delivery mix declined sequentially and/or on a yoy basis. On pricing, our tracker suggests more pricing activities were introduced in coffee from freshly made tea brands (e.g. Guming launched weekly Rmb9.9 coupon, Mixue launched a buy-one-get-one free coupon for stores that introduced coffee machines), to educate customers and drive dine-in sales; Luckin also launched a daily Rmb9.9 offering for select SKUs across categories. All said, promotion magnitude/scale remains disciplined in our view. For restaurant brands we track, Jiumaojiu and Haidilao both saw stable pricing trends.

In this note, we provide updates on a variety of high-frequency indicators, including air traffic run rate, and commodity inflation. We also include competition environment updates, key company news and key reports published over the past month for covered China Restaurants names and peers.

## Brand performance

1. Haidilao (6862.HK; Neutral): Haidilao's average table turn turned to slightly negative in May, vs. a MSD% increase in Apr from a low base. Management believes the calendar shift of the Dragon Boat festival (1 day in May in 2025) was a headwind for May performance. Based on our calculation, this implies a \~3.8x table turn, or 3.5x\~3.6x post Labor Day holiday which is a similar table turn level compared to Apr. This implies a low-mid 80% recovery level compared to 2019, slightly better than \~80% for Apr but remains lower than 1Q. Haidilao opened 4 company stores and 1 franchise store, and closed 4 company stores in May.

## Michelle Cheng

+852-2978-6631

michelle.cheng@gs.com

GS (Asia) L.L.C.

## Xinyu Ruan

+852-2978-7347 | xinyu.ruan@gs.com

GS (Asia) L.L.C.

## Molly Dai

+852-3966-4000 | molly.dai@gs.com

GS (Asia) L.L.C.

## Carol Chen

+852-2978-7999 | carol.chen@gs.com

GS (Asia) L.L.C.

## Keira Liu

+852-2978-0473 | keira.liu@gs.com

GS (Asia) L.L.C.

GS read: Table turn performance remained relatively soft, and post-holiday growth slightly decelerated (vs. stable table turn in Labor Day), but we believe market expectation has also come down considering softness in overall consumption/weather headwinds. YTD average table turn increase of LSD% is slightly tracking behind GSe which assumes 4% per store sales growth yoy.

2. Jiumaojiu (9922.HK, Buy): Tai Er recorded LDD% SSSG in ML China, which slightly declined from Apr yet remained above the 1Q level (10.9% SSSG in ML China). This implies a post holiday acceleration compared to MSD%-HSD% SSSG during the Labor Day holiday when rainy weather in South China was a headwind. New model stores continued to drive growth, while old models continued to see positive SSSG, also recording LSD%-MSD% SSSG in May. For Jiumaojiu and Song, pressure lingered and SSSG trends remained similar to 1Q (-20%/-11% for Song/Jiumaojiu respectively).

GS read: Tai Er continues to see solid SSSG performance despite the fluid consumption in May, and the post-holiday improvement shows momentum of its new model/fresh product strategy. That said, Song/Jiumaojiu brands are still seeing pressure despite their base being sequentially easier compared to 1Q. Compared to GSe, Tai Er/Jiumaojiu are largely on track, while Song is tracking behind our 1H26 expectation.

3. Gourmet Master (2723.TW; Neutral): ML China sales decline remained significant at -46% yoy (Apr: -48%), with store count sequentially stable at 290-300 which implies a >30% yoy decline and transition to franchised stores. In the US market, sales growth has been sequentially accelerating in Apr-May (sales in local currency up 4%/8% yoy) post the weather headwinds in 1Q26, and the company expects store count to reach 95 (3 expected to be opened in Jun)/>100 by mid/end of 2026.

GS read: The sales decline in Apr-May at high 40%s in ML China iss tracking behind GSe (\~-40% yoy decline). While in the US market, Apr-May sales growth is slightly ahead of GSe (MSD% growth in local currency), and store openings have been on track with GSe.

Exhibit 1: Haidilao/Tai Er May SSSG decelerated; FMD players generally seeing SSSG pressure due to a tough base

<table><tr><td></td><td>Jan 25</td><td>Feb 25</td><td>Mar 25</td><td>Apr 25</td><td>May 25</td><td>Jun 25</td><td>Jul 25</td><td>Aug 25</td><td>Sep 25</td><td>25-Oct</td><td>25-Nov</td><td>25-Dec</td><td>26-Jan</td><td>26-Feb</td><td>26-Mar</td><td>26-Apr</td><td>26-May</td><td>Apr-May</td><td>CNY 2023</td><td>Labor Day 2023</td><td>National Day 2023</td><td>CNY 2024</td><td>Labor Day 2024</td><td>National Day 2024</td><td>CNY 2025</td><td>Labor Day 2025</td><td>National Day 2025</td><td>CNY 2026</td><td>Labor Day 2026</td><td></td></tr><tr><td colspan="30">SSSG</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>0%</td><td>-8%</td><td>-9%</td><td>-13%</td><td>-6%</td><td>-7%</td><td>0%</td><td>1%</td><td>-2%</td><td>2%</td><td>-1%</td><td>-1%</td><td>-5%</td><td>13%</td><td>1%</td><td>5%</td><td>-1%</td><td>2%</td><td>-10%</td><td>40%</td><td>25%</td><td>40%</td><td>20%</td><td>0%</td><td>-5%</td><td>-10%</td><td>0%</td><td>5%</td><td>0%</td><td></td></tr><tr><td>Tai Er</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>LSD% decl</td><td></td><td>HSD%</td><td>MSD%</td><td>DD%</td><td>LDD%</td><td>DD%</td><td>LDD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>low teens decline</td><td></td><td>HSD%</td><td></td></tr><tr><td>Nayuki</td><td>-8%</td><td>-13%</td><td>-7%</td><td>3%</td><td>14%</td><td>13%</td><td>22%</td><td>8%</td><td>0%</td><td>-1%</td><td>10%</td><td>0%</td><td></td><td></td><td>-3%</td><td>-11%</td><td></td><td></td><td>-10%</td><td>30%</td><td>-14%</td><td>-20%</td><td>-20%</td><td>-23%</td><td></td><td>20%</td><td></td><td></td><td>-30%</td><td></td></tr><tr><td>Nayuki (average sales per store)</td><td></td><td></td><td></td><td></td><td>20%</td><td>20%</td><td>29%</td><td>15%</td><td>5%</td><td>3%</td><td>13%</td><td>3%</td><td></td><td></td><td>-1%</td><td>-11%</td><td>-24%</td><td>-18%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Guming</td><td>+LSD%</td><td></td><td></td><td>Acceleration</td><td>DD</td><td>DD</td><td colspan="2">&gt;20% (GMV)</td><td>~20% (GMV)</td><td>No slower vs. Sep</td><td></td><td>Slightly slower vs. Oct</td><td>DD%</td><td>SD%</td><td>&gt;20%</td><td>HSD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td></td></tr><tr><td>ChaPanda</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD%</td><td>DD%</td><td>~25%</td><td>SD%</td><td>DD%</td><td>SD%</td><td>SD%</td><td>Decline</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td>decline</td><td></td></tr><tr><td>Auntea Jenny</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>close to 20%</td><td></td><td>Slower than 1Q26</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Slower than Apr-26</td><td></td></tr><tr><td colspan="30">SSS vs. 2021</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>27%</td><td>18%</td><td>23%</td><td>17%</td><td>27%</td><td>52%</td><td>34%</td><td>52%</td><td>17%</td><td>15%</td><td>32%</td><td>26%</td><td>21%</td><td>33%</td><td>24%</td><td>23%</td><td>26%</td><td>24%</td><td>-16%</td><td>5%</td><td>5%</td><td>18%</td><td>26%</td><td>5%</td><td>12%</td><td>14%</td><td>5%</td><td>17%</td><td>14%</td><td></td></tr><tr><td>Nayuki</td><td>-50%</td><td>-54%</td><td>-48%</td><td>-47%</td><td>-41%</td><td>-40%</td><td>-41%</td><td>-28%</td><td>-43%</td><td>-47%</td><td>-38%</td><td>-52%</td><td></td><td></td><td>-49%</td><td>-53%</td><td>-55%</td><td>-54%</td><td>-30%</td><td>-20%</td><td>-31%</td><td>-44%</td><td>-36%</td><td>-47%</td><td></td><td>-23%</td><td></td><td></td><td>-46%</td><td></td></tr><tr><td>Gourmet Master</td><td>-33%</td><td>-27%</td><td>-22%</td><td>-23%</td><td>-28%</td><td>-31%</td><td>-35%</td><td>-34%</td><td>-32%</td><td>-33%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-18%</td><td>-21%</td><td>-15%</td><td>-18%</td><td>-14%</td><td>-6%</td><td>-14%</td><td>-4%</td><td>-19%</td><td>-22%</td><td>-3%</td><td>-13%</td><td></td><td></td><td>-12%</td><td>-15%</td><td>-15%</td><td>-15%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of 2021</td><td>82%</td><td>79%</td><td>85%</td><td>82%</td><td>86%</td><td>94%</td><td>86%</td><td>96%</td><td>81%</td><td>78%</td><td>97%</td><td>87%</td><td></td><td></td><td>88%</td><td>85%</td><td>85%</td><td>85%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="30">SSS vs. 2019</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>-12%</td><td>-12%</td><td>-14%</td><td>-24%</td><td>-15%</td><td>-19%</td><td>-20%</td><td>-19%</td><td>-29%</td><td>-15%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-18%</td><td>-37%</td><td>-24%</td><td>-10%</td><td>-12%</td><td>-8%</td><td>-10%</td><td>-16%</td><td>-18%</td><td>-10%</td><td>-12%</td><td>-18%</td><td></td></tr><tr><td>Gourmet Master</td><td>-34%</td><td>-29%</td><td>-26%</td><td>-29%</td><td>-35%</td><td>-38%</td><td>-42%</td><td>-39%</td><td>-39%</td><td>-39%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-23%</td><td>-20%</td><td>-20%</td><td>-26%</td><td>-25%</td><td>-29%</td><td>-31%</td><td>-29%</td><td>-34%</td><td>-27%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-18%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of pre-COVID</td><td>77%</td><td>80%</td><td>80%</td><td>74%</td><td>75%</td><td>71%</td><td>69%</td><td>71%</td><td>66%</td><td>73%</td><td>83%</td><td>83%</td><td>84%</td><td>100%</td><td>87%</td><td>80%</td><td>84%</td><td>82%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data

Exhibit 2: Quarterly SSSG tracker

<table><tr><td colspan="10">SSSG yoy trend</td><td colspan="10">vs. 2019</td></tr><tr><td>SSSG yoy</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td></td></tr><tr><td>KFC China</td><td>-2.0%</td><td>-3.0%</td><td>-2.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>2.0%</td><td>3.0%</td><td>1.0%</td><td>-10%</td><td>-12%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-11%</td><td>-10%</td><td>-14%</td><td>-9%</td><td></td></tr><tr><td>Pizza Hut China</td><td>-5.0%</td><td>-8.0%</td><td>-6.0%</td><td>-2.0%</td><td>0.0%</td><td>2.0%</td><td>1.0%</td><td>1.0%</td><td>-1.0%</td><td>-8%</td><td>-14%</td><td>-14%</td><td>-16%</td><td>-8%</td><td>-12%</td><td>-13%</td><td>-16%</td><td>-9%</td><td></td></tr><tr><td>YUM China</td><td>-3.0%</td><td>-4.0%</td><td>-3.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>1.0%</td><td>3.0%</td><td>0.0%</td><td>-10%</td><td>-13%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-12%</td><td>-11%</td><td>-13%</td><td>-10%</td><td></td></tr><tr><td>Starbucks China</td><td>-11.0%</td><td>-14.0%</td><td>-14.0%</td><td>-6.0%</td><td>0.0%</td><td>2.0%</td><td>2.0%</td><td>7.0%</td><td>0.5%</td><td>-33%</td><td>-32%</td><td>-32%</td><td>-34%</td><td>-33%</td><td>-31%</td><td>-30%</td><td>-29%</td><td>-32%</td><td></td></tr><tr><td>Gourmet Master China</td><td>-15.7%</td><td>-16.7%</td><td>-15.2%</td><td>-9.7%</td><td>-9.7%</td><td>-4.0%</td><td>-7.7%</td><td>-10.0%</td><td></td><td>-26%</td><td>-31%</td><td>-35%</td><td>-28%</td><td>-33%</td><td>-34%</td><td>-40%</td><td>-36%</td><td>-33%</td><td></td></tr><tr><td>Xiabuxiabu</td><td>-19.0%</td><td></td><td>-27.6%</td><td></td><td>-15.6%</td><td></td><td></td><td>-3.6%</td><td></td><td></td><td>-55%</td><td></td><td>-54%</td><td></td><td>-62%</td><td></td><td></td><td></td><td></td></tr><tr><td>Coucou</td><td>-43.0%</td><td></td><td>-21.0%</td><td></td><td>-14.0%</td><td></td><td></td><td>-14.4%</td><td></td><td></td><td>-57%</td><td></td><td>-61%</td><td></td><td>-63%</td><td></td><td></td><td></td><td></td></tr><tr><td>Haidilao</td><td>14.5%</td><td></td><td>-4.6%</td><td></td><td>14.5%</td><td></td><td></td><td>-3.0%</td><td>2.0%</td><td></td><td>-16%</td><td></td><td>-22%</td><td></td><td>-4%</td><td></td><td>-24%</td><td></td><td></td></tr><tr><td>Jiu Mao Jiu</td><td>-4.1%</td><td>-12.6%</td><td>-10.3%</td><td>-18.5%</td><td>-18.6%</td><td>-18.5%</td><td>-14.8%</td><td>-16.4%</td><td>-11.3%</td><td>-26%</td><td>-29%</td><td>-26%</td><td>-38%</td><td>-40%</td><td>-43%</td><td>-37%</td><td>-48%</td><td>-47%</td><td></td></tr><tr><td>Tai Er</td><td>-13.9%</td><td>-18.1%</td><td>-18.3%</td><td>-24.6%</td><td>-21.2%</td><td>-13.7%</td><td>-9.3%</td><td>-3.0%</td><td>6.9%</td><td>-24%</td><td>-33%</td><td>-32%</td><td>-41%</td><td>-40%</td><td>-42%</td><td>-38%</td><td>-43%</td><td>-36%</td><td></td></tr><tr><td>Tai Er - China</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Song</td><td>-34.8%</td><td>-36.6%</td><td>-32.5%</td><td>-26.9%</td><td>-24.2%</td><td>-14.3%</td><td>-19.1%</td><td>-19.0%</td><td>-19.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Helens</td><td>-29.7%</td><td></td><td>-12.9%</td><td></td><td>-17.9%</td><td></td><td></td><td>-18.9%</td><td></td><td></td><td>-48%</td><td></td><td>-43%</td><td></td><td>-58%</td><td></td><td>-54%</td><td></td><td></td></tr><tr><td>Nayuki</td><td>-28.5%</td><td></td><td>-21.3%</td><td></td><td>-9.3%</td><td>10.0%</td><td>10.0%</td><td>3.0%</td><td>LSD%</td><td></td><td>-47%</td><td></td><td>-44%</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Juewei</td><td>-13.7%</td><td>-11.0%</td><td>-5.5%</td><td>-21.5%<

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
