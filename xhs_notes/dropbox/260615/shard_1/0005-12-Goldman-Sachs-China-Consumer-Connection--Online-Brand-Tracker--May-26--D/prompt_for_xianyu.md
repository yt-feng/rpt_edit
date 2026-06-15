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
# China Consumer Connection: Online Brand Tracker: May-26: Divergent 618 performance across most sectors; Cosmetics led, IMF/White Goods

We summarize the May updates of our Online Brand Tracker within. Key highlights:

1. Category performance: In May-26, we observe weak performance for consumer categories - With Tmall/Taobao/JD combined, Women's clothing was flat yoy while all other categories recorded a yoy decline. Sports shoes/Beauty/Supplements/Dairy/Sportswear/Small kitchen appliances/IMF/Beer/Pet Foods/White goods registered

-2%/-4%/-6%/-9%/-11%/-18%/-19%/-22%/-22%/-31% yoy declines. Note: Tracker data suggest a meaningful re-base in Beauty and Supplements for Tmall/Taobao numbers in 2025 Jan - May.

Considering Douyin/Tmall/Taobao/JD combined, we saw Beauty GMV growing at 14% yoy in May, accelerating vs. 11% in April, partially helped by a softer Women's Day in 1Q, along with increasing subsidies from platforms and local governments. At the same time, aggregate GMV for core brands (Exhibit 10) for

Sportswear/Condiments grew at 14%/47% yoy in May, accelerating vs. April at 9%/34%. Other categories recorded deceleration/decline, with Dairy/Women's Clothing/Pet Foods/Beer/IMF/White Goods at 3%/-1%/-8%/-8%/-24%/-33% yoy for core brands in May (Pet Food using industry yoy) vs. 11%/1%/18%/1%/-23%/-35% in April.

## 2. Domestic vs. MNC brands:

In Cosmetics, data show a rebound in local brands while MNCs continuing to outperform. We think the acceleration was partially helped by a softer Women's Day in 1Q, along with increasing subsidies from platforms and local governments. Local brands that rebounded were Forest Cabin/Botanee/Shanghai Jahwa/MGP/Proya/Shanghai Chicmax/Giant Biogene, recording 110%/43%/27%/22%/8%/7%/6% yoy GMV growth, while Bloomage/Yatsen saw GMV decline by 19%/36% yoy. For MNCs, Estee Lauder (EL)/L'Oreal/Shiseido delivered 36%/16%/11% yoy GMV growth, while LG H&H/Amore Corp/Kose were under pressure at -34%/-31%/-22% yoy. Estee Lauder group outperformed in the higher segment, while L'Oreal group was driven by dermocosmetics, albeit mass-market brands faced local brands' competition.

Besides accelerating in May and solid growth for key covered brands/western brands in phase I (see our 618 phase I pulse check: Beauty GMV is tracking well with likely improving ROI), for Jun 1-8 on Douyin, we note an ongoing robust profile for

Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Michelle Cheng

+852-2978-6631 | michelle.cheng@gs.com GS (Asia) L.L.C.

Sho Kawano

+81(3)4587-9905 |
sho.kawano@gs.com
GS Japan Co., Ltd.

Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Nicolas Yi

+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

western MNCs with L'Oreal and EL Group at 50%+ yoy while local brands are mixed: Mao Geping is catching up at 60%+ yoy Jun-to-date, uplifting its 618-to date yoy to 40%+ yoy. Giant is accelerating on an easier base at 13% yoy Jun-to-date. To reflect the full picture, for the first 25 days of 618 (May 15 - June 8) on Douyin, Forest Cabin led with triple-digit% LFL growth, partly due to an easier base, followed by Proya/Botanee/MGP/Giant at 64%/51%/43%/20% LFL growth.

