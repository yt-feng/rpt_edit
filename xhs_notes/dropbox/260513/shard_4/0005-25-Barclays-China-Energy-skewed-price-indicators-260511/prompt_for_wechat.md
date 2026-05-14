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
# China

# Energy-skewed price indicators

April inflation data show oil prices driving a sharp PPI rebound and higher energy CPI, while core and services inflation stayed muted. Upstream price pressures surged, but weak pass-through to downstream sectors. Soft core and services pointed to limited second round effects.

• April: 1.2% y/y for CPI, and 2.8% y/y for PPI   
- Bloomberg consensus forecast (BARC): $0.9\%$ $(0.8\%)$ y/y for CPI, and $1.8\%$ $(1.2\%)$ y/y for PPI   
• March: 1.0% y/y for CPI, and 0.5% y/y for PPI

The April price data suggest that rising oil prices continued to push up PPI inflation and energy-related components of CPI, while the impact on core and services CPI remained contained, pointing to limited second-round effects. After PPI exited deflation in March for the first time since late 2022, it accelerated further to 2.8% y/y (from 0.5%), far exceeding market expectations (Bloomberg: 1.8%; BARC: 1.2%). On a month-on-month basis, PPI surged to a post-COVID high of 1.7% in April, up from 1.0%, suggesting a lagged pass-through from earlier oil price increases, even though the rise in oil prices was less pronounced in April than in March.

The PPI breakdown shows that the rebound was mainly driven by upstream raw materials (April: 7.1% y/y vs 1.1% in March) and mining (10.6% vs 2.0%), while price pressures in downstream consumer goods (-1.0% vs -1.3%) and manufacturing sectors (1.5% vs 0.9%) remained much more muted. This suggests that downstream firms are still struggling to pass higher input costs further along the value chain. Within upstream sectors, PPI for oil and gas extraction surged to 29% y/y in April, the strongest reading since late 2022. Higher oil prices also spilled over into coal, with PPI for coal mining and washing turning positive for the first time since mid-2024.

While CPI inflation rose by 0.2pp to 1.2% y/y in April, we think this modest pickup in headline inflation mainly reflected energy-driven supply-side constraints rather than demand-led reflation or second-round effects. We estimate the contribution from energy to headline CPI rose by about 0.5pp in April, compared with only a 0.2pp increase in headline CPI inflation. This implies that, excluding energy, underlying CPI inflation actually softened in April.

Consistent with this view, several major CPI components continued to decline, including housing rents (April: -0.6% y/y vs -0.5% in March), automobiles (-1.2% vs -1.1%), and household goods and services (1.4% vs 1.5%). Moreover, core CPI remained subdued at 1.1–1.2% in March–April following the Middle East conflict, compared with an average of 1.3% in January–February. Over the same period, services CPI was broadly flat at 0.8–0.9%, slightly below its pre-conflict average of 0.9%, underscoring still-weak domestic demand.

# Yingke Zhou

+852 2903 2653

yingke.zhou@BARC.com

BARC Bank, Hong Kong

# Ying Zhang

+852 2903 2652

ying.zhang3@BARC.com

BARC Bank, Hong Kong

# Jian Chang

+852 2903 2654

jian.chang@BARC.com

BARC Bank, Hong Kong

# CPI breakdown: broadly stable core and services inflation

Looking at the breakdown, we highlight some of the key developments in the CPI data:

\- Goods CPI inflation edged up slightly to 1.4% y/y in April from 1.3% previously, as a sharp rise in gasoline prices more than offset declines in food prices. Domestic gasoline prices surged 19.3% y/y, up from 3.8% in March, contributing around 0.56pp to headline CPI. In contrast, food CPI fell 1.6% y/y, reversing a 0.3% increase in March, driven by a faster decline in pork prices alongside softer vegetable and fruit prices.

Core CPI remained relatively resilient at 1.2% y/y, up marginally from 1.1%, but still below its pre-conflict average of 1.3% in January–February. Within core goods, gold jewellery contributed 0.2pp to headline inflation, although gold price growth moderated. Prices in other key goods categories firmed, with household appliances and clothing rising 2.6% and 1.6% y/y, respectively, together adding about 0.11pp to CPI inflation. By contrast, vehicle prices softened further, with deflation widening slightly to -1.2% y/y from -1.1%. On a month-on-month basis, vehicle prices fell 0.4% in April, marking a second consecutive decline.

