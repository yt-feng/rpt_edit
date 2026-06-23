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
CHINA CONSUMER CONNECTIONS

# 618 wrap: Boosted GMV with divergent ROI on discounts and subsidies; cosmetics outperformed

China's 618 Shopping Festival concluded on June 18/20/21 for Douyin/JD/Tmall. The event this year started from May 15/11/21 for Douyin/JD/Tmall. We summarize within, data points by platform, category and brand level and share our key takeaways.

1. Overall GSV at 6% yoy per Analysys in main platforms in aggregate, moderating from last year 10% yoy; with narrowing gap between GSV and parcel volume growth (8% yoy during May 13 to Jun 14 vs. +16% yoy during the same period last year) likely due to higher ticket size (see our 618 expert call takeaways) but a wider gap vs. yoy GMV growth according to the expert's note of mid-teens yoy GMV in this year/low-teens yoy last year 618 on larger platform and government's supports/subsidies/discounts.

2. Divergent ROI trend with wider discounts but more platform support/rebates: Our price checks (Exhibit 3) also showed that most categories recorded broader discounts (especially on pet foods) except snacks cutting back discounts while beauty/jewelry was flat yoy. Platform-wise, channel checks suggest a stepping up of national subsidies in Taobao/Tmall, for cosmetics in particular, and a Douyin KOL cut-back on slotting fees/commission fees.

3. Growth concentrated in leading players in selected categories: Top players across categories we track were largely stable, with leading players driving growth in selected categories. In cosmetics, MNC leaders occupied the top rankings, while leading domestic brands e.g. Mao Geping/Giant Biogene/Forest Cabin/Proya/Shanghai Jahwa delivering solid growth, outpacing broad industry growth. For spirits, we observe consolidation trends with online growth mainly concentrated in the super-premium category with the JD 618 report indicating that overall spirits GMV was up by 25% yoy this year driven by strong growth in Moutai/Wuliangye.

4. Category performance: Per our earlier expert call, pet (+c.48% yoy), supplements (+c.20% yoy) & 3C products (+19% yoy) delivered fast growth on Tmall/Taobao over 618 while jewelry lagged (-27% yoy). Beauty (incl. skincare and color cosmetics) was in-line with Taobao/Tmall platform growth at 15% yoy while growing 21% yoy in Douyin. Sportswear saw 16% yoy growth in Taobao/Tmall, also roughly in-line with platform growth.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Michelle Cheng
+852-2978-6631 |
michelle.cheng@gs.com
GS (Asia) L.L.C.

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Nicolas Yi
+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

Molly Dai
+852-3966-4000 | molly.dai@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Cecilia Tang
+86(21)2401-8738 |
cecilia.tang@goldmansachs.cn
GS (China) Securities
Company Limited

Xinyu Ruan
+852-2978-7347 | xinyu.ruan@gs.com
GS (Asia) L.L.C.

Carol Chen
+852-2978-7999 | carol.chen@gs.com
GS (Asia) L.L.C.

## Additional highlights by category:

1) Cosmetics: Per our expert call, cosmetics GMV in Tmall during this 618 was 15% yoy, and combining with the 21% yoy in Douyin, we expect mid-high teens yoy growth across all platforms vs. Analysys's c.10% yoy GSV. We continue to see better performance of high-end MNC brands (with Skinceuticals/Estee Lauder brand/SK-II/Clarins/Shiseido improved ranking in Tmall), strong recovery of Comfy and MGP to be on track of their full year target. Shanghai Jahwa/Winona showed strong GMV on Douyin, with 68%/29% yoy growth for 1 May - 18 Jun 2026 (refer to our 618 pulse check).

2) Sportswear & Apparel: Sportswear brands showed lackluster sales trend during 618, with discounts largely stable/slightly deeper. Within sportswear, we highlight that Descente/Decathlon/Kolon Sport/Adidas/Fila/Lulu rankings improved or support ongoing popularity, domestic mass brands overall rankings were largely stable, and Nike/Camel underperformed with rankings declining yoy.