In Sportswear, looking at May data across Tmall, JD, and Douyin, we see an overall divergent brand performance in May, with Labor Day demand soft but 618 shopping festival promotion brought support for certain brands. We flag that due to cadence of the 618, promotion may diverge across brands; we suggest combining May - Jun sales to assess overall performance. In May, several outdoor names such as Arc'teryx and Descente, as well as niche premium brand Lulu saw deceleration in May partially on a high base, while adidas, Li Ning, Anta, Fila, Bosideng, Salomon accelerated from Apr possibly on 618 shopping festival promotion. We also flag that brands have been executing omni-channel strategies in both online (e.g.; emerging channels like Dewu) and offline, suggesting the sales data collected by data vendors may not reconcile with actual growth.

Outperforming brands (May): Estee Lauder, Winona, Forest Cabin, Fancl, Nongfu, Haidilao

Underperforming brands (May): Nutrilon, Timage, QuadHA, Mead Johnson, Wyeth, Midea

## Relevant reads:

China Cosmetics: Monthly tracker: May-26: accelerating versus 1Q; local brands rebound likely on subsidies; MNCs continue to be strong June to date

Asia Pacific Textile, Apparel & Footwear: Monthly Tracker: OEM May trends mixed; Pou Sheng slightly moderated

China Consumer Durables: Appliance Tracker: Apr 2026: Weakening domestic demand and exports resuming growth with mixed performance across products, 618 in focus

China IP Retailer and Toy Tracker: May update: Pop Mart China online growth decelerated with higher base; Miniso/Bloks accelerating IP/product launch

China Restaurants: Monthly Tracker: May update: Trends turn softer but divergence across brands; FMD high base effect kicking in

China Pet Food Monthly: May 2026: softer pricing causes sales to moderate; China Pet Foods GMV growth led

China Consumer Staples Cost Index Tracker: May 2026: PET cost easing but still high; Aluminum sequentially trended down

We would like to thank Molly Dai, Christina Liu, Cecilia Tang, Lily Qi, Keira Liu, Xinyu Ruan, and Carol Chen for their contributions to this report.

## Category performance

## Category trends (JD/Tmall/Taobao)

Baby and Supplements: Online sales growth of the IMF category declined by 19% yoy in May on Tmall/Taobao/JD combined, worsening vs. 1Q26 at an 11% yoy decline. Online sales of the Supplements category declined by 10% yoy in May vs. -8% yoy in 1Q26.

Cosmetics: With Tmall/Taobao/JD combined, Beauty online GMV declined 4% yoy in May, weakening from 1% yoy decline in 1Q26.

Consumer Durables: Sales growth remained under pressure yoy in May with relative outperformance of small kitchen appliances and RVC. Compared to Apr, most appliances categories showed a widened yoy decline, while RVC and wet dry vacuums recorded narrower decline.

Exhibit 1: In May-26, we observe weak performance for consumer categories - With Tmall/Taobao/JD combined, Women's clothing was flat yoy while all other categories recorded yoy declines. Sports shoes/Beauty/Supplements/Dairy/Sportswear/Small kitchen appliances/IMF/Beer/Pet Foods/White goods registered $-2\% / -4\% / -6\% / -9\% / -11\% / -18\% / -19\% / -22\% / -22\% / -31\%$ yoy decline. Note: Tracker data suggest a meaningful re-base for Beauty for Tmall/Taobao numbers in 2025 Jan - May.  
Snapshot of category sales growth (% yoy)

