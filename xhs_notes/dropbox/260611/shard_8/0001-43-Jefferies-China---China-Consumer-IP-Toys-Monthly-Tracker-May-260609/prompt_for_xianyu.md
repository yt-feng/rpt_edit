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
## IP Toys Monthly Tracker - May

Pop Mart's share price has been resilient since its 1Q26 earnings release on 13 May. While Mr. Duan Yongping's purchase of 81m shares (c.6% stake) in late May boosted market confidence, we do not see any material change in fundamentals. Key catalysts ahead include: (1) the launch of Labubu 4.0, and (2) World Cup-related promotions, which could further drive overseas momentum.

## China

- Second-hand prices: Labubu plush second-hand prices stabilized MoM. Of the top 30 most wanted products on the second-hand exchange platforms, we see more diversity: three of them are non-Pop Mart products, while the Pop Mart x aespa collaboration remains most wanted.  
- Ecommerce sales: Meritco has not released May data yet; Apr data shows Pop Mart's GMV on ecommerce platforms was up 70% YoY and up 25% MoM. Meanwhile, Bloks' ecommerce sales were up 16% you, and Miniso's was up 11% YoY in Apr.

## Overseas

- Social media interactions: Amid the ongoing normalization trend, Pop Mart's engagement on TikTok picked up in May for its global and Thailand accounts, which were up 49% and 67% MoM, respectively.  
- Social media followers: In May, Pop Mart added 13k new Instagram followers across its Global, Thailand, US, and UK accounts combined (vs. +19k in Apr; Figures 19-20).  
- Website traffic & app active users: Pop Mart app's active users declined in May, both globally and in the US. Global and regional Google Search Trends for Pop Mart continued to trend downward (Figures 21-24).

## New Product Launches/events

- Pop Mart: Pop Mart's 1Q26 results were broadly in line with market expectations, while the post-earnings call highlighted possible margin pressure in 2026 (refer to our report). Despite this, the share price was resilient, supported by Duan Yongping's purchase of 81m shares, representing c.6% of total shares outstanding, between 25–28 May, making him a substantial shareholder of the company (Figure 3).  
- On the product front, Pop Mart stepped up global marketing initiatives through World Cup-related promotions, including an appearance in the music video of the official FIFA World Cup 2026 song "Goals", and a collaboration with Coca-Cola to launch Labubu-branded cans in China.  
- Bloks: Bloks launched 13 new series in May (vs. 12 in Apr and 21 in 1Q26). The new releases feature a more diversified IP portfolio, with a particular focus on Star Wars, while the company continued to emphasize assembly vehicle products. Looking ahead, Bloks is expected to launch collaborative products tied to Toy Story 5 ahead of the movie's release in late June.

[Continued inside.]

Figure 1 - Pop Mart Labubu 1.0 second-hand price in mainland China  
![](images/0ae382db8104da7f2bbbfb15885de31c8d8a275a05d53ad045dbeb5e99dbb4bc.jpg)

<details>
<summary>line chart</summary>

| Date | Toffee | Soymilk | Lychee Berry | Sea Salt | Green Grape | Sesame |
| --- | --- | --- | --- | --- | --- | --- |
| 11/8/2004 | 200 | 100 | 100 | 100 | 100 | 100 |
| 12/7/2004 | 150 | 100 | 100 | 100 | 100 | 100 |
| 2/6/2005 | 125 | 100 | 100 | 100 | 100 | 100 |
| 3/5/2005 | 125 | 100 | 100 | 100 | 100 | 100 |
| 4/4/2005 | 125 | 100 | 100 | 100 | 100 | 100 |
| 5/3/2005 | 125 | 100 | 100 | 100 | 100 | 100 |
| 6/2/2005 | 125 | 100 | 100 | 100 | 100 | 100 |
| 7/9/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 8/6/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 9/4/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 10/3/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 11/2/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 12/9/2005 | 250 | 250 | 250 | 250 | 250 | 250 |
| 1/7/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| 2/6/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| 3/4/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| 4/3/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| 5/2/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| 6/1/2006 | 250 | 250 | 250 | 250 | 250 | 250 |
| Jun-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Jul-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Aug-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Sep-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Oct-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Nov-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Dec-16-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Jan-17-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Feb-17-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Mar-18-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Apr-18-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| May-18-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Jun-18-26 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 |
| Jul-18-26 | nan | nan | nan | nan | nan | nan |
| Aug-18-26 | nan | nan | nan | nan | nan | nan |
| Sep-18-26 | nan | nan | nan | nan | nan | nan |
| Oct-18-26 | nan | nan | nan | nan | nan | nan |
| Nov-18-26 | nan | nan | nan | nan | nan | nan |
| Dec-18-26 | nan | nan | nan | nan | nan | nan |
| Jan-19-26 | nan | nan | nan | nan | nan | nan |
| Feb-19-26 | nan | nan | nan | nan | nan | nan |
| Mar-19-26 | nan | nan | nan | nan | nan | nan |
| Apr-19-26 | nan | nan | nan | nan | nan | nan |
| May-19-26 | nan | nan | nan | nan | nan | nan |
| Jun-19-26 | nan | nan | nan | nan | nan | nan |
| Jul-19-26 | nan | nan | nan | nan | nan | nan |
| Aug-19-26 | nan | nan | nan | nan | nan | nan |
| Sep-19-26 | nan | nan | nan | nan | nan | nan |
| Oct-19-26 | nan | nan | nan | nan | nan | nan |
| Nov-19-26 | nan | nan | nan | nan | nan | nan |
| Dec-19-26 | nan | nan | nan | nan | nan | nan |
</details>

