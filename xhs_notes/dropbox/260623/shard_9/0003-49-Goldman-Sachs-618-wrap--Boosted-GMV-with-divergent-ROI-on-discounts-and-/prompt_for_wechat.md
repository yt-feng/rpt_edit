你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td colspan="4">Douyin</td></tr><tr><td>25</td><td>26</td><td>Brand</td><td>Company</td></tr><tr><td colspan="4">Color makeup</td></tr><tr><td>1</td><td>1</td><td>Dirovo</td><td>Shanghai Youke Jiabei</td></tr><tr><td>2</td><td>2</td><td>MAOGEPING</td><td>Mao Geping</td></tr><tr><td>4</td><td>3</td><td>YSL</td><td>L&#x27;Oreal</td></tr><tr><td>6</td><td>4</td><td>Pramy</td><td>Shanghai PRAMY</td></tr><tr><td>&gt;10</td><td>5</td><td>BABI</td><td>Hangzhou Lanchi Technology</td></tr><tr><td>7</td><td>6</td><td>Carslan</td><td>Carslan</td></tr><tr><td>8</td><td>7</td><td>MAC</td><td>Estee Lauder</td></tr><tr><td>&gt;10</td><td>8</td><td>Socorskin</td><td>Nanjing Maorun Zhicheng</td></tr><tr><td>&gt;10</td><td>9</td><td>Flower Lure</td><td>Guangzhou Aoqi Biotechnology</td></tr><tr><td>&gt;10</td><td>10</td><td>DPDP</td><td>Aromasong Cosmetics</td></tr></table>

Small kitchen appliances

<table><tr><td>1</td><td>1</td><td>Haier</td><td>Haier Smart Home</td></tr><tr><td>2</td><td>2</td><td>Midea</td><td>Midea</td></tr><tr><td>4</td><td>3</td><td>Little Swan</td><td>Midea</td></tr><tr><td>9</td><td>4</td><td>Leader</td><td>Haier Smart Home</td></tr><tr><td>6</td><td>5</td><td>Xiaomi</td><td>Xiaomi Group</td></tr><tr><td>7</td><td>6</td><td>MIJIA</td><td>Xiaomi Group</td></tr><tr><td>5</td><td>7</td><td>Hisense</td><td>Hisense Home Appliances</td></tr><tr><td>3</td><td>8</td><td>Gree</td><td>Gree</td></tr><tr><td>8</td><td>9</td><td>Wahin</td><td>Midea</td></tr><tr><td>&gt;10</td><td>10</td><td>TCL</td><td>TCL</td></tr></table>

<table><tr><td>1</td><td>1</td><td>Midea</td><td>Midea</td></tr><tr><td>4</td><td>2</td><td>Supor</td><td>Supor</td></tr><tr><td>5</td><td>3</td><td>Yangzi</td><td>Yangzi</td></tr><tr><td>3</td><td>4</td><td>Joyoung</td><td>Joyoung</td></tr><tr><td>2</td><td>5</td><td>Royalstar</td><td>Royalstar</td></tr><tr><td>9</td><td>6</td><td>Malata</td><td>Malata</td></tr><tr><td>&gt;10</td><td>7</td><td>CASDON</td><td>CASDON</td></tr><tr><td>&gt;10</td><td>8</td><td>bewinch</td><td>Lexy</td></tr><tr><td>&gt;10</td><td>9</td><td>Jialiquan</td><td>Jialiquan</td></tr><tr><td>6</td><td>10</td><td>Bear</td><td>Bear Electric Appliance</td></tr></table>

Lifestyle appliances

<table><tr><td>3</td><td>1</td><td>Dreame</td><td>Dreame</td></tr><tr><td>2</td><td>2</td><td>Roborock</td><td>Roborock Tech</td></tr><tr><td>1</td><td>3</td><td>Ecovacs</td><td>Ecovacs Robotics</td></tr><tr><td>7</td><td>4</td><td>Uwant</td><td>Uwant</td></tr><tr><td>4</td><td>5</td><td>Tineco</td><td>Ecovacs Robotics</td></tr><tr><td>6</td><td>6</td><td>Skyworth</td><td>Skyworth</td></tr><tr><td>9</td><td>7</td><td>Midea</td><td>Midea</td></tr><tr><td>&gt;10</td><td>8</td><td>Haier</td><td>Haier Smart Home</td></tr><tr><td>&gt;10</td

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
