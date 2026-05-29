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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Luxury Goods

Luca Solca +41 582 723 126 luca.solca@bernsteinsg.com

Yi-Peng Khoo, CFA +44 20 7676 6822 yi-peng.khoo@bernsteinsg.com

Eric Chen, CFA +852 2123 2628 eric.chen@bernsteinsg.com

Maria Meita +44 20 7170 0540 maria.meita@bernsteinsg.com

# Hermès: The Secondhand Pricing Tracker - May 2026

We update our secondhand Hermès Birkin and Kelly price tracker to incorporate prices from recent auctions. The underlying dataset is available on request.

This update includes data from two auctions: (1) a Sotheby's online handbag and accessories auction, held in Zurich with 137 lots, that closed on 21 May 2026, and (2) a Christie's handbag and accessories auction, held in Hong Kong with 168 lots, that closed on 25 May 2026. The auctions saw 38 bags fall into our basket: 7 Birkin 25s in Togo Leather, 4 Birkin 30 Togos, 5 Kelly 25 Epsoms, 3 Kelly 28 Epsoms, 10 Kelly Pochette Swifts and 9 Mini Kelly II Epsoms. This brings the total number of handbags tracked in 2Q26 to 78 vs. 90 at the end of 2Q25.

We now see resale price premiums for our core Birkin/Kelly tracker rise from 1.2x in 1Q26 to 1.5x in 2Q26. Our expanded tracker, which includes data on what are likely to be some of the most popular models - the Kelly Pochette and Mini Kelly II - sees resale price premiums rise to \~1.8x over the same period.

Resale price trends may have started to stabilize. 2Q26's estimated multiple now comes in a touch below 2Q25's levels in both our core and expanded trackers, and sequentially above that of 1Q26's. Multiples in Hong Kong remain the weakest; those in Europe and the USA have started to reflate slightly. Auction volumes seem healthy, with 2Q26 QTD auction volumes in our expanded tracker +26% above the level observed in the first two months of 2Q25, and above those observed in the entirety of 2Q24, 1Q25, and 4Q25. Most auctions take place in 2Q and 4Q of each year while 1Q26's auction volumes were particularly weak. There are three more auctions scheduled for the rest of 2Q26.

We believe this supports our benign diagnosis of Hermès' recent performance (see Hermès: Valuations already discount a 'Ferrari reset'). In the near-term, Hermès seems to have been temporarily eclipsed by creative renewals at Chanel and Dior, compounding difficult comps and a tough macroeconomic setting in China, creating a soft patch in momentum. However, stabilizing resale multiple trends, if confirmed, would suggest that the core Hermès “growth formula” remains intact (see The Hermès Magic Formula). New energy is likely set to arrive in 2027, with a new menswear creative director and haute couture. In the meantime, we believe more innovative marketing or product activities could also help bridge this soft patch in momentum (see Global Luxury Goods: The Battle for Attention).

For more notes in this series, see: Hermès: The Secondhand Pricing Tracker, and updates in Sep'25, Oct'25, Nov'25, Dec'25 (with a focus on the Mini Kelly II), Feb'26, Mar'26 (with a comparison to another luxury icon, the Rolex Daytona), early-Apr'26, and more recently in end-Apr'26.

We update our secondhand Hermès Birkin and Kelly price tracker to incorporate prices from recent auctions. The underlying dataset is available on request.

This update includes data from two auctions: (1) a Sotheby's online handbag and accessories auction, held in Zurich with 137 lots, that closed on 21 May 2026, and (2) a Christie's handbag and accessories auction, held in Hong Kong with 168 lots, that closed on 25 May 2026. The auctions saw 38 bags fall into our basket: 7 Birkin 25s in Togo Leather, 4 Birkin 30 Togos, 5 Kelly 25 Epsoms, 3 Kelly 28 Epsoms, 10 Kelly Pochette Swifts and 9 Mini Kelly II Epsoms. This brings the total number of handbags tracked in 2Q26 to 78 vs. 90 at the end of 2Q25.