Source: Chaowanzu, JEF. Note: official retail price is RMB99

Figure 2 - Pop Mart Instagram Interaction Index  
![](images/0f7fae7ced2885a4a634fb06413ba463396f222adb41d24b537528b45c2ea7e0.jpg)

<details>
<summary>bar chart</summary>

| Month   | Global | Thailand | US   |
|---------|--------|----------|------|
| Jan-24  | 100    | 100      | 100  |
| Feb-24  | 150    | 150      | 150  |
| Mar-24  | 200    | 200      | 200  |
| Apr-24  | 250    | 250      | 250  |
| May-24  | 300    | 300      | 300  |
| Jun-24  | 350    | 350      | 350  |
| Jul-24  | 400    | 400      | 400  |
| Aug-24  | 450    | 450      | 450  |
| Sep-24  | 500    | 500      | 500  |
| Oct-24  | 550    | 550      | 550  |
| Nov-24  | 600    | 600      | 600  |
| Dec-24  | 650    | 650      | 650  |
| Jan-25  | 700    | 700      | 700  |
| Feb-25  | 750    | 750      | 750  |
| Mar-25  | 800    | 800      | 800  |
| Apr-25  | 850    | 850      | 850  |
| May-25  | 900    | 900      | 900  |
| Jun-25  | 950    | 950      | 950  |
| Jul-25  | 1000   | 1000     | 1000 |
| Aug-25  | 1050   | 1050     | 1050 |
| Sep-25  | 1100   | 1100     | 1100 |
| Oct-25  | 1150   | 1150     | 1150 |
| Nov-25  | 1200   | 1200     | 1200 |
| Dec-25  | 1250   | 1250     | 1250 |
| Jan-26  | 1300   | 1300     | 1300 |
| Feb-26  | 1350   | 1350     | 1350 |
| Mar-26  | 1400   | 1400     | 1400 |
| Apr-26  | 1450   | 1450     | 1450 |
| May-26  | 1500   | 1500     | 1500 |
</details>

Source: Listen First, JEF, Note: Jan-2024 = 100, interactions include likes, comments, and forwards.

Figure 3 - Pop Mart shareholdings breakdown: Duan Yong Ping is now a substantial shareholder

<table><tr><td>Total no.of shares</td><td>1,341,043,150</td><td>100.0%</td></tr><tr><td>GWF</td><td>561,131,960</td><td>41.84%</td></tr><tr><td>Pop Mart Hehuo</td><td>62,053,027</td><td>4.63%</td></tr><tr><td>Tianjin Paqu</td><td>31,196,420</td><td>2.33%</td></tr><tr><td>Owned by Mr. Wang</td><td>654,381,407</td><td>48.80%</td></tr><tr><td>Sidsi</td><td>10,616,060</td><td>0.79%</td></tr><tr><td>Justin Moon</td><td>1,319,618</td><td>0.10%</td></tr><tr><td>Owned by mgmt</td><td>11,935,678</td><td>0.89%</td></tr><tr><td>Andrew Yue Wu</td><td>8,609</td><td>0.00%</td></tr><tr><td>Owned by Non-executive director</td><td>8,609</td><td>0.00%</td></tr><tr><td>Duan Yongping</td><td>81,031,600</td><td>6.04%</td></tr></table>

