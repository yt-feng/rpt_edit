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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Japan Autos & Auto Parts

# Best of Times, Worst of Times: How K-shaped polarization is reshaping Japan's auto market

![](images/f45d3e17966c2941a02ced4e29091d75de64d4829fd8ccf8459767b8338e0c09.jpg)  
Masahiro Akita  
+81 3 6777 6998

masahiro.akita@bernsteinsg.com

![](images/691d44a0d3dfa78270052df3fe5b881414124011006e6c740d3ae42ccd88eee6.jpg)

Seunghyeok Kim

+81 3 6777 6974

seunghyeok.kim@bernsteinsg.com

![](images/0bf9bf2f0987b582277e202090c692ec22577b7b3cee4083fe13e9db982bcd44.jpg)

Tomohiro Kashimoto

+81 3 6777 6975

tomohiro.kashimoto@bernsteinsg.com

"It was the best of times, it was the worst of times". The famous opening line of Charles Dickens' 'A Tale of Two Cities' captures a period of contradiction: the French aristocracy indulging in opulence and privilege, the peasantry experiencing poverty and oppression. While 2026 is thankfully not 18th century France, shifting class dynamics remain more topical than ever, from the US K-shaped economy to the squeezed Chinese middle class. In this note, we examine how K-shaped polarization is reshaping Japan's auto market, weakening affordability, and changing automakers' competitive positioning.

K-shaped polarization is reshaping Japan's auto market: Demand in Japan's auto market is becoming polarized between low-end and high-end vehicles. Between 2015 and 2025, monthly new car purchase spending per household declined as much as $22\%$ among lower-income households, while increasing as much as $32\%$ among higher-income households. Car ownership also became more polarized, with the ownership rate gap between lower-income and higher-income households widening from $27\%$ to $30\%$ p. Polarization is also visible in currently owned vehicle prices. The share of low-end vehicles priced below JPY 1 mn increased from $1\%$ in 2017 to $6\%$ in 2025, while the share of high-end vehicles priced above JPY 5 mn rose from $6\%$ to $15\%$ . In contrast, the share of vehicles priced at JPY 1-2 mn, the largest volume segment, declined from $46\%$ to $19\%$ .

## Affordability pressure is weakening car ownership among lower-income

households: Rising financial burdens from car ownership are affecting demand. Japan's real monthly disposable income declined 5% from its 2020 peak of JPY 499 thousand to JPY 476 thousand in 2025, reflecting inflation. The impact of weaker real purchasing power was more pronounced among lower-income households. In 2025, the proportion of households describing car ownership costs as a financial burden reached 44% among lower-income households, compared with 29% among higher-income households.

## Automakers with exposure to both low-end and high-end demand are better

positioned: K-shaped polarization in Japan's auto market could increasingly affect automakers' sales mix and profitability. In 2025, the combined domestic sales mix of the lowest-priced segment below JPY 2 mn and the highest-priced segment above JPY 5 mn was highest for Suzuki at $74\%$ and Toyota at $43\%$ , followed by Honda at $38\%$ , Mazda at $37\%$ , Nissan at $29\%$ , and Subaru at $10\%$ . Meanwhile, operating margins in Japan were also highest for Toyota at $11\%$ and Suzuki at $9\%$ , followed by Nissan at $0\%$ , Mazda at $-5\%$ , Subaru at $-11\%$ , and Honda at $-14\%$ . This suggests that automakers with exposure to both low-end and high-end segments tend to maintain higher profitability under a K-shaped demand environment, with Toyota and Suzuki appearing relatively well positioned.