We now see resale price premiums for our core Birkin/Kelly tracker rise from 1.2x in 1Q26 to 1.5x in 2Q26. Our expanded tracker, which includes data on what are likely to be some of the most popular models - the Kelly Pochette and Mini Kelly II - sees resale price premiums rise to \~1.8x over the same period.

Resale price trends may have started to stabilize. 2Q26's estimated multiple now comes in a touch below 2Q25's levels in both our core and expanded trackers, and sequentially above that of 1Q26's. Multiples in Hong Kong remain the weakest; those in Europe and the USA have started to reflate slightly. Auction volumes seem healthy, with 2Q26 QTD auction volumes in our expanded tracker +26% above the level observed in the first two months of 2Q25, and above those observed in the entirety of 2Q24, 1Q25, and 4Q25. Most auctions take place in 2Q and 4Q of each year while 1Q26's auction volumes were particularly weak. There are three more auctions scheduled for the rest of 2Q26.

We believe this supports our benign diagnosis of Hermès' recent performance (see Hermès: Valuations already discount a 'Ferrari reset'). In the near-term, Hermès seems to have been temporarily eclipsed by creative renewals at Chanel and Dior, compounding difficult comps and a tough macroeconomic setting in China, creating a soft patch in momentum. However, stabilizing resale multiple trends, if confirmed, would suggest that the core Hermès “growth formula” remains intact (see The Hermès Magic Formula). New energy is likely set to arrive in 2027, with a new menswear creative director and haute couture. In the meantime, we believe more innovative marketing or product activities could also help bridge this soft patch in momentum (see Global Luxury Goods: The Battle for Attention).

For more notes in this series, see: Hermès: The Secondhand Pricing Tracker, and updates in Sep'25, Oct'25, Nov'25, Dec'25 (with a focus on the Mini Kelly II), Feb'26, Mar'26 (with a comparison to another luxury icon, the Rolex Daytona), early-Apr'26, and more recently in end-Apr'26.

EXHIBIT 1: Our ‘core’ resale price tracker, which only includes data on the Birkin 25/30 and Kelly 25/28   
Hermès Birkin & Kelly Resale Premium (volume weighted average)   
![](images/5a9c5680e639eb4f366043d0db8c9d49dacc5d0530c1259bf6f43249d3bb00c9.jpg)

<details>
<summary>line</summary>

| Quarter | Value (x) |
|---|---|
| 1Q14 | 2.3 |
| 2Q14 | 1.6 |
| 3Q14 | 1.6 |
| 4Q14 | 1.9 |
| 1Q15 | 1.6 |
| 2Q15 | 1.2 |
| 3Q15 | 1.6 |
| 4Q15 | 1.3 |
| 1Q16 | 1.7 |
| 2Q16 | 1.4 |
| 3Q16 | 1.9 |
| 4Q16 | 1.4 |
| 1Q17 | 1.6 |
| 2Q17 | 1.7 |
| 3Q17 | 1.7 |
| 4Q17 | 1.7 |
| 1Q18 | 1.7 |
| 2Q18 | 1.6 |
| 3Q18 | 2.1 |
| 4Q18 | 1.8 |
| 1Q19 | 2.0 |
| 2Q19 | 1.9 |
| 3Q19 | 1.9 |
| 4Q19 | 2.2 |
| 1Q20 | 2.1 |
| 2Q20 | 2.2 |
| 3Q20 | 1.9 |
| 4Q20 | 1.9 |
| 1Q21 | 1.8 |
| 2Q21 | 1.7 |
| 3Q21 | 1.7 |
| 4Q21 | 1.6 |
| 1Q22 | 1.6 |
| 2Q22 | 1.4 |
| 3Q22 | 1.7 |
| 4Q22 | 1.4 |
| 1Q23 | 1.5 |
| 2Q23 | 1.4 |
| 3Q23 | 1.5 |
| 4Q23 | 1.6 |
| 1Q24 | 1.4 |
| 2Q24 | 1.5 |
| 3Q24 | 1.6 |
| 4Q24 | 1.4 |
| 1Q25 | 1.5 |
| 2Q25 | 1.6 |
| 3Q25 | 1.2 |
| 4Q25 | 1.4 |
| 1Q26 | 1.5 |
The dashed line indicates a reference level of the value of the data points on the x-axis (e.g., “1.68x” or “0” in the chart). The y-axis is labeled numerically and corresponds to the x-axis label.
</details>