Source: HKEX, JEF, Note: as of 8 June 2026

Jingjue Pei \* | Equity Analyst

852 3767 1224 | jingjue.pei@JEF.com

Anne Ling \* | Equity Analyst

852 3743 8783 | aling@JEF.com

## Ecommerce sales trackers

May data will be available after 15 June.

Figure 4 - Pop Mart eCommerce sales  
![](images/caaac41be5e4720982ab2ee322ddff7c733e643bf42662522c199360e9188846.jpg)

<details>
<summary>bar-line hybrid</summary>

Pop Mart
| Month | Taobao sales (RMBm) | Douyin sales (RMBm) | JD sales (RMBm) | Major E-Commerce YoY (%) |
|---|---|---|---|---|
| Feb-24 | 30.00 | 50.00 | 10.00 | 150 |
| Mar-24 | 35.00 | 55.00 | 12.00 | 140 |
| Apr-24 | 40.00 | 60.00 | 15.00 | 180 |
| May-24 | 50.00 | 70.00 | 20.00 | 220 |
| Jun-24 | 60.00 | 140.00 | 25.00 | 350 |
| Jul-24 | 70.00 | 130.00 | 30.00 | 380 |
| Aug-24 | 80.00 | 140.00 | 35.00 | 360 |
| Sep-24 | 90.00 | 130.00 | 40.00 | 280 |
| Oct-24 | 150.00 | 210.00 | 55.00 | 320 |
| Nov-24 | 160.00 | 155.00 | 65.00 | 250 |
| Dec-24 | 175.00 | 175.00 | 75.00 | 280 |
| Jan-25 | 185.00 | 135.00 | 85.00 | 310 |
| Feb-25 | 95.00 | 215.00 | 195.00 | 335 |
| Mar-25 | 85.00 | 225.00 | 195.00 | 315 |
| Apr-25 | 95.00 | 255.00 | 195.00 | 335 |
| May-25 | 95.00 | 195.00 | 195.00 | 285 |
| Jun-25 | 285.00 | 445.00 | 395.00 | 365 |
| Jul-25 | 65.00 | 235.00 | 195.00 | 185 |
| Aug-25 | 135.00 | 375.00 | 375.00 | 195 |
| Sep-25 | 95.00 | 315.00 | 315.00 | 175 |
| Oct-25 | 165.00 | 415.00 | 415.00 | 195 |
| Nov-25 | 115.00 | 375.00 | 375.00 | 165 |
| Dec-25 | 85.00 | -65.00 | -65.00 | -47 |
| Jan-26 | 225.00 | 375.00 | 512.56 | 277 |
| Feb-26 | 115.00 | 337.56 | 337.56 | -67 |
| Mar-26 | 145.00 | 425.00 | 375.66 | -67 |
| Apr-26 | 148.76 | 437.56 | 425.66 | -67 |
The chart displays a bar chart for Taobao sales and Douyin sales, alongside a line graph for JD sales, with the line representing the year-over-year growth rate of major e-commerce YoY (%). The data is already in English.
</details>

Source: Meritco, JEF

Figure 6 - Kayou eCommerce sales  
![](images/44bab2979a381d52ce4ccd001a397a19951179f6dbda626b2530e87ae1deb00f.jpg)

<details>
<summary>bar-line hybrid</summary>