<table><tr><td rowspan="2">Category</td><td colspan="3">May-26</td><td colspan="3">Apr-26</td><td colspan="3">1Q26</td><td colspan="3">4Q25</td><td>3Q25</td><td>2Q25</td><td>1Q25</td></tr><tr><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td></td></tr><tr><td>Beer</td><td>-4%</td><td>-35%</td><td>-22%</td><td>-9%</td><td>-16%</td><td>-13%</td><td>-1%</td><td>-17%</td><td>-9%</td><td>-23%</td><td>5%</td><td>-10%</td><td>-7%</td><td>-4%</td><td>-1%</td></tr><tr><td>Dairy</td><td>-21%</td><td>11%</td><td>-9%</td><td>-2%</td><td>18%</td><td>6%</td><td>-38%</td><td>-24%</td><td>-33%</td><td>-38%</td><td>16%</td><td>-17%</td><td>n.a.</td><td>n.a.</td><td>-1%</td></tr><tr><td>IMF</td><td>-2%</td><td>-26%</td><td>-19%</td><td>14%</td><td>-24%</td><td>-14%</td><td>2%</td><td>-19%</td><td>-11%</td><td>-3%</td><td>7%</td><td>4%</td><td>4%</td><td>19%</td><td>5%</td></tr><tr><td>Skincare</td><td>5%</td><td>-17%</td><td>-4%</td><td>-3%</td><td>-7%</td><td>-4%</td><td>0%</td><td>-8%</td><td>-1%</td><td>-14%</td><td>12%</td><td>-7%</td><td>-4%</td><td>-15%</td><td>1%</td></tr><tr><td>Cosmetics</td><td>-9%</td><td></td><td></td><td>-3%</td><td></td><td></td><td>1%</td><td></td><td></td><td>-8%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sportswear</td><td>-15%</td><td>21%</td><td>-11%</td><td>2%</td><td>32%</td><td>6%</td><td>29%</td><td>-5%</td><td>26%</td><td>-7%</td><td>7%</td><td>-5%</td><td>6%</td><td>-3%</td><td>6%</td></tr><tr><td>Sports shoes</td><td>-3%</td><td>3%</td><td>-2%</td><td>-6%</td><td>-3%</td><td>-5%</td><td>7%</td><td>-15%</td><td>4%</td><td>-9%</td><td>11%</td><td>-4%</td><td>10%</td><td>2%</td><td>12%</td></tr><tr><td>Women&#x27;s clothing</td><td>-1%</td><td>19%</td><td>0%</td><td>16%</td><td>17%</td><td>16%</td><td>7%</td><td>-58%</td><td>8%</td><td>-4%</td><td>108%</td><td>-3%</td><td>-13%</td><td>-16%</td><td>-6%</td></tr><tr><td>White goods</td><td>-50%</td><td>-8%</td><td>-31%</td><td>-25%</td><td>-19%</td><td>-22%</td><td>-8%</td><td>-51%</td><td>-15%</td><td>-18%</td><td>5%</td><td>-3%</td><td>4%</td><td>6%</td><td>5%</td></tr><tr><td>Small kitchen appliances</td><td>-15%</td><td>-23%</td><td>-18%</td><td>-2%</td><td>-8%</td><td>-4%</td><td>-2%</td><td>-27%</td><td>-1%</td><td>-19%</td><td>68%</td><td>-12%</td><td>8%</td><td>-9%</td><td>1%</td></tr><tr><td>Condiments</td><td>-12%</td><td>n.a.</td><td>n.a.</td><td>-19%</td><td>n.a.</td><td>n.a.</td><td>-16%</td><td>n.a.</td><td>n.a.</td><td>-20%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3%</td></tr><tr><td>Pet foods</td><td>-7%</td><td>-45%</td><td>-22%</td><td>14%</td><td>-3%</td><td>10%</td><td>0%</td><td>-60%</td><td>-5%</td><td>-11%</td><td>82%</td><td>-6%</td><td>-4%</td><td>3%</td><td>-3%</td></tr><tr><td>Supplements</td><td>-7%</td><td>-3%</td><td>-6%</td><td>6%</td><td>21%</td><td>11%</td><td>-9%</td><td>-8%</td><td>-8%</td><td>-21%</td><td>14%</td><td>-11%</td><td>5%</td><td>-11%</td><td>-7%</td></tr></table>

Sportswear, sports shoes, women's clothing are from Tmall only. For Condiments, we use Tmall+Taobao only as JD data is not meaningful on a yoy basis after the platform's category reclassification.  
Source: Moojing

## Category performance (Tmall/Taobao)

Exhibit 2: YoY monthly/quarterly trends at Tmall/Taobao in May

