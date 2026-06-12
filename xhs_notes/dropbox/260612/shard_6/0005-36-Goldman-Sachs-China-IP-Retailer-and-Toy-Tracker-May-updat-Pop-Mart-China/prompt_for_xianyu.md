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
CHINA IP RETAILER AND TOY TRACKER

# May update: Pop Mart China online growth decelerated with higher base; Miniso/Bloks accelerating IP/product launch

In this note, we provide updates on China IP retailers and toy companies, including new products/IP, sales momentum, and overseas market updates. Pop Mart's domestics online sales grew +29% yoy in May, slower than Apr at +95% yoy growth with higher base. On Douyin, run-rate into Jun is lagging both sequentially and YoY, facing a tough comparison against June 2025 supply surge of Labubu's Big Into Energy series. In the US market, May's YoY decline (-36% yoy) slightly narrowed vs Apr (-43% yoy) thanks to an easier prior-year base; however, the comparison base will become more challenging heading into June. 2Q-to-date credit card sales tracking remained negative (c.40% yoy decline QTD according to BBG data, compared to LSD% growth in 1Q). In the US and China, secondary market price/google trends did not indicate significant IP momentum improvement in May. Whether the upcoming World Cup (Jun 11-Jul 19) could restore momentum for the Labubu IP is among the market focus for the upcoming month. Miniso continued its rapid IP rollout in May and early-Jun, and more high quality IPs will be launched into summer peak season. Mgmt noted Apr-May performance saw positive SSSG and Labor day sales recorded +high-teens% yoy growth, on track with company's guidance. In the US market, growth in May sequentially improved from Apr thanks to favorable base, while base into Jun will be tougher. 2Q26-to-date sales growth decelerated from 1Q due to a higher base, i.e.\~26% yoy QTD vs. close to 50% in 1Q according to BBG credit sales data. Bloks accelerated 2QTD new product launches, increasing the number of series/SKUs launched both YoY and QoQ. Overall, Tmall+JD+Douyin sales yoy growth accelerated in May vs. Apr based on our tracker, driven by new releases focusing on existing major IPs. More details within.

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

## Pop Mart:

New IPs/products: 1) Dear Birds multi-IP series debut in May, which was not sold out in the first few days after debut. It recorded >32k/>10k sales volume in Douyin/Tmall and still available as of Jun 8, which is relatively muted compared to previous multi-IP series Have a good run which was sold out quickly after debut and recorded >200k sales volume in Douyin for the first month. 2) New plush toy series released by Crybaby and Hacipupu in May did not sell out in the first few days after debut, while Zsiga was sold out in Douyin. More specifically, Zsiga's new plush toy series (launched on Jun 4) recorded >10k/>14k sales volume on Tmall and Douyin as of Jun 8; Hacipupu's new series (launched on May 28) registered >4k/>3k sales volume in Douyin/Tmall and still available as of Jun 8; Crybaby's new plush toy series (launched on May 21) recorded >70k/>40k sales volume in Douyin/Tmall and still available as of Jun 8. In the secondary market, for the new series, only few non-secret SKUs are trading at SD%-low teens% premium, while others are trading at discounts as of Jun 8.

Secondary market prices: Secondary market discounts saw further expansion for IPs including Labubu, Molly, Dimoo in May and stabilization/slight recovery for IPs including Skullpanda, CryBaby for the sample SKUs we track. 1) Labubu: Discounts for the sample SKUs we track is generally at $30\% -45\%$ currently, slightly expanded from Apr. The FIFA plush pendant saw a deeper discount at c. $15\%$ in May. 2) Twinkle: Twinkle: For the sample SKUs we track, secondary market discount narrowed to LSD% in May but dropped to HSD% in early-Jun.

Marketing: 1) Labubu participated in Lisa's World Cup MV, which had 13.6mn views on Youtube so far. However, based on Google index, we didn't see meaningful improvement on its popularity. 2) Collaborations launched include McDonalds (Twinkle Twinkle); Coca Cola (Labubu); Ninebot (Sweet Bean) in May.

Online sales: Based on a third-party database, combined sales on Tmall and Douyin flagship stores grew +29% yoy in May, slower than Apr at +95% yoy growth. Based on our Douyin flagship store tracker, plush toy sales in May also lagged Apr and run-rate in Jun is currently lagging behind May as of Jun 6.

## Miniso:

■ Recent performance: The company continued its rapid IP rollout in May and early-Jun, featuring in-house IP Yoyo, movie-related IPs (such as Star War, Toy Story) and popular IPs including Chiikawa x Sanrio, Loopy, etc. Mgmt noted Apr-May performance saw positive SSSG and Labor day sales recorded +high-teens% yoy, outperforming overall retail sales with daily sales reaching historical highs.