Includes resale price premia for the Birkin 25 Togo, Birkin 30 Togo, Kelly 25 Epsom, Kelly 28 Epsom Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 2: Our expanded tracker now includes data on the Mini Kelly II and Kelly Pochette   
Hermès Birkin, Kelly, Mini Kelly & Kelly Pochette Resale Premium (volume weighted average)   
![](images/df1788a4f21de78baaa1de3a7f2b7b01358ae877aa50a99f0da003ac9f4b02af.jpg)

<details>
<summary>line</summary>

| Quarter | Value (x) |
|---|---|
| 1Q14 | 2.3 |
| 3Q14 | 1.6 |
| 1Q15 | 1.6 |
| 3Q15 | 1.8 |
| 1Q16 | 1.2 |
| 3Q16 | 1.6 |
| 1Q17 | 1.3 |
| 3Q17 | 1.8 |
| 1Q18 | 1.4 |
| 3Q18 | 2.0 |
| 1Q19 | 1.4 |
| 3Q19 | 1.7 |
| 1Q20 | 1.8 |
| 3Q20 | 1.7 |
| 1Q21 | 1.6 |
| 3Q21 | 1.9 |
| 1Q22 | 2.1 |
| 3Q22 | 2.4 |
| 1Q23 | 2.4 |
| 3Q23 | 2.3 |
| 1Q24 | 2.2 |
| 3Q24 | 2.0 |
| 1Q25 | 2.0 |
| 3Q25 | 1.8 |
| 1Q26 | 1.8 |
| 3Q26 | 1.7 |
| 1Q27 | 1.8 |
| 3Q27 | 1.9 |
| 1Q28 | 1.8 |
| 3Q28 | 1.5 |
| 1Q29 | 1.8 |
| 3Q29 | 1.6 |
| 1Q30 | 1.8 |
</details>

Includes resale price premia for the Birkin 25 Togo, Birkin 30 Togo, Kelly 25 Epsom, Kelly 28 Epsom, Mini Kelly II 20 Epsom, and Kelly Pochette   
Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 3: Our 'core' tracker on a half-yearly basis   
Hermès Birkin & Kelly Resale Premium (volume weighted average)   
![](images/0d50d7c5faefdc68e1cc75471e97cdcbcc345d03c8e5ef1c60d8772dec98c3d0.jpg)

<details>
<summary>line</summary>

| Period | Value (x) |
|---|---|
| 2014H2 | 1.3 |
| 2015H1 | 1.6 |
| 2015H2 | 1.9 |
| 2016H1 | 1.4 |
| 2016H2 | 1.3 |
| 2017H1 | 1.7 |
| 2017H2 | 1.4 |
| 2018H1 | 1.9 |
| 2018H2 | 1.5 |
| 2019H1 | 1.7 |
| 2019H2 | 1.7 |
| 2020H1 | 1.6 |
| 2020H2 | 2.0 |
| 2021H1 | 1.9 |
| 2021H2 | 2.1 |
| 2022H1 | 2.1 |
| 2022H2 | 1.9 |
| 2023H1 | 1.8 |
| 2023H2 | 1.6 |
| 2024H1 | 1.6 |
| 2024H2 | 1.5 |
| 2025H1 | 1.5 |
| 2025H2 | 1.5 |
| 2026H1 | 1.4 |
The chart displays a series of values over time, with a horizontal reference line at 1.69x for comparison.
</details>

Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 4: Our expanded tracker on a half-yearly basis   
Hermès Birkin, Kelly, Mini Kelly & Kelly Pochette Resale Premium (volume weighted average)   
![](images/0920290b73fbaa1dce8a8943064b4345088d681ed0235e82d45ed1b62a6a2e1e.jpg)