Shared mobility benefits as car ownership becomes less affordable: Japan's shared mobility market, including car sharing and ride sharing, is expanding alongside K-shaped polarization. As the economic rationality of car ownership declines, some ownership demand could shift toward shared mobility. As the market expands, automakers may increasingly need to focus not only on manufacturing and sales, but also on recurring revenue generation across the vehicle lifecycle and downstream service capabilities.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="3">Ticker</td><td rowspan="3">Rating</td><td colspan="4">24 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td>ClosingPrice</td><td>PriceTarget</td><td>PriceTarget</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cur</td><td>Price</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>7203.JP (Toyota)</td><td>O</td><td>JPY</td><td>2,686.00</td><td>4,200.00</td><td>(39.2)%</td><td>JPY</td><td>295.25</td><td>308.93</td><td>367.29</td><td>9.1</td><td>8.7</td><td>7.3</td><td></td></tr><tr><td>7269.JP (Suzuki)</td><td>O</td><td>JPY</td><td>1,883.50</td><td>2,550.00</td><td>(36.4)%</td><td>JPY</td><td>227.69</td><td>234.71</td><td>255.99</td><td>8.3</td><td>8.0</td><td>7.4</td><td></td></tr><tr><td>7267.JP (Honda)</td><td>M</td><td>JPY</td><td>1,391.50</td><td>1,300.00</td><td>(47.0)%</td><td>JPY</td><td>(106.06)</td><td>161.84</td><td>147.24</td><td>(13.1)</td><td>8.6</td><td>9.5</td><td></td></tr><tr><td>7201.JP (Nissan)</td><td>U</td><td>JPY</td><td>301.00</td><td>350.00</td><td>(57.7)%</td><td>JPY</td><td>(152.58)</td><td>4.78</td><td>53.06</td><td>(2.0)</td><td>62.9</td><td>5.7</td><td></td></tr><tr><td>7261.JP (Mazda)</td><td>U</td><td>JPY</td><td>1,072.00</td><td>1,000.00</td><td>(18.1)%</td><td>JPY</td><td>55.64</td><td>116.61</td><td>142.17</td><td>19.3</td><td>9.2</td><td>7.5</td><td></td></tr><tr><td>7270.JP (Subaru)</td><td>U</td><td>JPY</td><td>2,375.00</td><td>2,350.00</td><td>(50.4)%</td><td>JPY</td><td>125.50</td><td>222.96</td><td>249.75</td><td>18.9</td><td>10.7</td><td>9.5</td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,627.28</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Toyota Outperform with an updated price target of JPY 4,200.00.

We rate Suzuki Outperform with a price target of JPY 2,550.00.

We rate Honda Market-Perform with a price target of JPY 1,300.00.

We rate Nissan Underperform with a price target of JPY 350.00.

We rate Subaru Underperform with an price target of JPY 2,350.00.

We rate Mazda Underperform with a price target of JPY 1,000.00.

## K-SHAPED POLARIZATION IS RESHAPING JAPAN'S AUTO MARKET

## Higher-income households are spending more while lower-income households are spending less

From 2015 to 2025, monthly new car purchase spending per household in Japan increased only marginally from JPY 10.3 thousand to JPY 10.5 thousand, up 2%, suggesting limited change at the aggregate level. However, a clear divergence emerged between lower-income and higher-income households when viewed by income bracket (Exhibit 1). In this part, households with annual income below JPY 4 mn are classified as lower-income households, while households with annual income above JPY 12.5 mn are classified as higher-income households, based on the income categories defined by Japan's Ministry of Internal Affairs and Communications.

Among lower-income households with annual income below JPY 4 mn, monthly new car purchase spending declined across all income brackets. More specifically, spending among households earning below JPY 2 mn declined 22%, from JPY 2.9 thousand to JPY 2.3 thousand. Households earning JPY 2-3 mn also declined 6%, from JPY 5.2 thousand to JPY 4.9 thousand, while households earning JPY 3-4 mn declined 16%, from JPY 7.6 thousand to JPY 6.4 thousand.

Meanwhile, among higher-income households with annual income above JPY 12.5 mn, monthly new car purchase spending increased across all income brackets. More specifically, spending among households earning JPY 12.5-15 mn increased 6%, from JPY 24.4 thousand to JPY 25.8 thousand. Households earning JPY 15-20 mn also increased 3%, from JPY 29.4 thousand to JPY 30.4 thousand, while households earning above JPY 20 mn increased 32%, from JPY 24.3 thousand to JPY 32.0 thousand.

EXHIBIT 1: Among lower-income households with annual income below JPY 4 mn, new car purchase spending declined across all income brackets, while among higher-income households with annual income above JPY 12.5 mn, new car purchase spending increased across all income brackets

Monthly Spending per Household by Income Bracket (New Car Purchase)

![](images/cb0ed6a23cfaf3894d4455e40735e3d4ffa026cc10f4b3cc7f0cd0404a77db45.jpg)  
Source: Ministry of Internal Affairs and Communications, Bernstein analysis

K-shaped polarization is likely to progress not only in current car ownership, but also in future new car demand in Japan's auto market

From here onward, households with annual income below JPY 3.6 mn are classified as lower-income households, while households with annual income above JPY 7.8 mn are classified as higher-income households, based on the income categories defined by JAMA (Japan Automobile Manufacturers Association). Against the backdrop of Japan's broader trend of declining interest in car ownership, the overall car ownership rate in Japan declined from $80\%$ in 2019 to $72\%$ in 2025, down $8\%$ p (Exhibit 2).