3) Consumer Durables: Home appliances growth was largely muted during 618, due to a high base last year driven by trade-in stimulus. On pricing, we note lower AC prices vs. Singles' Day this year for select brands though were higher yoy, which may indicate that brands may have turned to promotions to boost demand despite rising input costs. Product wise, products with penetration increase potential such as cleaning appliances likely recorded better growths as market leaders continued to highlight robust growth.

4) Staples: Staples saw larger discounts in liquid milk/IMF while relatively rational promotions on spirits were disciplined (on JD). Super-premium spirits brands saw robust growth on JD (mid-teens% GMV growth for Moutai/Wuliangye), with Moutai Feitian 2026 original case GMV reaching Rmb300mn+ and common Wuliangye (world-cup edition) GMV increasing over 13-fold yoy. Tsingtao/Budweiser ranked top 2 on JD among beer brands.

5) Pet Food: Pet food delivered solid GMV growth at 48% yoy in Taobao/Tmall per our expert call. Yet, we saw mixed performance on our covered names: Gambol/China Pet Food group delivered 15%/45% yoy during 5.15-6.18 on Douyin yet Gambol saw weaker Tmall performance in which Myfoodie saw lower ranking vs. last year's 618 while Fregate remained stable. We also saw wider discounts among local names in which China Pet Foods/Gambol/Rosy Fresh saw 3ppt/13ppt/6ppt wider discounts vs. 2025's 618, reflecting intensifying competition in the industry.

Key brands outperformed during 618: Adidas/Descente/Kolon, Forest Cabin/Mao Geping/Estee Lauder, Moutai, Rosy Fresh, Ninebot.

## More reads:

China Cosmetics: 618 pulse check: performance in Douyin: MNCs/higher-end led; MGP rebound to 50%+ yoy

China Cosmetics: 618 pulse check: Expert call takeaways: sound growth, more subsidies/promotion supports and stable channel spending; leading local/MNCs ahead

China Consumer Connection: Online Brand Tracker: May-26: Divergent 618 performance across most sectors; Cosmetics led, IMF/White Goods lag

China Cosmetics: Monthly tracker: May-26: accelerating versus 1Q; local brands rebound likely

## on subsidies; MNCs continue to be strong June to date

China Pet Food Monthly: May 2026: Softer pricing causes sales to moderate; China Pet Foods GMV growth led

China Consumer Durables: Appliance Tracker: May 2025: Still weak domestic demand yet base will ease into June, 618 in focus; exports sequentially improved

Exhibit 1: 618 online GSV yoy moderated to 6% in 2026 vs. 10% in 2025 per Analysys
618 Shopping festival online GSV YoY growth

![](images/41657e979c3f56e43e43ac97efc8a0269b042cf7e31e904b3558dddb31a23005.jpg)  
Source: Analysys, Data compiled by GS Global Investment Research  
Exhibit 2: Industry online GMV (excl. Taobao) reached Rmb864bn this 618 largely flat yoy per Syntun

618 Shopping festival online GMV growth  
![](images/fe9f29454909159f11941ec281b0e726e041bcf5c4dff34c700b466f9226a63c.jpg)  
GMV includes Tmall, JD, Douyin, PDD, Kuaishou.  
Source: Syntun, Data compiled by GS Global Investment Research

Exhibit 3: Compared to the 618 shopping festival last year, discounts were higher in most segments with snacks cutting back on discounts while beauty/jewelry were flat yoy