■ Marketing: 1) Gallery was launched in Shanghai in mid-May. Its first exhibition was featured by Indonesian artist RYOL; 2) YOYO appeared on the Met Gala red carpet as a bag accessory worn by model Paloma Elsesser and was featured as part of the official event souvenirs in early-May.

■ Online sales: Based on a third-party database, combined sales on Tmall, JD and Douyin in May grew 21%, faster than 10% growth in Apr but decelerated from 1Q26 (+43% yoy) partly due to the higher base.

## Bloks:

■ New IP/products: New product launches in May focused on existing major IPs (such as Ultraman, Transformers, Kamen Rider). Number of series/SKUs launched in 2Q-to-date has increased YoY and QoQ.  
■ Product momentum: For adult lines, based on Tmall flagship store sales, most adult IPs saw sequential sales volume increase in May except for Pokemon. Overall, Tmall+JD+Douyin sales yoy growth accelerated vs. Apr based on our tracker.

Exhibit 1: Pop Mart's online sales growth in May and 2Q26-to-date growth were both slower sequentially based on the data we track  
![](images/3c70ae3e0e2d223dc7b347e0e10657904f7a911565c743f057b72d3b7ab7d3f3.jpg)

<details>
<summary>bar chart</summary>

Pop Mart China online sales growth
| Quarter | Tmall+Douyin sales yoy (%) | Reported EC platform sales yoy (%) | Reported online sales yoy (%) |
| :--- | :--- | :--- | :--- |
| 1Q24 | 47 | 23 | |
| 2Q24 | 108 | 91 | |
| 1H24 | 81 | 54 | |
| 3Q24 | 136 | 138 | |
| 4Q24 | 215 | 168 | |
| 1Q25 | 220 | 143 | |
| 2Q25 | 183 | 196 | 282 |
| 1H25 | 199 | 154 | |
| 3Q25 | 154 | 303 | |
| 4Q25 | 83 | 107 | |
| 2H25 | 114 | 163 | |
| 1Q26 | 115 | 153 | |
| 2Q26-to-date | 56 | | |
</details>

EC platform sales are Tmall and Douyin combined sales.  
Source: Company data, Moojing, Chanmama

Exhibit 3: Labubu's resale prices of Sanrio/FIFA series slightly corrected in May for the SKUs we track  
![](images/eb9c01b361a0be9bd0de246ab87e2404f20738af14fd6d8dbc9454288dab6934.jpg)

<details>
<summary>line chart</summary>

Labubu plush toy price premium in secondary market
| Date | Macaron 芝麻豆豆 (%) | Coca Cola 快乐因子 (%) | Energy 欢乐 (%) | Pin For Love "F" (%) | Sanrio_Kuromi (%) | FIFA (%) |
|---|---|---|---|---|---|---|
| Jan-24 | -30 | -10 | -15 | -15 | -15 | -15 |
| Mar-24 | -10 | -5 | -10 | -10 | -10 | -10 |
| May-24 | 120 | 5 | 5 | 5 | 5 | 5 |
| Jul-24 | 30 | 10 | 10 | 10 | 10 | 10 |
| Sep-24 | 40 | 15 | 15 | 15 | 15 | 15 |
| Nov-24 | 70 | 20 | 20 | 20 | 20 | 20 |
| Jan-25 | -10 | -5 | -5 | -5 | -5 | -5 |
| Mar-25 | -5 | 0 | 0 | 0 | 0 | 0 |
| May-25 | 0 | 5 | 50 | 50 | 50 | 50 |
| Jul-25 | 150 | 60 | 200 | 60 | 60 | 60 |
| Sep-25 | 100 | 40 | 40 | 40 | 40 | 40 |
| Nov-25 | 30 | 10 | 10 | 10 | 10 | 10 |
| Jan-26 | -10 | -5 | -5 | -5 | -5 | -5 |
| Mar-26 | -20 | -10 | -10 | -10 | -10 | -10 |
| May-26 | -30 | -20 | -20 | -20 | -20 | -20 |
The chart displays the percentage premium for each game from January to May, with values ranging from approximately -30% to +30%. The legend identifies six games: Macaron 芝麻豆豆, Coca Cola 快乐因子, Energy 欢乐, Pin For Love "F", Sanrio_Kuromi, and FIFA. The data is presented in a single column format with the date on the left and the premium value on the right. The chart is created using a line graph with a color-coded legend. The title explicitly states that the chart is part of a multi-panel figure.
</details>

As of Jun 3, 2026.  
Source: Qiandao