Meanwhile, by income bracket, lower-income households saw a larger decline in car ownership rates. Among lower-income households earning below JPY 2.2 mn, car ownership declined from 61% to 54%, down 7%p. Households earning JPY 2.2-3.6 mn also saw a 6%p decline, from 77% to 71%. In contrast, among higher-income households earning above JPY 7.8 mn, car ownership declined only 5%p, from 88% to 83%. The ownership gap between households earning below JPY 2.2 mn and those earning above JPY 7.8 mn also widened from 27%p in 2019 to 30%p in 2025, suggesting increasing polarization in car ownership (Exhibit 3).

EXHIBIT 2: Car ownership rates declined more sharply among lower-income households, with the gap between households earning below JPY 2.2 mn and above JPY 7.8 mn widening from 27%p in 2019 to 30%p in 2025  
![](images/cf28191bec2103b17bc8c875fe8e303a3eb11f70f7f9a4d1d9392167a7149969.jpg)  
Source: JAMA, Bernstein analysis

EXHIBIT 3: The gap in car ownership rates between households earning below JPY 2.2 mn and those earning above JPY 7.8 mn also widened from 27%p in 2019 to 30%p in 2025  
![](images/175b3c49b44d6d858aecab1fccdea58a8d2625c6ea0483186f52020c9ed54a52.jpg)  
Source: JAMA, Bernstein analysis

Car purchase intention among non-owner households also shows weaker demand among lower-income households and stronger demand among higher-income households. As of 2025, the combined purchase intention ratio for ‘planning to purchase within the next three years’, ‘planning to purchase within four to five years’, and ‘planning to purchase after five years’ was 7% across all households. Among households earning above JPY 7.8 mn, the ratio was 9%, exceeding the 7% average for all households. In contrast, the ratio remained at 6% among households earning JPY 2.2-3.6 mn and 4% among households earning below JPY 2.2 mn, both below the all-household average (Exhibit 4).

The survey on latent car ownership intention, assuming no constraints such as financial limitations or driver's license ownership, also suggests stronger ownership intention among higher-income households. As of 2025, the combined ratio of households answering ‘want to own’ and ‘somewhat want to own’ reached 23% among households earning above JPY 7.8 mn. In contrast, the ratio remained at 19% among households earning below JPY 2.2 mn and 21% among households earning JPY 2.2-3.6 mn (Exhibit 5).

Another notable point is that the trend of declining interest in car ownership itself is becoming increasingly polarized by income bracket. In the same survey, 67% of non-owner households across all households answered that they did not intend to own a car, combining responses of ‘do not want to own’ and ‘do not really want to own’. By income bracket, the ratio reached 70% among lower-income households earning below JPY 2.2 mn and 69% among households earning JPY 2.2-3.6 mn. In contrast, the ratio remained at 64% among higher-income households earning above JPY 7.8 mn.

EXHIBIT 4: Lower-income households tend to show weaker vehicle purchase demand  
![](images/200ca019dbb1e245de6859232af514cec50aaf26c7b10e31209878d445a2c692.jpg)  
Source: JAMA, Bernstein analysis

EXHIBIT 5: Higher-income households tend to show stronger vehicle ownership intention  
![](images/d8f6d6ab1d1b173c48c8ac4ad6e9b33834895532335585cb6eead831f3869e40.jpg)  
Source: JAMA, Bernstein analysis

## Some lower-income households are showing signs not only of weaker car replacement demand, but also of stopping car ownership altogether

K-shaped polarization is also becoming increasingly visible in replacement demand among car-owning households. As of 2025, the car replacement intention ratio across all households stood at 26%. By income bracket, the ratio reached 34% among higher-income households earning above JPY 7.8 mn, exceeding the all-household average. In contrast, the ratio remained at 22% among lower-income households earning JPY 2.2-3.6 mn and 20% among households earning below JPY 2.2 mn, both below the all-household average (Exhibit 6)

Meanwhile, some lower-income households are also showing signs of suspending car ownership altogether. As of 2025, the car ownership discontinuation intention ratio across all households stood at 9%. However, the ratio reached 19% among lower-income households earning below JPY 2.2 mn and 15% among households earning JPY 2.2-3.6 mn, both materially above the all-household average. In contrast, among households earning above JPY 7.8 mn, both below the all-household average (Exhibit 7).

EXHIBIT 6: K-shaped polarization is also emerging in replacement demand among car-owning households  
![](images/bf4f8adf871ab11e7c4c7771ce5d219366884c877e0a88ea97ccdcaf04bd35b0.jpg)  
Source: JAMA, Bernstein analysis  
EXHIBIT 7: Some lower-income households are also showing signs of suspending car ownership altogether

![](images/33011515147e03612042e393cba979828c8cb1f1d73c9dff0920006a13e2e860.jpg)  
Source: JAMA, Bernstein analysis

