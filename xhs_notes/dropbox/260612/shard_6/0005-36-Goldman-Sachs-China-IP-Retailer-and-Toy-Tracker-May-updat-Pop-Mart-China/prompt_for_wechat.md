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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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

In the US, non-farm payrolls in May was well above expectations with unchanged unemployment rate, and core retail sales increased $0.5\%$ in Apr, slightly above expectations. That said, UMich consumer sentiment fell by 5.0pt to 44.8—its lowest level on record—while the Conference Board's consumer confidence index decreased by 0.7pt to 93.1 in May, also point to retrenchments in consumer confidence in recent weeks. Our economists noted G10 consumers generally continue to benefit from healthy balance sheets, but labor markets are more mixed, sentiment has worsened from already low levels following the start of the war in the Middle East, and spending headwinds are expected as higher energy prices erode real incomes in the next few months. Elsewhere, consumer sentiment in Singapore/Indonesia also deteriorated, while sentiment in Malaysia/Euro area slightly recovered (Exhibit 16).

For players in diversified retailer sector, we noticed FIVE 1Q26 comp was at +22.7% (above GS/consensus) driven by strong store execution, customer engagement, and strong product trends. However, the company is cautiously guiding the 2H of the year, keeping guidance in those quarters unchanged due to the challenging macro. That said, mgmt did not see any data suggesting a shift in behavior or trade-down. On margin, the company expected OPM to expand for the FY, driven by gross margin, and higher fuel costs are being offset by better tariff costs. We view it as a mixed read to Miniso and Pop Mart in US. Resilient consumption behaviors was observed and tariff tailwinds could be expected. Yet, the company’s cautious guidance on the 2H26 with concerns on macro may imply Miniso/Pop mart will hold similar stance.

Pop Mart: 1) US: The YoY US credit card sales decline narrowed in May arriving at -36% yoy (vs c.43% decline in Apr). Secondary market prices for Labubu remained overall stable in May at \~50% average discount, with an initial dip followed by a recovery. Google search trends was also largely stable, while APP MAU recovered sequentially. 2)

Other regions: Google Trends in Europe and ASEAN was largely stable. APP MAU declined in Europe, while picked up in ASEAN. 3) New IPs/products updates: In the US, we noticed that multi-IP Dear Birds series and Hacipupu's Enchanted Realm Tales series were not offered on the US official website as of Jun 8, while Zsiga and Peach Riot's new plush series were still available. In France, Hacipupu and Peach Riot's new series were sold out, while Zsiga and Dear Birds new series remained available in the official website. In Thailand, new series (Zsiga/ Hacipupu/ Dear Birds/ Peach Riot new series) were all available on the official websites as of Jun 8.

Miniso: US credit card sales growth of $+31\%$ yoy in May accelerated sequentially from $+19\%$ in Apr, leading to $26\%$ growth in 2Q26-to-date.

Exhibit 7: Pop Mart US credit card sales decelerated sequentially in 2Q26-to-date  
![](images/8990fdd75ebe92cba2b06b722a639506ec85668a8df2bfc4e443e54e9d63d5a0.jpg)

<details>
<summary>bar chart</summary>

Pop Mart US credit card sales (quarterly)
| Quarter |

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