Kayou
| Month | Taobao sales (RMBm) | Douyin sales (RMBm) | JD sales (RMBm) | Major E-Commerce YoY (RHS) (%) |
|---|---|---|---|---|
| Jan-24 | 15 | 35 | 0 | 0 |
| Feb-24 | 18 | 45 | 0 | 0 |
| Mar-24 | 22 | 55 | 0 | 0 |
| Apr-24 | 45 | 60 | 0 | 0 |
| May-24 | 55 | 70 | 0 | 0 |
| Jun-24 | 58 | 75 | 0 | 0 |
| Jul-24 | 50 | 65 | 0 | 0 |
| Aug-24 | 40 | 60 | 0 | 0 |
| Sep-24 | 35 | 70 | 0 | 0 |
| Oct-24 | 30 | 160 | 0 | 0 |
| Nov-24 | 25 | 80 | 0 | 0 |
| Dec-24 | 20 | 50 | 0 | 0 |
| Jan-25 | 18 | 45 | 0 | -10 |
| Feb-25 | 18 | 55 | 0 | -10 |
| Mar-25 | 50 | 135 | 0 | -10 |
| Apr-25 | 35 | 120 | 0 | -10 |
| May-25 | 15 | 85 | 0 | -10 |
| Jun-25 | 12 | 60 | 0 | -10 |
| Jul-25 | 12 | 90 | 0 | -10 |
| Aug-25 | 12 | 70 | 0 | -10 |
| Sep-25 | 8 | 35 | 0 | -10 |
| Oct-25 | 8 | 40 | 0 | -10 |
| Nov-25 | 8 | 25 | 0 | -10 |
| Dec-25 | 8 | 15 | 0 | -10 |
| Jan-26 | 8 | 18 | 0 | -10 |
| Feb-26 | 8 | 18 | 0 | -10 |
| Mar-26 | 8 | 18 | 0 | -10 |
| Apr-26 | 8 | 18 | 0 | -10 |
</details>

Source: Meritco, JEF

Figure 8 - Top Toy eCommerce sales  
![](images/54e746b4eee3d2bfe5c575a079e36e0fcf1f5e54d874c4970fc3d0a17c52fba6.jpg)

<details>
<summary>bar chart</summary>

| Month    | T Mall | JD   | Douyin | Total yoy (RHS) |
|----------|--------|------|--------|-----------------|
| Aug-23   | 3      | 1    | 0      | 80%             |
| Oct-23   | 2      | 1    | 0      | 60%             |
| Dec-23   | 3      | 1    | 0      | 40%             |
| Feb-24   | 3      | 1    | 0      | 100%            |
| Apr-24   | 3      | 1    | 0      | 60%             |
| Jun-24   | 3      | 1    | 0      | 80%             |
| Aug-24   | 3      | 1    | 0      | 60%             |
| Oct-24   | 3      | 1    | 0      | 80%             |
| Dec-24   | 5      | 1    | 0      | 90%             |
| Feb-25   | 3      | 1    | 0      | 60%             |
| Apr-25   | 5      | 1    | 0      | 100%            |
| Jun-25   | 8      | 3    | 1      | 150%            |
| Aug-25   | 7      | 3    | 2      | 120%            |
| Oct-25   | 7      | 3    | 3      | 180%            |
| Dec-25   | 5      | 3    | 4      | 100%            |
| Feb-26   | 3      | 1    | 0      | 60%             |
| Apr-26   | 2      | 1    | 1      | -20%            |
</details>

Source: Meritco, JEF

Figure 5 - Bloks eCommerce sales  
![](images/588189003b9f0a54d28383d32dc858b6b29b9360a56445d5f02a132672d5579d.jpg)

<details>
<summary>bar-line hybrid</summary>

Bloks
| Month | Taobao sales (RMBm) | Douyin sales (RMBm) | JD sales (RMBm) | Major E-Commerce YoY (RHS) |
|---|---|---|---|---|
| Jan-24 | 7 | 3 | 10 | 5% |
| Feb-24 | 7 | 5 | 8 | 100% |
| Mar-24 | 4 | 1 | 3 | -20% |
| Apr-24 | 7 | 3 | 9 | 50% |
| May-24 | 15 | 3 | 12 | 130% |
| Jun-24 | 10 | 1 | 10 | 50% |
| Jul-24 | 5 | 1 | 6 | 30% |
| Aug-24 | 5 | 1 | 6 | 20% |
| Sep-24 | 5 | 1 | 6 | 20% |
| Oct-24 | 8 | 3 | 6 | 50% |
| Nov-24 | 9 | 3 | 6 | 50% |
| Dec-24 | 11 | 3 | 10 | 30% |
| Jan-25 | 11 | 1 | 10 | 30% |
| Feb-25 | 7 | 1 | 5 | -20% |
| Mar-25 | 8 | 3 | 10 | 70% |
| Apr-25 | 7 | 1 | 6 | -10% |
| May-25 | 13 | 3 | 8 | -10% |
| Jun-25 | 9 | 1 | 10 | -20% |
| Jul-25 | 7 | 1 | 8 | 50% |
| Aug-25 | 7 | 1 | 8 | 50% |
| Sep-25 | 7 | 1 | 8 | 50% |
| Oct-25 | 9 | 3 | 8 | 60% |
| Nov-25 | 7 | 1 | 10 | 60% |
| Dec-25 | 11 | 8 | 10 | 110% |
| Jan-26 | 7 | 3 | 10 | -20% |
| Feb-26 | 8 | 3 | 10 | -20% |
| Mar-26 | 4 | 1 | 8 | -10% |
| Apr-26 | 4 | 1 | 6 | -10% |
The chart displays a stacked bar chart with the left axis showing total sales in RMBm and the right axis showing the percentage of major e-commerce year-over-year growth. The bars are segmented by sales channel: Taobao (dark blue), Douyin (light blue), JD (gray), and Major E-Commerce YoY (light yellow). The data is already in English.
</details>