\- Services CPI inflation edged up to 0.9% y/y in April from 0.8% in March, broadly in line with its pre-conflict level in January–February. Prices of basic public services remained largely stable, with healthcare services (April: 3.4% y/y vs 3.0% in March) and education services (steady at 0.5%) continuing to rise, together contributing around 0.25pp to headline CPI. Travel-related service prices accelerated further, rising 3.7% y/y and adding about 0.13pp, reflecting the impact of higher oil prices.

Meanwhile, according to the NBS, prices of labour-intensive services increased only modestly. Pet services, dining out, housekeeping, and vehicle repair and maintenance saw price rises of 1.1%–1.4%, jointly contributing roughly 0.10pp to CPI inflation. In contrast, housing rents fell 0.6% y/y, marking the fastest pace of decline since January 2023, while data from the China Index Academy show rents in major Cities declined at a much sharper rate of 3.4% y/y.

# PPI breakdown: notable rise in upstream sectors

April PPI rose 2.8% after returning to positive growth in March with a 0.5% gain. The notable improvement was supported by surging prices in non-ferrous metals and energy-related sectors, with surging copper prices amid strong AI and green tech-related demand and supply concerns amid Middle East conflicts, as well as higher energy prices. On a m/m basis, PPI rose by 1.7% from 1%, the fastest pace since late 2021.

Looking at the breakdown, the producer goods PPI for mining (April: 10.6%, March: 2.0%) and raw materials (April: 7.1%, March: 1.1%) jumped, while manufacturing PPI picked up at much measured pace (April: 1.5%, March: 0.9%). However, the consumer goods PPI remained in deflation, despite some narrowing (April: -1%, March: -1.3%). Meanwhile, the decline in consumer durable goods prices continued, coming in at -0.3% in April, albeit with some moderation from -1% in March.

By sector and on a m/m basis, the PPI for energy-related sectors rose notably amid rising global oil prices. Sectors affected included oil and gas extraction (April: 18.5%, March: 15.8%), fuel processing (April: 16.4%, March: 5.8%), chemicals (April: 8.3%, March: 3.6%), chemical fiber (April: 5.6, March: 3.4%) and rubber and plastics (April: 1.7, March: 0.6%). Moreover, as market competition continues to normalize thanks to the anti-involution campaign, prices of lithium-ion battery manufacturing rose by 1.6% m/m, and prices for EV manufacturing fell at a slower pace of -0.1% (-0.8% in March). New growth drivers are gaining traction: alongside the rapid expansion of the “AI+” ecosystem and surging demand for computing power and accelerating electrification process, prices of optical fiber manufacturing jumped 22.5% m/m, while external storage devices increased 3.2% m/m.

FIGURE 1. PPI exceeded market expectations...   
![](images/e2ff26d323fe6f1c96450cccfd91dcac1beb50bc06970790bbcfff874e90d646.jpg)

<details>
<summary>line</summary>

| Date   | PPI    | PPI: producer goods | Consumer goods |
|--------|--------|--------------------|----------------|
| Apr-23 | -3.0   | -7.0               | 1.0            |
| Oct-23 | -2.5   | -3.5               | -0.5           |
| Apr-24 | -1.0   | -1.0               | -0.5           |
| Oct-24 | -2.5   | -3.0               | -1.0           |
| Apr-25 | -3.0   | -4.0               | -1.5           |
| Oct-25 | -2.0   | -2.5               | -1.0           |
| Apr-26 | 3.0    | 4.0                | -1.0           |
</details>

Source: Wind, BARC

FIGURE 2. ...led by oil and gas extraction   
![](images/087793f5a8475092df11a4d90269694ab90bdfb0f460f6b65df7bdd6b0469f4b.jpg)

<details>
<summary>line</summary>

| Date   | PPI: Oil and gas extraction | Coal mining and washing | Ferrous metals processing | Non-ferrous metals processing | Non-metal minerals processing |
|--------|-----------------------------|--------------------------|----------------------------|-------------------------------|--------------------------------|
| Apr-23 | -25                         | -10                      | -15                        | 5                             | 0                              |
| Oct-23 | 0                           | -15                      | 15                         | 10                            | 0                              |
| Apr-24 | 10                          | -10                      | 5                          | 15                            | 0                              |
| Oct-24 | -15                         | -15                      | -5                         | 20                            | 0                              |
| Apr-25 | -10                         | -20                      | -10                        | 15                            | 0                              |
| Oct-25 | -5                          | -10                      | 0                          | 20                            | 0                              |
| Apr-26 | 30                          | 5                        | 5                          | 40                            | 0                              |
</details>

Source: Wind, BARC

FIGURE 3. Without energy, CPI inflation softens   
![](images/37030c0f28909a29f2d54be7710a24d5824487c21e400efee987eeb79f9c10e8.jpg)