Exhibit 2: Pop Mart's plush toy supply on Douyin slightly moderated in May  
![](images/57cab1e46700229aa51856b5f21d21e41a13abd4f244ec231b3ada4db3c4f55b.jpg)

<details>
<summary>stacked bar chart</summary>

| Jan-25 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Feb-25 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mar-25 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Apr-25 | 150 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| May-25 | 250 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 |
| Jun-25 | 450 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 |
| Jul-25 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 | 450 |
| Aug-25 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 | -150 |
| Sep-25 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 | -125 |
| Oct-25 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 |
| Nov-25 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 | -75 |
</details>

As of Jun 6, 2026.  
Source: Chanmama

Exhibit 4: Most IPs secondary prices were relatively stable in May  
![](images/1dae27ff1b519ce2f6e068e2d6515f0a7d115a419bbe1f34862bdcfad31a5011.jpg)

<details>
<summary>line chart</summary>

| Date       | Hirono | Molly | Skullpanda | Crybaby | Dimoo | Labubu | Twinkle Twinkle |
|------------|--------|-------|------------|---------|-------|--------|-----------------|
| 30-Dec-23  | 10%    | -50%  | -30%       | -10%    | -10%  | -10%   | -10%            |
| 29-Feb-24  | 15%    | -30%  | -25%       | -5%     | -5%   | -5%    | -5%             |
| 30-Apr-24  | 20%    | -20%  | -20%       | 0%      | 0%    | 100%   | 0%              |
| 30-Jun-24  | 25%    | -10%  | -15%       | 5%      | 5%    | 50%    | 5%              |
| 31-Aug-24  | 30%    | 0%    | -10%       | 10%     | 10%   | 30%    | 10%             |
| 31-Oct-24  | 25%    | 5%    | -5%        | 15%     | 15%   | 20%    | 15%             |
| 31-Dec-24  | 20%    | 10%   | 0%         | 20%     | 20%   | 15%    | 20%             |
| 28-Feb-25  | 15%    | 15%   | 5%         | 25%     | 25%   | 10%    | 25%             |
| 30-Apr-25  | 10%    | 20%   | 10%        | 30%     | 30%   | 5%     | 30%             |
| 30-Jun-25  | 5%     | 25%   | 15%        | 35%     | 35%   | 0%     | 35%             |
| 31-Aug-25  | 0%     | 30%   | 20%        | 40%     | 40%   | -5%    | 40%             |
| 31-Oct-25  | -5%    | 35%   | 25%        | 45%     | 45%   | -10%   | 45%             |
| 31-Dec-25  | -10%   | 40%   | 30%        | 50%     | 50%   | -15%   | 50%             |
| 28-Feb-26  | -15%   | 45%   | 35%        | 55%     | 55%   | -20%   | 55%             |
| 30-Apr-26  | -20%   | 50%   | 40%        | 60%     | 60%   | -25%   | 60%             |
</details>

As of Jun 3, 2026.  
Source: Qiandao

Exhibit 5: Most adult IPs saw sequential sales volume increase in May, except for Pokemon  
![](images/f4d9eea5e562963c5b5541e947fdfd6e367fc3e2aecd9786f396ea17781d48f3.jpg)

<details>
<summary>stacked bar chart</summary>

Sales volume in Bloks Tmall flagship store
| Month | EVA (Legend) (Thousands) | Pokemon (Thousands) | Hatsune Miku (Thousands) | Detective Conan (Thousands) | Naruto (Champion) (Thousands) | Kamen Rider (Legend) (Thousands) |
|---|---|---|---|---|---|---|
| Nov-24 | 10.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Dec-24 | 2.0 | 0.0 | 2.0 | 0.0 | 0.0 | 12.5 |
| Jan-25 | 5.0 | 1.5 | 1.5 | 0.0 | 0.0 | 1.0 |
| Feb-25 | 7.5 | 1.5 | 1.5 | 0.0 | 0.0 | 0.0 |
| Mar-25 | 4.0 | 1.5 | 1.5 | 0.0 | 0.0 | 1.5 |
| Apr-25 | 5.0 | 1.5 | 1.5 | 0.0 | 0.0 | 1.5 |
| May-25 | 4.5 | 3.0 | 1.5 | 1.5 | 0.0 | 0.0 |
| Jun-25 | 3.0 | 3.5 | 1.5 | 0.5 | 0.0 | 1.5 |
| Jul-25 | 2.0 | 1.5 | 1.5 | 0.5 | 0.0 | 1.5 |
| Aug-25 | 2.0 | 1.5 | 1.5 | 1.5 | 0.5 | 1.5 |
| Sep-25 | 3.5 | 1.5 | 1.5 | 1.5 | 0.5 | 1.5 |
| Oct-25 | 2.0 | 1.5 | 1.5 | 1.5 | 0.5 | 1.5 |
| Nov-25 | 6.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.5 |
| Dec-25 | 3.5 | 1.5 | 1.5 | 1.5 | 1.0 | 16.0 |
| Jan-26 | 2.0 | 1.5 | 1.5 | 1.5 | 3.0 | 13.5 |
| Feb-26 | 2.0 | 1.5 | 1.5 | 1.5 | 2.0 | 9.0 |
| Mar-26 | 1.5 | 1.5 | 1.5 | 1.5 | 2.0 | 9.0 |
| Apr-26 | 1.5 | 1.5 | 1.5 | 1.5 | 2.0 | 6.5 |
| May-26 | 1.5 | 1.5 | 1.5 | 1.5 | 2.0 | 7.0 |
The chart displays a stacked bar chart with each bar representing a total sales volume for that month from Nov-24 to May-26, broken down by the sales volume of each individual brand or category on the Y-axis (in thousands). The legend identifies six brands: EVA (Legend), Pokemon, Hatsune Miku, Detective Conan, Naruto (Champion), and Kamen Rider (Legend). The data is presented in a single column format with values labeled above each bar.
</details>