<details>
<summary>line</summary>

| Period | Value (x) |
|---|---|
| 2014H2 | 1.3 |
| 2015H1 | 1.6 |
| 2015H2 | 1.8 |
| 2016H1 | 1.4 |
| 2016H2 | 1.3 |
| 2017H1 | 1.8 |
| 2017H2 | 1.4 |
| 2018H1 | 2.0 |
| 2018H2 | 1.6 |
| 2019H1 | 1.8 |
| 2019H2 | 1.8 |
| 2020H1 | 1.6 |
| 2020H2 | 2.0 |
| 2021H1 | 2.1 |
| 2021H2 | 2.4 |
| 2022H1 | 2.4 |
| 2022H2 | 2.2 |
| 2023H1 | 2.0 |
| 2023H2 | 1.8 |
| 2024H1 | 2.0 |
| 2024H2 | 1.8 |
| 2025H1 | 1.8 |
| 2025H2 | 1.7 |
| 2026H1 | 1.8 |
</details>

Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 5: Share of auction lots by handbag   
Hermès Birkin, Kelly, Mini Kelly & Kelly Pochette Resale Volume Share   
![](images/38bc91811c6c229e490cea5cfcd3157a45026b628151f5a473f08048b396b3fa.jpg)  
Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 6: Birkin 25 Togo estimated resale prices, by region   
Birkin 25 Togo Auction & Retail Prices (By Region, USD)   
![](images/bcafe3a46341e78a4fc33c65620eed834138df243a4fb0e3a19df6e7241f3b9e.jpg)  
Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 7: Birkin 30 Togo estimated resale prices, by region   
Birkin 30 Togo Auction & Retail Prices (By Region, USD)   
![](images/60a9f917a922ac381674b74a1450114b5f9d03e9ff135c82fbf79af492ca1f24.jpg)

<details>
<summary>line</summary>

| Period   | EUROPE | HONG KONG | UNITED STATES | Retail | Avg. Multiple |
|----------|--------|-----------|--------------|--------|---------------|
| 2014H2   |        |           |              |        | 1.9x          |
| 2015H1   |        |           |              |        | 1.5x          |
| 2015H2   |        |           |              |        | 1.9x          |
| 2016H1   |        |           |              |        | 1.2x          |
| 2016H2   |        |           |              |        | 1.3x          |
| 2017H1   |        |           |              |        | 1.5x          |
| 2017H2   |        |           |              |        | 1.2x          |
| 2018H1   |        |           |              |        | 1.9x          |
| 2018H2   |        |           |              |        | 1.6x          |
| 2019H1   |        |           |              |        | 1.4x          |
| 2019H2   |        |           |              |        | 1.4x          |
| 2020H1   |        |           |              |        | 1.4x          |
| 2020H2   |        |           |              |        | 1.7x          |
| 2021H1   |        |           |              |        | 1.6x          |
| 2021H2   |        |           |              |        | 1.7x          |
| 2022H1   |        |           |              |        | 1.7x          |
| 2022H2   |        |           |              |        | 1.7x          |
| 2023H1   |        |           |              |        | 1.5x          |
| 2023H2   |        |           |              |        | 1.4x          |
| 2024H1   |        |           |              |        | 1.4x          |
| 2024H2   |        |           |              |        | 1.3x          |
| 2025H1   |        |           |              |        | 1.3x          |
| 2025H2   |        |           |              |        | 1.0x          |
| 2026H1   |        |           |              |        | 1.2x          |
</details>

Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 8: Kelly 25 Epsom estimated resale prices, by region   
Kelly 25 Epsom Auction & Retail Prices (By Region, USD)   
![](images/7dc29ed6d3a6030a06771ecf9a2ceb037167839ab6aa94a18e65ff23e8749032.jpg)

<details>
<summary>line</summary>