<details>
<summary>bar</summary>

| Date   | Core  | Energy | Pork  | Vegetables | Other food | CPI    |
|--------|-------|--------|-------|------------|------------|--------|
| Apr-23 | 0.5   | 0.3    | 0.2   | 0.1        | 0.9        | 0.1    |
| Oct-23 | 0.6   | 0.4    | 0.3   | 0.2        | 0.8        | -0.1   |
| Apr-24 | 0.7   | 0.5    | 0.4   | 0.3        | 0.7        | 0.2    |
| Oct-24 | 0.8   | 0.6    | 0.5   | 0.4        | 0.6        | 0.3    |
| Apr-25 | 0.9   | 0.7    | 0.6   | 0.5        | 0.5        | 0.4    |
| Oct-25 | 1.0   | 0.8    | 0.7   | 0.6        | 0.4        | 0.5    |
| Apr-26 | 1.1   | 0.9    | 0.8   | 0.7        | 0.3        | 0.6    |
</details>

Source: Wind, BARC

FIGURE 4. Core and services CPI remained broadly stable   
![](images/595bde29a6b1d42fdb7b24325799927409b54d227497af218184fc0ed3fbd129.jpg)

<details>
<summary>line</summary>

| Date   | Core CPI | CPI services |
|--------|----------|--------------|
| Apr-14 | 1.7      | 2.7          |
| Apr-16 | 1.5      | 2.0          |
| Apr-18 | 2.3      | 3.6          |
| Apr-20 | 0.5      | -0.5         |
| Apr-22 | 0.8      | 1.5          |
| Apr-24 | 0.2      | 1.9          |
| Apr-26 | 1.8      | 0.8          |
</details>

Source: Wind, BARC

FIGURE 5. Auto prices fell again   
![](images/15d0cfb83d85f5864436f5ed920144bf041ff44d99e641ca1a221eab2e0864ab.jpg)

<details>
<summary>line</summary>

| Date   | CPI vehicles, % y/y | CPI vehicles, % m/m (RHS) |
|--------|---------------------|----------------------------|
| Apr-21 | -1.5                | 0.0                        |
| Apr-22 | 0.0                 | 0.0                        |
| Apr-23 | -4.5                | -1.5                       |
| Apr-24 | -6.0                | -1.0                       |
| Apr-25 | -4.5                | 0.0                        |
| Apr-26 | -1.5                | 0.5                        |
</details>

Source: Wind, BARC

FIGURE 6. Contribution from gold and platinum jewellery to CPI declined   
![](images/4fa691bcf96e7d88af59d1e6a0c64dbc293420e1ff217e0258323a7475cd43ee.jpg)

<details>
<summary>line</summary>

| Date    | categories excl. gold and platinum jewellery | gold and platinum jewellery | core CPI, % y/y |
|---------|--------------------------------------------------|-----------------------------|-----------------|
| Oct-21  | 1.4                                              | -0.1                        | 1.3             |
| Jul-22  | 1.3                                              | -0.1                        | 1.2             |
| Apr-23  | 0.9                                              | -0.1                        | 0.7             |
| Jan-24  | 0.8                                              | -0.1                        | 1.2             |
| Oct-24  | 0.6                                              | 0.1                         | 0.6             |
| Jul-25  | 1.2                                              | 0.3                         | 1.2             |
| Apr-26  | 1.8                                              | 0.6                         | 1.8             |
</details>

Source: Wind, BARC

FIGURE 7. CPI breakdown and PPI 