Source: Moojing

Exhibit 6: Sales value in Bloks Tmall flagship store  
![](images/189e6af916c8681608703dca4da01f31ba6c4678921b127c99da7d860a7a0271.jpg)

<details>
<summary>stacked bar chart</summary>

Sales value in Bloks Tmall flagship store
| Month | EVA (Legend) (Millions) | Pokemon (Millions) | Hatsune Miku (Millions) | Detective Conan (Millions) | Naruto (Champion) (Millions) | Kamen Rider (Legend) (Millions) |
|---|---|---|---|---|---|---|
| Nov-24 | 1.75 | 0.0 | 0.35 | 0.0 | 0.0 | 0.0 |
| Dec-24 | 0.35 | 0.0 | 0.25 | 0.0 | 0.0 | 0.0 |
| Jan-25 | 0.95 | 0.25 | 0.15 | 0.0 | 0.0 | 0.0 |
| Feb-25 | 1.25 | 0.35 | 0.15 | 0.0 | 0.0 | 0.0 |
| Mar-25 | 0.7 | 0.25 | 0.25 | 0.0 | 0.0 | 0.0 |
| Apr-25 | 1.0 | 0.15 | 0.25 | 0.0 | 0.0 | 0.0 |
| May-25 | 0.85 | 0.25 | 0.15 | 0.15 | 0.0 | 0.0 |
| Jun-25 | 0.6 | 0.15 | 0.15 | 0.15 | 0.0 | 0.0 |
| Jul-25 | 0.35 | 0.1 | 0.15 | 0.15 | 0.15 | 0.0 |
| Aug-25 | 0.35 | 0.15 | 0.25 | 0.15 | 0.15 | 0.0 |
| Sep-25 | 0.85 | 0.15 | 0.25 | 0.15 | 0.15 | 0.0 |
| Oct-25 | 0.35 | 0.15 | 0.15 | 0.15 | 0.15 | 0.0 |
| Nov-25 | 1.25 | 0.25 | 0.35 | 0.15 | 0.15 | 0.1 |
| Dec-25 | 0.75 | 0.15 | 0.25 | 0.15 | 0.15 | 1.2 |
| Jan-26 | 0.35 | 0.15 | 0.25 | 0.15 | 0.25 | 1.4 |
| Feb-26 | 0.35 | 0.15 | 0.25 | 0.15 | 0.25 | 1.2 |
| Mar-26 | 0.25 | 0.15 | 0.35 | 0.15 | 0.15 | 1.2 |
| Apr-26 | 0.15 | 0.15 | 0.35 | 0.15 | 0.15 | 0.6 |
| May-26 | 0.15 | 0.15 | 0.35 | 0.15 | 0.15 | 0.7 |
The chart displays a stacked bar chart with each bar representing the total sales value for that month from Nov-24 to May-26, broken down by the sales value of each product category on the Y-axis (in millions). The legend indicates the product categories: EVA (Legend), Pokemon, Hatsune Miku, Detective Conan, Naruto (Champion), and Kamen Rider (Legend). The data is presented in a single column format.
</details>

Source: Moojing

## Overseas market

In the US, non-farm payrolls in May was well above expectations with unchanged unemployment rate, and core retail sales increased $0.5\%$ in Apr, slightly above expectations. That said, UMich consumer sentiment fell by 5.0pt to 44.8—its lowest level on record—while the Conference Board's c

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