| Period   | EUROPE | HONG KONG | UNITED STATES | Retail |
|----------|--------|-----------|--------------|--------|
| 2014H2   |        |           |              |        |
| 2015H1   |        |           |              | 10,000 |
| 2015H2   |        |           |              | 10,000 |
| 2016H1   |        |           |              | 10,000 |
| 2016H2   |        |           |              | 10,000 |
| 2017H1   |        |           |              | 10,000 |
| 2017H2   |        |           |              | 10,000 |
| 2018H1   |        |           |              | 10,000 |
| 2018H2   |        |           |              | 9,500  |
| 2019H1   |        |           |              | 17,500 |
| 2019H2   |        |           |              | 17,500 |
| 2020H1   |        |           |              | 19,500 |
| 2020H2   |        |           |              | 18,500 |
| 2021H1   |        |           |              | 18,500 |
| 2021H2   |        |           |              | 18,500 |
| 2022H1   |        |           |              | 26,500 |
| 2022H2   |        |           |              | 24,500 |
| 2023H1   |        |           |              | 26,500 |
| 2023H2   |        |           |              | 24,500 |
| 2024H1   |        |           |              | 24,500 |
| 2024H2   |        |           |              | 18,500 |
| 2025H1   |        |           |              | 23,500 |
| 2025H2   |        |           |              | 16,500 |
| 2026H1   |        |           |              | 21,500 |
The chart displays a line graph with markers for each region. The x-axis represents time periods from 2014H2 to 2026H1. The y-axis represents numerical values ranging from 9,500 to 30,000. Legend indicates: EUROPE (blue line), HONG KONG (dark blue line), UNITED STATES (cyan line), Retail (green line). Annotations above the chart indicate relative multiples of the average multiple (×) for each region. Values are annotated above the lines as multiples of the average multiple.
</details>

Source: Sotheby's, Christie's, Cherry Sang, Bernstein analysis and estimates

EXHIBIT 9: Kelly 28 Epsom estimated resale prices, by region   
Kelly 28 Epsom Auction & Retail Prices (By Region, USD)   
![](images/8800bfd57e3558ad93470ae2a334e23cf8a40bc1a6dbddc56ffa92a9c8d5513f.jpg)

<details>
<summary>line</summary>

| Period   | EUROPE | HONG KONG | UNITED STATES | Retail | Avg. Multiple |
|----------|--------|-----------|--------------|--------|---------------|
| 2014H2   |        |           |              |        |               |
| 2015H1   |        |           |              |        |               |
| 2015H2   |        |           |              |        |               |
| 2016H1   |        | 35,000    |              |        |               |
| 2016H2   |        | 14,000    |              |        |               |
| 2017H1   |        | 23,000    |              |        |               |
| 2017H2   |        | 15,000    |              |        |               |
| 2018H1   |        |           |              |        |               |
| 2018H2   |        | 20,000    |              |        |               |
| 2019H1   |        | 13,500    |              |        |               |
| 2019H2   |        | 19,500    |              |        |               |
| 2020H1   |        | 22,500    |              |        |               |
| 2020H2   |        | 21,500    |              |        |               |
| 2021H1   |        | 26,500    | 25,500       |        |               |
| 2021H2   |        | 30,000    | 24,000       |        |               |
| 2022H1   |        | 22,500    | 21,500       |        |               |
| 2022H2   |        | 19,500    | 19,500       |        |               |
| 2023H1   |        | 19,500    | 23,500       |        |               |
| 2023H2   |        | 14,500    | 18,500       |        |               |
| 2024H1   |        | 17,500    | 16,500       |        |               |
| 2024H2   |        | 16,500    | 18,500       |        |               |
| 2025H1   |        | 15,500    | 18,500       |        |               |
| 2025H2   |        | 16,500    | 17,500       |        |               |
| 2026H1   |        | 14,500    | 13,500       |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |        |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |
|            |                |           |              |        |               |

| Average Multiple (x) |
| ------------------- |
|                     |
|  

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