<table><tr><td rowspan="2"></td><td colspan="11">Price discount change</td></tr><tr><td>2022 618</td><td>2022 11.11</td><td>2023 618</td><td>2023 11.11</td><td>2024 618</td><td>2024 11.11</td><td>2025 618</td><td>2025 11.11</td><td>2026 618</td><td>vs 2025 11.11</td><td>vs 2025 618</td></tr><tr><td colspan="12">Consumer staples</td></tr><tr><td>Dairy</td><td>27%</td><td>30%</td><td>27%</td><td>33%</td><td>41%</td><td>29%</td><td>28%</td><td>32%</td><td>33%</td><td>2%</td><td>5%</td></tr><tr><td>IMF</td><td>29%</td><td>20%</td><td>8%</td><td>14%</td><td>23%</td><td>20%</td><td>18%</td><td>22%</td><td>26%</td><td>4%</td><td>8%</td></tr><tr><td>Beer</td><td>18%</td><td>29%</td><td>22%</td><td>21%</td><td>26%</td><td>19%</td><td>23%</td><td>28%</td><td>25%</td><td>-3%</td><td>2%</td></tr><tr><td>Compound condiments</td><td>26%</td><td>32%</td><td>24%</td><td>17%</td><td>19%</td><td>18%</td><td>19%</td><td>23%</td><td>23%</td><td>0%</td><td>4%</td></tr><tr><td>Pet foods</td><td>23%</td><td>27%</td><td>25%</td><td>24%</td><td>23%</td><td>19%</td><td>23%</td><td>28%</td><td>32%</td><td>5%</td><td>10%</td></tr><tr><td>Snacks</td><td>46%</td><td>50%</td><td>39%</td><td>40%</td><td>39%</td><td>36%</td><td>39%</td><td>37%</td><td>36%</td><td>-1%</td><td>-3%</td></tr><tr><td colspan="12">Consumer discretionary</td></tr><tr><td>Beauty</td><td>55%</td><td>58%</td><td>56%</td><td>58%</td><td>55%</td><td>55%</td><td>54%</td><td>55%</td><td>54%</td><td>-1%</td><td>0%</td></tr><tr><td>Jewelry</td><td></td><td></td><td></td><td></td><td></td><td>17%</td><td>12%</td><td>12%</td><td>13%</td><td>0%</td><td>0%</td></tr><tr><td>Sportswear</td><td>27%</td><td>40%</td><td>33%</td><td>32%</td><td>33%</td><td>40%</td><td>40%</td><td>45%</td><td>44%</td><td>-1%</td><td>4%</td></tr><tr><td>AC (incl. trade-in)</td><td>2,724</td><td>2,559</td><td>2,599</td><td>2,624</td><td>2,512</td><td>2,079</td><td>1,739</td><td>1,962</td><td>1,912</td><td>-3%</td><td>10%</td></tr></table>

We use the change in price after discounts for ACs to calculate the price discount change. For other categories, we use the average discount rate to calculate the price discount change. For the Beauty sector, we use discounts incl. gifts. Higher % means higher discounts.

Color makeup (source: Syntum)  
Exhibit 4: Tmall/JD sales ranking by category

<table><tr><td colspan="4">Tmall</td></tr><tr><td>25</td><td>26</td><td>Brand</td><td>Company</td></tr><tr><td colspan="4">Beauty (source: Tmall)</td></tr><tr><td>6</td><td>1</td><td>SkinCeuticals</td><td>L&#x27;Oreal</td></tr><tr><td>4</td><td>2</td><td>Estee Lauder</td><td>Estee Lauder</td></tr><tr><td>1</td><td>3</td><td>Proya</td><td>Proya Cosmetics</td></tr><tr><td>2</td><td>4</td><td>Lancome</td><td>L&#x27;Oreal</td></tr><tr><td>7</td><td>5</td><td>SK-II</td><td>P&amp;G</td></tr><tr><td>3</td><td>6</td><td>L&#x27;Oreal Paris</td><td>L&#x27;Oreal</td></tr><tr><td>5</td><td>7</td><td>La Mer</td><td>Estee Lauder</td></tr><tr><td>10</td><td>8</td><td>Clarins</td><td>Clarins</td></tr><tr><td>8</td><td>9</td><td>HR</td><td>L&#x27;Oreal</td></tr><tr><td>9</td><td>10</td><td>CPB</td><td>Shiseido</td></tr></table>

