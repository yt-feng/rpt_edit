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
# China Restaurants: Monthly Tracker: Jun update: weakness continued with weather headwind; FMD relatively resilient despite high base

Jun SSSG performance remained weak, with weather also a headwind during the month. By brand, Haidilao table turn was stable vs. May at \~3.8x implying LSD% yoy decline; this translates to \~80% recovery compared to 2019, below low-mid 80% in May and similar to Apr levels. Jiumaojiu's Tai Er brand SSSG moderated to MSD% in Jun, impacted by unfavorable weather in the last week of Jun (the first three weeks of Jun saw DD% SSSG). For freshly made drinks (FMD), while SSSG faced yoy pressure from last year's tough base, several brands showed SSSG resiliency/sequential improvement which is better than market had worried. For example, ChaPanda SSSG in Jun sequentially improved to slight LSD% decline in Jun, supported by coffee roll-out/campaign and successful products like Iced Lychee Milk. Guming SSSG also improved to slightly LSD% decline, partially thanks to promotion calendar shift (buy one get one free campaign in Jun vs. last year in May). Chagee SSSG/per store GMV in Jun was also sequentially better than May, with support from new product launches. On pricing, while promotions picked up compared to May, it was mainly impacted by promotion calendar (i.e. Guming's buy one get one free, Luckin's Rmb9.9 campaign for select SKUs, PH's regular buffet campaign), and the magnitude of promotion remains disciplined.

In this note, we provide updates on a variety of high-frequency indicators, including air traffic run rate, and commodity inflation. We also include competition environment updates, key company news and key reports published over the past month for covered China Restaurants names and peers.

## Brand performance

1. Haidilao (6862.HK; Neutral): Haidilao's average table turn was sequentially stable, or down LSD% in Jun. This implies a \~3.8x table turn, implying \~80% recovery level compared to 2019, lower than low-mid 80% in May and similar to Apr level. Haidilao opened 5 company stores and 2 franchise stores, and closed 6 company stores in Jun.

GS read: Table turn performance remained relatively soft, and 1H26 average table turn increase of \~2% is behind GSe which assumes 4% per store sales growth yoy, though market expectation also stepped down amid overall consumption softness. The brand net closed 8 stores in 1H which is lower than GSe of 23 net opening (excl. transfer to franchised stores); while newly opened franchised store of 14 in 1H is ahead of GSe of 8.

Michelle Cheng  
+852-2978-6631 |  
michelle.cheng@gs.com  
GS (Asia) L.L.C.

Xinyu Ruan  
+852-2978-7347 | xinyu.ruan@gs.com  
GS (Asia) L.L.C.

Molly Dai  
+852-3966-4000 | molly.dai@gs.com  
GS (Asia) L.L.C.

Carol Chen
+852-2978-7999 | carol.chen@gs.com
GS (Asia) L.L.C.

Keira Liu  
+852-2978-0473 | keira.liu@gs.com  
GS (Asia) L.L.C.

2. Guming (1364.HK; Buy on CL): SSSG significantly improved from May, with benefits from promotion calendar shift (i.e. buy one get one free offered in Jun compared to May last year).

GS read: We believe Guming's SSSG in Jun was better than market expectation. Compared to lowered market expectation for the full year SSSG, we are more positive (we look for flat SSSG in 2026E) with continuous coffee category expansion and launch of differentiated new products. However, store opening is weaker than company's expectation earlier this year.

3. Chagee (CHA; Neutral): Jun monthly average GMV was above Rmb350k with some sequential increase in both SSSG and GMV level, with support from new product launches (e.g. new products beer-like tea (流沙茶) and lemon milk tea has \~15% GMV contribution).

GS read: SSSG in 2Q was largely in line with GSe of -13% yoy implying sequentially improvement in Jun vs. Apr-May at mid-teens% decline. With support from new product launches and peak season, we expect the SSSG improvement trend to continue into 3Q which has a low base. That said, continuous SSSG improvement/turnaround will depend on whether the brand is able to launch successful new products.

4. Jiumaojiu (9922.HK, Buy): Tai Er recorded MSD% SSSG in ML China in Jun, decelerated from DD%/low-DD% in Apr/May, negatively impacted by weather headwinds (in first three weeks, SSSG was at DD%); overseas remained a drag on overall SSSG. New model saw HDD% SSSG in Jun, while legacy stores were broadly flat. Tai Er opened a new 6.0 model with upgraded decoration and menu, and initial sales was \~30%-40% higher than the old format in the first week. Jiumaojiu brand SSSG decline narrowed to -HSD% in Jun, with support from new format stores; while Song SSSG remained under pressure.

In 2Q26, Jiumaojiu reported mixed 2Q26 results (Exhibit 4). Tai Er China SSSG slightly accelerated to 12% (vs 1Q26: +11%) supported by c.1% ASP increase while Tai Er other regions' SSSG -17% yoy (vs 1Q26: -14%) with c.3% ASP decline; Jiumaojiu brand SSSG decelerated to -14% yoy (vs 1Q26: -11%) with flat ASP; Song brand SSSG decelerated to -26% yoy (vs 1Q26: -20%) despite c.6% ASP growth. On store network, Tai Er net closed 5 stores in 2Q26 or 23 stores in 1H26, including 0/1 net addition of franchised stores in 2Q26/1H26. As of Jun 30, 340 stores were upgraded to "Fresh" Model in ML China (vs 477 in total). Jiumaojiu brand net closed 1/2 stores in 2Q26/1H26, with the number of franchised store flat in 2Q26/1H26. In addition, 6 out of 61 Jiumaojiu stores were new-model stores by Jun-end. Song net decreased 5/8 stores in 2Q26/1H26. Shanwaimian net closed 3 stores in 2Q26 or 6 stores in 1H26, all related to franchise stores. Other brands (Lai Mei Li, Fresh Wood, Chaonabian) maintained store count at 1 as of Jun 30, 2026.

GS read: While Tai Er's SSSG decelerated in Jun under weather headwinds, the performance of new store formats remained solid and if 6.0 model is tested successfully, it could benefit store productivity increase ahead. Compared to GSe, considering the drag from overseas, SSSG is tracking slightly behind GSe implied low teens% in 2Q; Jiumaojiu is slightly tracking ahead, while Song is tracking behind of GSe.

5. Gourmet Master (2723.TW; Neutral): ML China sales decline remained significant at -46% yoy (May: -46%), with store count sequentially stable at 290-300 which implies a >30% yoy decline and transition to franchised stores. In US market, sales growth was

4.9% in Jun (vs, 8% in May), and store count reached 95 with 3 net additions in Jun.

GS read: The sales decline in 2Q at high 40%s in ML China was behind GSe (\~-40% yoy decline). In US market, sales growth in local currency of 6% yoy was largely in line with GSe; while in Taiwan market, 2Q growth of >15% implies sequential acceleration and was ahead of GSe.

Exhibit 1: Haidilao/Tai Er SSSG was stable/sequentially slower in Jun; several FMD players saw SSSG improvement thanks to new products/category expansion

<table><tr><td></td><td>Jan 25</td><td>Feb 25</td><td>Mar 25</td><td>Apr 25</td><td>May 25</td><td>Jun 25</td><td>Jul 25</td><td>Aug 25</td><td>Sep 25</td><td>25-Oct</td><td>25-Nov</td><td>25-Dec</td><td>26-Jan</td><td>26-Feb</td><td>26-Mar</td><td>26-Apr</td><td>26-May</td><td>26-Jun</td><td>2Q26</td><td>CNY 2023</td><td>Labor Day 2023</td><td>National Day 2023</td><td>CNY 2024</td><td>Labor Day 2024</td><td>National Day 2024</td><td>CNY 2025</td><td>Labor Day 2025</td><td>National Day 2025</td><td>CNY 2026</td><td>Labor Day 2026</td></tr><tr><td colspan="31">SSSG</td></tr><tr><td>Haidiao (avg. tabletum)</td><td>0%</td><td>-8%</td><td>-9%</td><td>-13%</td><td>-6%</td><td>-7%</td><td>0%</td><td>1%</td><td>-2%</td><td>2%</td><td>-1%</td><td>-1%</td><td>-5%</td><td>13%</td><td>1%</td><td>5%</td><td>-1%</td><td>-2%</td><td>1%</td><td>-10%</td><td>40%</td><td>25%</td><td>40%</td><td>20%</td><td>0%</td><td>-5%</td><td>-10%</td><td>0%</td><td>5%</td><td>0%</td></tr><tr><td>Tai Er</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>LSD% decl</td><td>HSD%</td><td></td><td>MSD%</td><td>DD%</td><td>LDD%</td><td>DD%</td><td>LDD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>low teens decline</td><td>HSD%</td><td>M-HSD%</td></tr><tr><td>Xiaoiayuan (YTD SSSG)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-mid-teens%</td><td></td><td>-LDD%</td><td>-LDD%</td><td>-LDD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Nayuki</td><td>-8%</td><td>-13%</td><td>-7%</td><td>3%</td><td>14%</td><td>13%</td><td>22%</td><td>8%</td><td>0%</td><td>-1%</td><td>10%</td><td>0%</td><td></td><td></td><td>-3%</td><td>-11%</td><td></td><td></td><td></td><td>-10%</td><td>30%</td><td>-14%</td><td>-20%</td><td>-20%</td><td>-23%</td><td></td><td>20%</td><td></td><td></td><td>-30%</td></tr><tr><td>Nayuki (average sales per store)</td><td></td><td></td><td></td><td></td><td>20%</td><td>20%</td><td>29%</td><td>15%</td><td>5%</td><td>3%</td><td>13%</td><td>3%</td><td></td><td></td><td>-1%</td><td>-11%</td><td>-24%</td><td></td><td>-22%</td><td>-19%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Guming</td><td>+LSD%</td><td></td><td></td><td>Acceleration</td><td>DD</td><td>DD</td><td>&gt;20% (GMV)</td><td></td><td>~20% (GMV)</td><td>No slower vs. Sep</td><td>Slightly slower vs. Oct</td><td>DD%</td><td>SD%</td><td>&gt;20%</td><td>HSD%</td><td>-LSD%</td><td>-HSD%</td><td></td><td>-slight LSD%</td><td>within -5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td></td></tr><tr><td>Chagee</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-mid teens %</td><td></td><td>-mid teens%</td><td>-low teens%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ChaPanda</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD%</td><td>DD%</td><td>~25%</td><td>SD%</td><td>DD%</td><td>SD%</td><td>SD%</td><td>Decline</td><td>-slight LSD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td>decline</td></tr><tr><td>Auntea Jenny</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>close to 20%</td><td></td><td>Slower than 1Q26</td><td>Decline</td><td>Decline</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Slower than Apr-26</td></tr><tr><td colspan="31">SSS vs. 2021</td></tr><tr><td>Haidiao (avg. tabletum)</td><td>27%</td><td>18%</td><td>23%</td><td>17%</td><td>27%</td><td>52%</td><td>34%</td><td>52%</td><td>17%</td><td>15%</td><td>32%</td><td>26%</td><td>21%</td><td>33%</td><td>24%</td><td>23%</td><td>26%</td><td>49%</td><td>33%</td><td>-16%</td><td>5%</td><td>5%</td><td>18%</td><td>26%</td><td>5%</td><td>12%</td><td>14%</td><td>5%</td><td>17%</td><td>14%</td></tr><tr><td>Nayuki</td><td>-50%</td><td>-54%</td><td>-48%</td><td>-47%</td><td>-41%</td><td>-40%</td><td>-41%</td><td>-28%</td><td>-43%</td><td>-47%</td><td>-38%</td><td>-52%</td><td></td><td></td><td>-49%</td><td>-53%</td><td>-55%</td><td>-53%</td><td>-54%</td><td>-30%</td><td>-20%</td><td>-31%</td><td>-44%</td><td>-36%</td><td>-47%</td><td></td><td>-23%</td><td></td><td></td><td>-46%</td></tr><tr><td>Gourmet Master</td><td>-33%</td><td>-27%</td><td>-22%</td><td>-23%</td><td>-28%</td><td>-31%</td><td>-35%</td><td>-34%</td><td>-32%</td><td>-33%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-18%</td><td>-21%</td><td>-15%</td><td>-18%</td><td>-14%</td><td>-6%</td><td>-14%</td><td>-4%</td><td>-19%</td><td>-22%</td><td>-3%</td><td>-13%</td><td></td><td></td><td>-12%</td><td>-15%</td><td>-15%</td><td>-2%</td><td>-11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of 2021</td><td>82%</td><td>79%</td><td>85%</td><td>82%</td><td>86%</td><td>94%</td><td>86%</td><td>96%</td><td>81%</td><td>78%</td><td>97%</td><td>87%</td><td></td><td></td><td>88%</td><td>85%</td><td>85%</td><td>98%</td><td>89%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="31">SSS vs. 2019</td></tr><tr><td>Haidiao (avg. tabletum)</td><td>-12%</td><td>-12%</td><td>-14%</td><td>-24%</td><td>-15%</td><td>-19%</td><td>-20%</td><td>-19%</td><td>-29%</td><td>-15%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-21%</td><td>-18%</td><td>-37%</td><td>-24%</td><td>-10%</td><td>-12%</td><td>-8%</td><td>-10%</td><td>-16%</td><td>-18%</td><td>-10%</td><td>-12%</td><td>-18%</td></tr><tr><td>Gourmet Master</td><td>-34%</td><td>-29%</td><td>-26%</td><td>-29%</td><td>-35%</td><td>-38%</td><td>-42%</td><td>-39%</td><td>-39%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-23%</td><td>-20%</td><td>-20%</td><td>-26%</td><td>-25%</td><td>-29%</td><td>-31%</td><td>-29%</td><td>-34%</td><td>-27%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-21%</td><td>-18%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of pre-COVID</td><td>77%</td><td>80%</td><td>80%</td><td>74%</td><td>75%</td><td>71%</td><td>69%</td><td>71%</td><td>66%</td><td>73%</td><td>83%</td><td>83%</td><td>84%</td><td>100%</td><td>87%</td><td>80%</td><td>84%</td><td>79%</td><td>82%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data

Exhibit 2: Quarterly SSSG tracker

<table><tr><td colspan="11">SSSG yoy trend</td><td colspan="10">vs. 2019</td></tr><tr><td>SSSG yoy</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>KFC China</td><td>-2.0%</td><td>-3.0%</td><td>-2.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>2.0%</td><td>3.0%</td><td>1.0%</td><td></td><td>-10%</td><td>-12%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-11%</td><td>-10%</td><td>-14%</td><td>-9%</td><td></td></tr><tr><td>Pizza Hut China</td><td>-5.0%</td><td>-8.0%</td><td>-6.0%</td><td>-2.0%</td><td>0.0%</td><td>2.0%</td><td>1.0%</td><td>1.0%</td><td>-1.0%</td><td></td><td>-8%</td><td>-14%</td><td>-14%</td><td>-16%</td><td>-8%</td><td>-12%</td><td>-13%</td><td>-16%</td><td>-9%</td><td></td></tr><tr><td>YUM China</td><td>-3.0%</td><td>-4.0%</td><td>-3.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>1.0%</td><td>3.0%</td><td>0.0%</td><td></td><td>-10%</td><td>-13%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-12%</td><td>-11%</td><td>-13%</td><td>-10%</td><td></td></tr><tr><td>Starbucks China</td><td>-11.0%</td><td>-14.0%</td><td>-14.0%</td><td>-6.0%</td><td>0.0%</td><td>2.0%</td><td>2.0%</td><td>7.0%</td><td>0.5%</td><td></td><td>-33%</td><td>-32%</td><td>-32%</td><td>-34%</td><td>-33%</td><td>-31%</td><td>-30%</td><td>-29%</td><td>-32%</td><td></td></tr><tr><td>Gourmet Master China</td><td>-15.7%</td><td>-16.7%</td><td>-15.2%</td><t

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