Source: Meritco, JEF

Figure 7 - 52 Toys eCommerce sales  
![](images/252350ceb20a0da7ced8915df3b8e0d35d70ed1ce452aeda71047506e70341f4.jpg)

<details>
<summary>bar-line hybrid</summary>

52 Toys
| Month | Taobao sales (RMBm) | Douyin sales (RMBm) | JD sales (RMBm) | Major E-Commerce YoY (%) |
|---|---|---|---|---|
| Jan-24 | 3.3 | 1.8 | 2.0 | 30 |
| Feb-24 | 2.0 | 2.0 | 2.0 | 40 |
| Mar-24 | 2.7 | 1.6 | 1.0 | -30 |
| Apr-24 | 2.7 | 1.6 | 1.0 | 10 |
| May-24 | 4.3 | 1.9 | 1.0 | 130 |
| Jun-24 | 3.7 | 1.9 | 1.0 | -10 |
| Jul-24 | 3.3 | 1.9 | 1.0 | -30 |
| Aug-24 | 4.0 | 1.9 | 1.0 | 20 |
| Sep-24 | 3.7 | 1.9 | 1.0 | -10 |
| Oct-24 | 3.7 | 1.9 | 1.0 | -10 |
| Nov-24 | 3.9 | 1.9 | 1.0 | -10 |
| Dec-24 | 2.3 | 1.9 | 1.0 | -70 |
| Jan-25 | 2.0 | 1.9 | 1.0 | -30 |
| Feb-25 | 2.3 | 1.9 | 1.0 | -30 |
| Mar-25 | 3.8 | 1.9 | 1.0 | 70 |
| Apr-25 | 3.7 | 1.9 | 1.0 | -10 |
| May-25 | 3.8 | 1.9 | 1.0 | -10 |
| Jun-25 | 5.0 | 1.9 | 1.0 | -10 |
| Jul-25 | 3.3 | 1.9 | 1.0 | -30 |
| Aug-25 | 2.7 | 1.9 | 1.0 | -30 |
| Sep-25 | 2.7 | 1.9 | 1.0 | -30 |
| Oct-25 | 4.3 | 1.9 | 1.0 | -30 |
| Nov-25 | 4.3 | 1.9 | 1.0 | -30 |
| Dec-25 | 2.7 | 1.9 | 1.0 | -30 |
| Jan-26 | 1.7 | 1.9 | 1.0 | -30 |
| Feb-26 | 3.7 | 1.9 | 1.0 | -30 |
| Mar-26 | 1.3 | 1.9 | 1.0 | -50 |
| Apr-26 | 1.3 | 1.9 | 1.0 | -50 |
The chart displays a bar chart with two data series: 'Taobao sales' and 'Douyin sales'. The bars are grouped by month from Jan to Dec, with each bar labeled by its value in RMBm and percentage change from prior month's baseline (e.g., +5% YoY). The secondary axis on the right shows 'Major E-Commerce YoY' values as percentages.
</details>

Source: Meritco, JEF

Figure 9 - Miniso eCommerce sales  
![](images/9535b1e97a69a07b817029313369ceee6583999080f8af10d2754cb7fd17f16d.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | T Mall (RMBm) | JD (RMBm) | Douyin (RMBm) | Total yoy (RHS) (%) |
| --- | --- | --- | --- | --- |
| Aug-22 | 25 | 10 | 0 | 100 |
| Sep-22 | 30 | 15 | 0 | 300 |
| Oct-22 | 35 | 20 | 0 | 700 |
| Nov-22 | 40 | 25 | 0 | 900 |
| Dec-22 | 30 | 15 | 0 

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