<table><tr><td>Category</td><td>Value</td><td>Volume</td><td>ASP</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td colspan="7">MF, Pat Foods, Supplements, Beauty and Jewelry</td></tr><tr><td colspan="7">MAY</td></tr><tr><td>Jul-25</td><td>11%</td><td>-2%</td><td>13%</td><td>Jul-25</td><td>-9%</td><td>-10%</td></tr><tr><td>Aug-25</td><td>-3%</td><td>-8%</td><td>6%</td><td>Aug-25</td><td>0%</td><td>-5%</td></tr><tr><td>Sep-25</td><td>1%</td><td>-4%</td><td>6%</td><td>Sep-25</td><td>-13%</td><td>-1%</td></tr><tr><td>Oct-25</td><td>-13%</td><td>-21%</td><td>10%</td><td>Oct-25</td><td>-21%</td><td>-12%</td></tr><tr><td>Nov-25</td><td>-1%</td><td>1%</td><td>-2%</td><td>Nov-25</td><td>-14%</td><td>-8%</td></tr><tr><td>Oct-Nov-25</td><td>-6%</td><td>-10%</td><td>4%</td><td>Oct-Nov-25</td><td>-11%</td><td>-10%</td></tr><tr><td>Dec-25</td><td>7%</td><td>3%</td><td>4%</td><td>Dec-25</td><td>-16%</td><td>-8%</td></tr><tr><td>Jan-26</td><td>12%</td><td>19%</td><td>-6%</td><td>Jan-26</td><td>4%</td><td>23%</td></tr><tr><td>Feb-26</td><td>-7%</td><td>-15%</td><td>9%</td><td>Feb-26</td><td>-10%</td><td>-4%</td></tr><tr><td>Jan-Feb-26</td><td>3%</td><td>3%</td><td>1%</td><td>Jan-Feb-26</td><td>-3%</td><td>10%</td></tr><tr><td>Mar-26</td><td>-1%</td><td>4%</td><td>-5%</td><td>Mar-26</td><td>5%</td><td>4%</td></tr><tr><td>Apr-26</td><td>14%</td><td>-14%</td><td>33%</td><td>Apr-26</td><td>14%</td><td>0%</td></tr><tr><td>May-26</td><td>-2%</td><td>-4%</td><td>2%</td><td>May-26</td><td>-7%</td><td>-1%</td></tr><tr><td>1Q25</td><td>11%</td><td>-13%</td><td>28%</td><td>1Q25</td><td>-19%</td><td>-19%</td></tr><tr><td>Mar-25</td><td>-7%</td><td>-14%</td><td>7%</td><td>Mar-25</td><td>-7%</td><td>-14%</td></tr><tr><td>3Q25</td><td>2%</td><td>-5%</td><td>8%</td><td>3Q25</td><td>-7%</td><td>-5%</td></tr><tr><td>4Q25</td><td>-3%</td><td>-6%</td><td>4%</td><td>4Q25</td><td>-11%</td><td>-6%</td></tr><tr><td>1Q26</td><td>2%</td><td>3%</td><td>-1%</td><td>1Q26</td><td>0%</td><td>8%</td></tr><tr><td colspan="7">Supplements</td></tr><tr><td>Jul-25</td><td>4%</td><td>-13%</td><td>18%</td><td>Jul-25</td><td>-10%</td><td>-23%</td></tr><tr><td>Aug-25</td><td>0%</td><td>34%</td><td>-25%</td><td>Aug-25</td><td>-2%</td><td>-16%</td></tr><tr><td>Sep-25</td><td>-3%</td><td>27%</td><td>-24%</td><td>Sep-25</td><td>-11%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>2%</td><td>-12%</td><td>16%</td><td>Oct-25</td><td>-16%</td><td>-25%</td></tr><tr><td>Nov-25</td><td>-35%</td><td>-29%</td><td>-9%</td><td>Nov-25</td><td>-14%</td><td>-14%</td></tr><tr><td>Oct-Nov-25</td><td>-21%</td><td>-21%</td><td>2%</td><td>Oct-Nov-25</td><td>-15%</td><td>-20%</td></tr><tr><td>Dec-25</td><td>-19%</td><td>-21%</td><td>2%</td><td>Dec-25</td><td>-7%</td><td>-15%</td></tr><tr><td>Jan-Feb-26</td><td>-17%</td><td>-18%</td><td>2%</td><td>Jan-Feb-26</td><td>-1%</td><td>-3%</td></tr><tr><td>Mar-26</td><td>8%</td><td>2%</td><td>6%</td><td>Mar-26</td><td>1%</td><td>-3%</td></tr><tr><td>Apr-26</td><td>6%</td><td>-14%</td><td>24%</td><td>Apr-26</td><td>-3%</td><td>-16%</td></tr><tr><td>May-26</td><td>-7%</td><td>-6%</td><td>-2%</td><td>May-26</td><td>5%</td><td>7%</td></tr><tr><td>1Q25</td><td>-20%</td><td>-20%</td><td>0%</td><td>1Q25</td><td>-5%</td><td>-15%</td></tr><tr><td>2Q25</td><td>-22%</td><td>-20%</td><td>-2%</td><td>2Q25</td><td>-23%</td><td>-28%</td></tr><tr><td>3Q25</td><td>0%</td><td>17%</td><td>-12%</td><td>3Q25</td><td>-8%</td><td>-18%</td></tr><tr><td>4Q25</td><td>-21%</td><td>-21%</td><td>2%</td><td>4Q25</td><td>-14%</td><td>-19%</td></tr><tr><td>1Q26</td><td>-9%</td><td>-11%</td><td>3%</td><td>1Q26</td><td>0%</td><td>-3%</td></tr><tr><td colspan="7">Color makeup</td></tr><tr><td>Jul-25</td><td>-6%</td><td>-29%</td><td>31%</td><td></td><td></td><td></td></tr><tr><td>Aug-25</td><td>3%</td><td>-24%</td><td>35%</td><td></td><td></td><td></td></tr><tr><td>Sep-25</td><td>-8%</td><td>-20%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Oct-25</td><td>-7%</td><td>-19%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Nov-25</td><td>-13%</td><td>-19%</td><td>7%</td><td></td><td></td><td></td></tr><tr><td>Oct-Nov-25</td><td>-10%</td><td>-19%</td><td>11%</td><td></td><td></td><td></td></tr><tr><td>Dec-25</td><td>-2%</td><td>-6%</td><td>5%</td><td></td><td></td><td></td></tr><tr><td>Jan-Feb-26</td><td>4%</td><td>4%</td><td>0%</td><td></td><td></td><td></td></tr><tr><td>Mar-26</td><td>-4%</td><td>-12%</td><td>10%</td><td></td><td></td><td></td></tr><tr><td>Apr-26</td><td>-3%</td><td>-16%</td><td>16%</td><td></td><td></td><td></td></tr><tr><td>May-26</td><td>-9%</td><td>-8%</td><td>-1%</td><td></td><td></td><td></td></tr><tr><td>1Q25</td><td>-8%</td><td>-25%</td><td>22%</td><td></td><td></td><td></td></tr><tr><td>2Q25</td><td>-18%</td><td>-35%</td><td>26%</td><td></td><td></td><td></td></tr><tr><td>3Q25</td><td>-4%</td><td>-24%</td><td>26%</td><td></td><td></td><td></td></tr><tr><td>4Q25</td><td>-8%</td><td>-16%</td><td>9%</td><td></td><td></td><td></td></tr><tr><td>1Q26</td><td>1%</td><td>-2%</td><td>3%</td><td></td><td></td><td></td></tr><tr><td colspan="7">Packaged FAS and Alcohol</td></tr><tr><td colspan="7">Dairy</td></tr><tr><td>Jul-25</td><td>-34%</td><td>-27%</td><td>4%</td><td>Jul-25</td><td>-17%</td><td>-22%</td></tr><tr><td>Aug-25</td><td>-15%</td><td>-22%</td><td>9%</td><td>Aug-25</td><td>-17%</td><td>-24%</td></tr><tr><td>Sep-25</td><td>-15%</td><td>-15%</td><td>0%</td><td>Sep-25</td><td>-13%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>-25%</td><td>-26%</td><td>2%</td><td>Oct-25</td><td>-7%</td><td>-25%</td></tr><tr><td>Nov-25</td><td>-51%</td><td>-43%</td><td>-14%</td><td>No

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