<table><tr><td></td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td><td>Apr-25</td></tr><tr><td colspan="14">CPI %y/y</td></tr><tr><td>Headline</td><td>1.2</td><td>1.0</td><td>1.3</td><td>0.2</td><td>0.8</td><td>0.7</td><td>0.2</td><td>-0.3</td><td>-0.4</td><td>0.0</td><td>0.1</td><td>-0.1</td><td>-0.1</td></tr><tr><td>Headline (%m/m)</td><td>0.3</td><td>-0.7</td><td>1.0</td><td>0.2</td><td>0.2</td><td>-0.1</td><td>0.2</td><td>0.1</td><td>0.0</td><td>0.4</td><td>-0.1</td><td>-0.2</td><td>0.1</td></tr><tr><td>Services</td><td>0.9</td><td>0.8</td><td>1.6</td><td>0.1</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.3</td></tr><tr><td>Services (%m/m)</td><td>0.5</td><td>-1.1</td><td>1.1</td><td>0.2</td><td>0.0</td><td>-0.4</td><td>0.2</td><td>-0.3</td><td>0.0</td><td>0.6</td><td>0.0</td><td>0.0</td><td>0.3</td></tr><tr><td>Goods</td><td>1.4</td><td>1.3</td><td>1.1</td><td>0.3</td><td>1.0</td><td>0.6</td><td>-0.2</td><td>-0.8</td><td>-1.0</td><td>-0.4</td><td>-0.2</td><td>-0.5</td><td>-0.3</td></tr><tr><td>Goods (%m/m)</td><td>0.1</td><td>-0.3</td><td>0.8</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.2</td><td>-0.1</td><td>-0.3</td><td>0.0</td></tr><tr><td>Food</td><td>-1.6</td><td>0.3</td><td>1.7</td><td>-0.7</td><td>1.1</td><td>0.2</td><td>-2.9</td><td>-4.4</td><td>-4.3</td><td>-1.6</td><td>-0.3</td><td>-0.4</td><td>-0.2</td></tr><tr><td>Food (%m/m)</td><td>-1.6</td><td>-2.7</td><td>1.9</td><td>0.0</td><td>0.3</td><td>0.5</td><td>0.3</td><td>0.7</td><td>0.5</td><td>-0.2</td><td>-0.4</td><td>-0.2</td><td>0.2</td></tr><tr><td>Core (excluding food and energy)</td><td>1.2</td><td>1.1</td><td>1.8</td><td>0.8</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.6</td><td>0.5</td></tr><tr><td>Core (excluding food and energy, %m/m)</td><td>0.2</td><td>-0.7</td><td>0.7</td><td>0.3</td><td>0.2</td><td>-0.1</td><td>0.2</td><td>0.0</td><td>0.0</td><td>0.4</td><td>0.0</td><td>0.0</td><td>0.2</td></tr><tr><td>Non food</td><td>1.8</td><td>1.2</td><td>1.3</td><td>0.4</td><td>0.8</td><td>0.8</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.1</td><td>0.0</td><td>0.0</td></tr><tr><td>Non food (%m/m)</td><td>0.7</td><td>-0.2</td><td>0.8</td><td>0.2</td><td>0.1</td><td>-0.2</td><td>0.2</td><td>-0.1</td><td>-0.1</td><td>0.5</td><td>0.0</td><td>-0.2</td><td>0.1</td></tr><tr><td>Housing</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.1</td><td>-0.2</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td></tr><tr><td>Recreation</td><td>1.3</td><td>1.1</td><td>2.0</td><td>0.0</td><td>0.9</td><td>0.8</td><td>0.9</td><td>0.8</td><td>1.0</td><td>0.9</td><td>1.0</td><td>0.9</td><td>0.7</td></tr><tr><td>Transportation</td><td>4.6</td><td>0.9</td><td>-0.7</td><td>-3.4</td><td>-2.6</td><td>-2.3</td><td>-1.5</td><td>-2.0</td><td>-2.4</td><td>-3.1</td><td>-3.7</td><td>-4.3</td><td>-3.9</td></tr><tr><td>Medical</td><td>2.2</td><td>1.9</td><td>1.9</td><td>1.7</td><td>1.8</td><td>1.6</td><td>1.4</td><td>1.1</td><td>0.9</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.2</td></tr><tr><td>Clothing</td><td>1.5</td><td>1.6</td><td>1.9</td><td>1.9</td><td>1.7</td><td>1.9</td><td>1.7</td><td>1.7</td><td>1.8</td><td>1.7</td><td>1.6</td><td>1.5</td><td>1.3</td></tr><tr><td>Household facilities</td><td>1.4</td><td>1.5</td><td>2.8</td><td>2.6</td><td>2.2</td><td>2.1</td><td>1.9</td><td>2.2</td><td>1.8</td><td>1.2</td><td>0.7</td><td>0.1</td><td>0.2</td></tr><tr><td>PPI % y/y</td><td>2.8</td><td>0.5</td><td>-0.9</td><td>-1.4</td><td>-1.9</td><td>-2.2</td><td>-2.1</td><td>-2.3</td><td>-2.9</td><td>-3.6</td><td>-3.6</td><td>-3.3</td><td>-2.7</td></tr><tr><td>PPI % m/m</td><td>1.7</td><td>1.0</td><td>0.4</td><td>0.4</td><td>0.2</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.0</td><td>-0.2</td><td>-0.4</td><td>-0.4</td><td>-0.4</td></tr></table>

Source: Wind, BARC

# Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

# Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

# Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.barlays.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may ha

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to sUBScribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