<table><tr><td colspan="4">JD</td></tr><tr><td>25</td><td>26</td><td>Brand</td><td>Company</td></tr><tr><td colspan="4">Skincare (source: Syntun)</td></tr><tr><td>1</td><td>1</td><td>Lancome</td><td>L&#x27;Oreal</td></tr><tr><td>3</td><td>2</td><td>SK-II</td><td>P&amp;G</td></tr><tr><td>5</td><td>3</td><td>Skinceuticals</td><td>L&#x27;Oreal</td></tr><tr><td>2</td><td>4</td><td>Estee Lauder</td><td>Estee Lauder</td></tr><tr><td>&gt;5</td><td>5</td><td>Anessa</td><td>Shiseido</td></tr></table>

<table><tr><td>1</td><td>1</td><td>YSL</td><td>L&#x27;Oreal</td></tr><tr><td>&gt;5</td><td>2</td><td>MGP</td><td>Maogeping</td></tr><tr><td>2</td><td>3</td><td>CPB</td><td>Shiseido</td></tr><tr><td>4</td><td>4</td><td>NARS</td><td>Shiseido</td></tr><tr><td>5</td><td>5</td><td>Estee Lauder</td><td>Estee Lauder</td></tr></table>

Home appliances (source: Syntun)

Color makeup (source: Syntun)

<table><tr><td>2</td><td>1</td><td>YSL</td><td>L&#x27;Oreal</td></tr><tr><td>1</td><td>2</td><td>Dior</td><td>LVMH</td></tr><tr><td>&gt;5</td><td>3</td><td>Mao Geping</td><td>Mao Geping</td></tr><tr><td>&gt;5</td><td>4</td><td>CPB</td><td>Shiseido</td></tr><tr><td>&gt;5</td><td>5</td><td>Armani</td><td>L&#x27;Oreal</td></tr></table>

<table><tr><td>1</td><td>1</td><td>Midea</td><td>Midea</td></tr><tr><td>2</td><td>2</td><td>Haier</td><td>Haier Smart Home</td></tr><tr><td>4</td><td>3</td><td>Gree</td><td>Gree</td></tr><tr><td>3</td><td>4</td><td>Xiaomi</td><td>Xiaomi Group</td></tr><tr><td>5</td><td>5</td><td>Little Swan</td><td>Midea</td></tr></table>

<table><tr><td colspan="4">Home appliances (source: Syntun)</td></tr><tr><td>1</td><td>1</td><td>Midea</td><td>Midea</td></tr><tr><td>2</td><td>2</td><td>Haier</td><td>Haier Smart Home</td></tr><tr><td>3</td><td>3</td><td>Gree</td><td>Gree</td></tr><tr><td>4</td><td>4</td><td>Xiaomi</td><td>Xiaomi Group</td></tr><tr><td>&gt;5</td><td>5</td><td>TCL</td><td>TCL</td></tr></table>

<table><tr><td colspan="4">Snack (source: Syntun)</td></tr><tr><td>1</td><td>1</td><td>Three Squirrels</td><td>Three Squirrels</td></tr><tr><td>4</td><td>2</td><td>Bestore</td><td>Bestore</td></tr><tr><td>3</td><td>3</td><td>Be &amp; Cheery</td><td>PepsiCo</td></tr><tr><td>2</td><td>4</td><td>BIBIZAN</td><td>Shangke Foods</td></tr><tr><td>&gt;5</td><td>5</td><td>Lay&#x27;s</td><td>PepsiCo</td></tr></table>

<table><tr><td>1</td><td>1</td><td>Three Squirrels</td><td>Three Squirrels</td></tr><tr><td>&gt;5</td><td>2</td><td>J.ZAO</td><td>JD</td></tr><tr><td>2</td><td>3</td><td>Bestore</td><td>Bestore</td></tr><tr><td>&gt;5</td><td>4</td><td>Wolong</td><td>Wolong</td></tr><tr><td>3</td><td>5</td><td>Want Want</td><td>Want Want China</td></tr></table>