## K-shaped polarization is also progressing across the price ranges of currently owned cars

From 2017 to 2025, changes also emerged in the purchase price of new and used cars currently owned. While the share of low-end and high-end vehicles increased, the share of mid-priced vehicles declined. More specifically, the share of low-end vehicles priced below JPY 1 mn increased from 1% in 2017 to 6% in 2025, while the share of high-end vehicles priced above JPY 5 mn also increased from 6% to 15%. In contrast, the share of cars priced between JPY 1-2 mn, previously the largest volume segment, declined from 46% to 19%. Japan's auto market is seeing K-shaped polarization, with demand shifting away from the traditional mid-priced mass market toward both low-end and high-end vehicle segments (Exhibit 8).

EXHIBIT 8: The share of low-end vehicles priced below JPY 1 mn increased from 1% in 2017 to 6% in 2025, while the share of high-end vehicles priced above JPY 5 mn also increased from 6% to 15%

![](images/2e6ec37208496c8f3dc43c1cbd5eb575d96931d55fea8a9ee139377dd6d42bd4.jpg)  
Note: Cars counted were purchased within the past two years  
Source: JAMA, Bernstein analysis

## AFFORDABILITY PRESSURE IS WEAKENING CAR OWNERSHIP AMONG LOWER-INCOME HOUSEHOLDS

## Japan's real purchasing power and real disposable income per capita have been trending downward amid prolonged low growth and inflation

Rising financial burdens associated with car ownership are increasingly affecting individual car demand. Since the collapse of Japan's bubble economy in the 1990s, the country has experienced a prolonged period of low economic growth. Real GDP growth gradually declined from $4.8\%$ in 1990, reaching $-5.6\%$ during the global financial crisis and $-4.1\%$ in 2020 amid the COVID-19 pandemic. Growth has since remained largely in the $0 - 1\%$ range, suggesting that Japan's economy has remained in a long-term low-growth environment. Real wages, adjusted for inflation, have also remained sluggish and have been declining since 2021 (Exhibit 9).

In terms of nominal monthly disposable income over the past decade, household income appears to have improved at first glance, increasing 24% from JPY 429 thousand in 2016 to JPY 532 thousand in 2025. However, CPI has continued to rise since 2022 and reached 12p as of 2025. Reflecting the impact of inflation, real monthly disposable income declined 5% from its 2020 peak of JPY 499 thousand to JPY 476 thousand in 2025 (Exhibit 10).

EXHIBIT 9: As a result of prolonged stagnation in real GDP growth and real wages, real purchasing power per capita has been trending downward

![](images/39896a200ad4331158313fc1e51e7bad07bfadb0cb04d8ae8ac3c9646379bd8c.jpg)  
Source: Ministry of Health, Labour and Welfare, IMF, Bernstein analysis  
EXHIBIT 10: Real monthly disposable income declined 5% from its 2020 peak of JPY 499 thousand to JPY 476 thousand in 2025

![](images/9b4b9913db7f3090e29fe424b5903e8b0e9fd51b6ed7c38576ebb1f7ef20b4f5.jpg)  
Source: Ministry of Internal Affairs and Communications, Bernstein analysis

## Lower purchasing power is leading to diverging ownership behavior

Japanese automakers' ASPs have generally trended upward since 2015, although the degree of increase has varied by company. Average ASP increased $32\%$ , from JPY 2.9 mn in 2015 to JPY 3.8 mn in 2025. By automaker, Honda's ASP increased $50\%$ , from JPY 2.3 mn to JPY 3.5 mn, while Mazda's ASP also increased $49\%$ , from JPY 2.9 mn to JPY 4.3 mn. Suzuki, despite maintaining a sales mix centered on lower-priced cars, saw ASP increase $39\%$ , from JPY 1.4 mn to JPY 2.0 mn. Subaru's ASP increased $33\%$ , from JPY 4.2 mn to JPY 5.5 mn, while Toyota's ASP increased $13\%$ , from JPY 2.9 mn to JPY 3.3 mn (Exhibit 11).

EXHIBIT 11: Industry average ASP increased 32%, from JPY 2.9 mn in 2015 to JPY 3.8 mn in 2025  
![](images/27b88be270de151da75ef2f8db6399bf20dfff642d45ab9eb7fb82e02186f84c.jpg)  
Source: IHS, Company websites, Bernstein analysis

Inflation is having a larger impact on car usage and ownership among lower-income households. As of 2025, the ratio of households answering that inflation had an impact on car usage, including ‘reduced frequency of car use’, reached 37% among lower-income households earning below JPY 2.2 mn and 34% among households earning JPY 2.2-3.6 mn, the highest levels across all incom

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