<table><tr><td>1</td><td>1</td><td>Rosy Fresh</td><td>Zhejiang Jichong</td></tr><tr><td>2</td><td>2</td><td>Legend Sandy</td><td>Jia Pets</td></tr><tr><td>&gt;5</td><td>3</td><td>Royal Canin</td><td>Mars</td></tr><tr><td>5</td><td>4</td><td>Myfoodie</td><td>Gambol</td></tr><tr><td>4</td><td>5</td><td>Honest Bite</td><td>Jianmo Biotech</td></tr></table>

<table><tr><td colspan="4">Pet foods (source: Syntun)</td></tr><tr><td>1</td><td>1</td><td>Royal Canin</td><td>Mars</td></tr><tr><td>4</td><td>2</td><td>Legend Sandy</td><td>Jia Pets</td></tr><tr><td>2</td><td>3</td><td>Myfoodie</td><td>Gambol</td></tr><tr><td>5</td><td>4</td><td>Pure &amp; Natural</td><td>Shanghai Yiyun Pet Products</td></tr><tr><td>&gt;5</td><td>5</td><td>Orijen</td><td>Champion Petfoods</td></tr></table>

<table><tr><td colspan="4">Sportswear (Source: Tmall)</td></tr><tr><td>2</td><td>1</td><td>Fila</td><td>Anta Sports</td></tr><tr><td>3</td><td>2</td><td>Adidas</td><td>Adidas</td></tr><tr><td>1</td><td>3</td><td>Nike</td><td>Nike</td></tr><tr><td>4</td><td>4</td><td>Lululemon</td><td>Lululemon</td></tr><tr><td>5</td><td>5</td><td>Li Ning</td><td>Li Ning</td></tr><tr><td>6</td><td>6</td><td>Anta</td><td>Anta Sports</td></tr><tr><td>10</td><td>7</td><td>Descente</td><td>Anta Sports</td></tr><tr><td>9</td><td>8</td><td>Decathlon</td><td>Decathlon</td></tr><tr><td>8</td><td>9</td><td>Asics</td><td>Asics</td></tr><tr><td>&gt;10</td><td>10</td><td>Kolon</td><td>Anta Sports</td></tr></table>

For Syntun, 2025 Ranking based on May 13 - Jun 18 2025 GMV and 2024 Ranking based on May 24 - Jun 18 2024 GMV; for Tmall, 2025 Ranking based on May 13 - Jun 20 2025 GMV and 2024 Ranking based on May 24 - Jun 20 2024 GMV.

Source: Tmall, Syntun, GS Global Investment Research

Exhibit 5: Douyin sales ranking by category

<table><tr><td colspan="4">Douyin</td></tr><tr><td>25</td><td>26</td><td>Brand</td><td>Company</td></tr><tr><td colspan="4">Skincare</td></tr><tr><td>3</td><td>1</td><td>Proya</td><td>Proya Cosmetics</td></tr><tr><td>2</td><td>2</td><td>HR</td><td>L&#x27;Oreal</td></tr><tr><td>4</td><td>3</td><td>Estee Lauder</td><td>Estee Lauder</td></tr><tr><td>5</td><td>4</td><td>La Mer</td><td>Estee Lauder</td></tr><tr><td>1</td><td>5</td><td>KANs</td><td>Shanghai Chicmax</td></tr><tr><td>7</td><td>6</td><td>Lancome</td><td>L&#x27;Oreal</td></tr><tr><td>6</td><td>7</td><td>L&#x27;Oreal Paris</td><td>L&#x27;Oreal</td></tr><tr><td>&gt;10</td><td>8</td><td>Pechoin</td><td>Shanghai Pehchaolin Daily Chemical</td></tr><tr><td>10</td><td>9</td><td>Chando</td><td>Shanghai Chando</td></tr><tr><td>&gt;10</td><td>10</td><td>Guyu</td><td>Guyu Biotechnology Group</td></tr></table>

Major appliances

<table><tr><td cols

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
